from dataclasses import dataclass


@dataclass(frozen=True)
class KnowledgeItem:
    topic: str
    answer: str
    keywords: tuple[str, ...]
    patterns: tuple[str, ...] = ()

