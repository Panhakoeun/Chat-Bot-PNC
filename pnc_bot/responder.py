import re
import unicodedata
from difflib import SequenceMatcher

from .knowledge import (
    KNOWLEDGE_BASE,
    PHRASE_ALIASES,
    RELATED_TOPICS,
    STOP_WORDS,
    TOPIC_HINTS,
    TOPIC_LOOKUP,
    UNVERIFIED_RESPONSES,
)
from .models import KnowledgeItem


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    for source, target in PHRASE_ALIASES.items():
        text = text.replace(source, target)
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    return [token for token in normalize_text(text).split() if token and token not in STOP_WORDS]


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def score_item(user_text: str, item: KnowledgeItem) -> float:
    score = 0.0
    tokens = set(tokenize(user_text))
    normalized_text = normalize_text(user_text)
    matched_signal = False

    for pattern in item.patterns:
        pattern_normalized = normalize_text(pattern)
        if pattern_normalized in normalized_text:
            score += 12.0
            matched_signal = True

    for keyword in item.keywords:
        keyword_normalized = normalize_text(keyword)
        keyword_tokens = set(keyword_normalized.split())

        if keyword_normalized in normalized_text:
            score += 5.0
            matched_signal = True
            continue

        if keyword_tokens and keyword_tokens.issubset(tokens):
            score += 4.0
            matched_signal = True
            continue

        overlap = len(tokens & keyword_tokens)
        if overlap:
            score += overlap * 2.0
            matched_signal = True

        if similarity(normalized_text, keyword_normalized) >= 0.84:
            score += 2.5
            matched_signal = True

    return score if matched_signal else 0.0


def build_fallback_response(user_text: str) -> str:
    suggestion = (
        "I am not fully sure about that, and I do not want to guess. I can help with verified PNC topics like "
        f"{', '.join(RELATED_TOPICS[:-1])}, and {RELATED_TOPICS[-1]}."
    )

    if any(word in normalize_text(user_text).split() for word in ("who", "what", "where", "when", "why", "how")):
        return suggestion + " Please try asking your question in a short sentence."

    return suggestion + " For example, you can ask: 'What is the mission of PNC?'"


def detect_topic_by_hints(tokens: set[str]) -> str | None:
    for topic, hints in TOPIC_HINTS.items():
        hit_count = sum(1 for hint in hints if hint in tokens)
        if hit_count >= 2:
            return topic
    return None


def handle_response(text: str) -> str:
    normalized = normalize_text(text)
    if not normalized:
        return "Please type a question about Passerelles Numeriques Cambodia."

    tokens = set(tokenize(normalized))

    if {"scholarship", "bursary"} & tokens or ({"financial", "aid"} <= tokens or {"financial", "support"} <= tokens):
        return TOPIC_LOOKUP["scholarship"].answer

    if ("partner" in normalized or "company" in normalized or "business" in normalized) and (
        "contact" in normalized or "who" in normalized or "email" in normalized
    ):
        return TOPIC_LOOKUP["partner_contact"].answer

    if {"where", "location", "address", "contact", "phone", "email"} & set(normalized.split()):
        return TOPIC_LOOKUP["location"].answer

    if (
        "country director" in normalized
        or "who is the director of pnc" in normalized
        or ("leader" in normalized and "pnc" in normalized)
    ):
        return TOPIC_LOOKUP["country_director"].answer

    if "principal" in normalized or "who leads pnc" in normalized:
        return UNVERIFIED_RESPONSES["principal"]

    if (
        "what do students learn" in normalized
        or "what do pnc students learn" in normalized
        or ("major" in normalized and "learn" in normalized)
    ):
        return TOPIC_LOOKUP["curriculum"].answer

    if "qualification" in normalized or ("degree" in normalized and "get" in normalized) or "certificate" in normalized:
        return TOPIC_LOOKUP["degree"].answer

    if "requirements" in normalized or "requirement" in normalized or "eligible" in normalized:
        return TOPIC_LOOKUP["eligibility"].answer

    if "how many" in normalized and "student" in normalized:
        return TOPIC_LOOKUP["student_count"].answer

    if "how many" in normalized and ({"staff", "teacher", "teachers"} & tokens):
        return UNVERIFIED_RESPONSES["staff_count"]

    if "degree" in normalized:
        return TOPIC_LOOKUP["degree"].answer

    if "curriculum" in tokens or "learn" in normalized:
        return TOPIC_LOOKUP["curriculum"].answer

    if "free" in tokens and "pnc" in normalized:
        return TOPIC_LOOKUP["cost"].answer

    if ("apply" in tokens or "application" in tokens or "admission" in tokens) and "pnc" in normalized:
        return TOPIC_LOOKUP["selection"].answer

    if ("food" in tokens or "meal" in tokens or "meals" in tokens) and ("provide" in tokens or "support" in tokens):
        return TOPIC_LOOKUP["food_allowance"].answer

    if ("accommodation" in tokens or "housing" in tokens or "dormitory" in tokens) and (
        "provide" in tokens or "live" in tokens
    ):
        return TOPIC_LOOKUP["housing"].answer

    if ("health" in tokens or "medical" in tokens or "healthcare" in tokens) and (
        "cover" in tokens or "support" in tokens or "provide" in tokens
    ):
        return TOPIC_LOOKUP["health_support"].answer

    hinted_topic = detect_topic_by_hints(tokens)
    if hinted_topic and hinted_topic in TOPIC_LOOKUP:
        return TOPIC_LOOKUP[hinted_topic].answer

    best_item = None
    best_score = 0.0
    for item in KNOWLEDGE_BASE:
        item_score = score_item(normalized, item)
        if item_score > best_score:
            best_score = item_score
            best_item = item

    if best_item and best_score >= 4.0:
        return best_item.answer

    return build_fallback_response(text)

