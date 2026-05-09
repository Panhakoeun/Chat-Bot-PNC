from .models import KnowledgeItem

OFFICIAL_CONTACT = (
    "Official PNC contact:\n"
    "Address: BP 511 St. 371 Phum Tropeang Chhuk (Borey Sorla), Sangkat Tek Thla, "
    "Khan Sen Sok, Phnom Penh, Cambodia\n"
    "Phone: +855 23 99 55 00\n"
    "Email: info.cambodia@passerellesnumeriques.org\n"
    "Website: https://www.passerellesnumeriques.org/what-we-do/cambodia/"
)

UNVERIFIED_RESPONSES = {
    "principal": (
        "The official PNC Cambodia page lists Hybunna HANG as the Country Director. "
        "If you mean a different role such as principal or another manager, I should not guess.\n\n"
        + OFFICIAL_CONTACT
    ),
    "staff_count": (
        "I do not have a verified current staff count for PNC, so I should not give a number that may be wrong.\n\n"
        + OFFICIAL_CONTACT
    ),
}

KNOWLEDGE_BASE: tuple[KnowledgeItem, ...] = (
    KnowledgeItem(
        topic="greeting",
        answer=(
            "Hello! I am your PNC assistant. Ask me about Passerelles Numeriques Cambodia, "
            "such as its mission, programs, students, support, location, or values."
        ),
        keywords=("hello", "hi", "hey", "good morning", "good afternoon"),
    ),
    KnowledgeItem(
        topic="about_pnc",
        answer=(
            "Passerelles Numeriques Cambodia (PNC) is the Cambodia center of Passerelles Numeriques, "
            "a French non-profit created in 2005. In Phnom Penh, PNC provides a 2-year IT training "
            "program for underserved youth, combining digital skills, professional development, and "
            "support for employment."
        ),
        keywords=("pnc", "passerelles numeriques", "passerelles numeriques cambodia", "about pnc"),
        patterns=("what is pnc", "tell me about pnc", "what is passerelles numeriques cambodia"),
    ),
    KnowledgeItem(
        topic="history",
        answer=(
            "Passerelles Numeriques was created in 2005, and Cambodia is where the first PN program began. "
            "The official Cambodia page says PNC started in Phnom Penh in 2005 with 25 students."
        ),
        keywords=("history", "background", "founded", "established", "created", "started"),
        patterns=("when was pnc founded", "when did pnc start", "tell me the history of pnc"),
    ),
    KnowledgeItem(
        topic="mission",
        answer=(
            "PNC's mission is to unlock the potential of disadvantaged youth by giving them access to "
            "education and key digital-sector skills so they can reach sustainable employment and help "
            "their families escape poverty."
        ),
        keywords=("mission", "goal", "purpose", "objective"),
        patterns=("what is the mission of pnc", "what does pnc do"),
    ),
    KnowledgeItem(
        topic="vision",
        answer=(
            "PN's vision is a world where underprivileged youth can build a better life through access "
            "to education, training, and employment."
        ),
        keywords=("vision",),
        patterns=("what is the vision of pnc", "what is pnc vision"),
    ),
    KnowledgeItem(
        topic="programs",
        answer=(
            "The official Cambodia page describes PNC as a 2-year IT training program in Phnom Penh "
            "with a major in Software Development, designed around the needs of local IT companies."
        ),
        keywords=("program", "programs", "training", "course", "courses", "study", "major"),
        patterns=("what programs does pnc offer", "what can students study at pnc"),
    ),
    KnowledgeItem(
        topic="duration",
        answer=(
            "PNC is known for its free 2-year IT training program for disadvantaged youth, combined with "
            "personal development and employability preparation."
        ),
        keywords=("duration", "how long", "2 year", "two years", "study duration", "program duration"),
        patterns=("how long is the pnc program", "how many years do students study at pnc"),
    ),
    KnowledgeItem(
        topic="degree",
        answer=(
            "According to the official Cambodia page, PNC students receive an Associate Degree in Computer "
            "Science with a major in Software Development, as well as a Passerelles Numeriques certificate."
        ),
        keywords=("degree", "certificate", "diploma", "associate degree", "qualification"),
        patterns=("what degree do pnc students get", "do pnc students receive a certificate"),
    ),
    KnowledgeItem(
        topic="cost",
        answer=(
            "PN says its education is offered at no cost to the student. For PNC specifically, the official "
            "Cambodia page says the program is free and students' basic needs such as housing, food, and "
            "medical care are covered."
        ),
        keywords=("cost", "price", "fee", "fees", "tuition", "free", "payment"),
        patterns=("is pnc free", "do students pay at pnc", "what are the fees at pnc"),
    ),
    KnowledgeItem(
        topic="scholarship",
        answer=(
            "PNC is not described on the official site as a separate scholarship to apply for. Instead, it is a "
            "free 2-year IT training program for disadvantaged youth. Students who are selected into PNC receive "
            "full support, including training, accommodation, food, medical care, and an allowance for additional expenses.\n\n"
            "If you want to join, the correct path is to follow the PNC selection process: attend an information session, "
            "take the written test, join the career guidance step if shortlisted, and complete the home visit and final selection."
        ),
        keywords=("scholarship", "financial aid", "financial support", "full support", "study support", "bursary"),
        patterns=(
            "does pnc offer scholarships",
            "how can i get scholarship at pnc",
            "how to apply for scholarship at pnc",
            "what scholarship does pnc provide",
            "does pnc provide financial aid",
        ),
    ),
    KnowledgeItem(
        topic="departments",
        answer=(
            "Historically, PNC launched with System and Network Administration in 2005 and added "
            "Web Programming in 2009. The current official Cambodia page describes the program as "
            "a 2-year IT training course with a major in Software Development."
        ),
        keywords=("department", "departments", "track", "tracks", "specialization", "specializations"),
        patterns=("what departments are in pnc", "what tracks does pnc offer"),
    ),
    KnowledgeItem(
        topic="curriculum",
        answer=(
            "The official Cambodia page lists technical topics such as MS Office, algorithm, web design, "
            "back-end, object-oriented programming, front-end, software development, databases, and REST API."
        ),
        keywords=("curriculum", "subjects", "technical skills", "modules", "what do students learn"),
        patterns=("what subjects are taught at pnc", "what do pnc students learn"),
    ),
    KnowledgeItem(
        topic="student_support",
        answer=(
            "PNC uses a holistic approach. Alongside IT training, students receive professional development "
            "support, and their basic needs such as housing, food, and medical care are covered."
        ),
        keywords=("support", "benefit", "benefits", "education support", "student support", "allowance"),
        patterns=("what support does pnc provide", "how does pnc help students"),
    ),
    KnowledgeItem(
        topic="daily_life",
        answer=(
            "Student life at PNC is not only about coding or technical lessons. Students also follow soft-skills "
            "training, English, teamwork activities, personal development, and community-style living support."
        ),
        keywords=("daily life", "student life", "life at pnc", "activities", "campus life"),
        patterns=("what is student life like at pnc", "tell me about life at pnc"),
    ),
    KnowledgeItem(
        topic="housing",
        answer=(
            "The official Cambodia page says students' accommodation is covered by PNC, and the dormitories "
            "are located less than 5 minutes on foot from the training center."
        ),
        keywords=("housing", "accommodation", "dormitory", "dorm", "where do students live"),
        patterns=("does pnc provide accommodation", "do pnc students live in dormitories"),
    ),
    KnowledgeItem(
        topic="food_allowance",
        answer=(
            "According to the official Cambodia page, warm meals are served 3 times a day in the training center "
            "and students also receive an allowance for additional expenses."
        ),
        keywords=("food", "meals", "allowance", "daily expenses", "meal support"),
        patterns=("does pnc provide food", "do pnc students get an allowance"),
    ),
    KnowledgeItem(
        topic="health_support",
        answer=(
            "The official Cambodia page says health costs are fully covered by Passerelles Numeriques, and "
            "a socio-educational team supports students throughout their training."
        ),
        keywords=("health", "medical", "hospital", "healthcare", "wellbeing"),
        patterns=("does pnc cover health costs", "what health support does pnc provide"),
    ),
    KnowledgeItem(
        topic="english_soft_skills",
        answer=(
            "PNC helps students grow in both technical and non-technical areas. Besides IT, students improve "
            "their English, communication, teamwork, professional attitude, and life skills."
        ),
        keywords=("english", "soft skills", "communication", "life skills", "professional skills"),
        patterns=("does pnc teach english", "does pnc teach soft skills"),
    ),
    KnowledgeItem(
        topic="values",
        answer=(
            "PN promotes five core values: Trust, Respect, Responsibility, Solidarity, and a fair and rigorous approach."
        ),
        keywords=("value", "values", "core values"),
        patterns=("what are pnc values", "what values does pnc have"),
    ),
    KnowledgeItem(
        topic="employment",
        answer=(
            "PNC focuses strongly on employability. Students receive technical training, soft-skills support, "
            "internship exposure, and guidance toward quality jobs aligned with the local tech market."
        ),
        keywords=("job", "jobs", "employment", "career", "internship", "internships"),
        patterns=("does pnc help students find jobs", "how does pnc support employment"),
    ),
    KnowledgeItem(
        topic="internship",
        answer=(
            "Internships are part of the PN student path. The official mission page shows a journey of "
            "selection, training in center, internship, employment guidance, and then a sustainable digital career."
        ),
        keywords=("internship", "internships", "work placement", "company experience"),
        patterns=("does pnc provide internships", "can pnc students do internships"),
    ),
    KnowledgeItem(
        topic="internship_duration",
        answer=(
            "The official Cambodia page says the internship is a 16-week full-time internship at the end of "
            "the program, from August to November."
        ),
        keywords=("16 week internship", "internship duration", "august to november", "full time internship"),
        patterns=("how long is the pnc internship", "when do pnc students do internship"),
    ),
    KnowledgeItem(
        topic="student_path",
        answer=(
            "The official PN mission page describes the student path in Cambodia as: selection and orientation, "
            "2 years of training in the center, internship, employment guidance, and then a sustainable digital career."
        ),
        keywords=("student path", "journey", "learning path", "stages", "steps in program"),
        patterns=("what is the student path at pnc", "how does the pnc program work"),
    ),
    KnowledgeItem(
        topic="alumni",
        answer=(
            "PNC alumni are an important part of the community. Graduates can support current students, "
            "share experiences, and strengthen the connection between PNC and employers."
        ),
        keywords=("alumni", "graduates", "former students", "old students"),
        patterns=("does pnc have alumni", "how do alumni support pnc"),
    ),
    KnowledgeItem(
        topic="outcomes",
        answer=(
            "According to the official Cambodia page, PNC has helped transform the lives of nearly 6,000 people "
            "(students and their families) through IT education."
        ),
        keywords=("outcome", "outcomes", "result", "results", "impact"),
    ),
    KnowledgeItem(
        topic="salary_impact",
        answer=(
            "The official Cambodia page says the graduate's average monthly wage is 305 USD, while the average "
            "family income before joining PNC is 50 USD."
        ),
        keywords=("salary", "wage", "income", "average salary", "average wage", "family income"),
        patterns=("what is the average salary of pnc graduates", "how does pnc change family income"),
    ),
    KnowledgeItem(
        topic="graduates",
        answer="According to the official Cambodia page, PNC has produced 1,768 graduates since 2005.",
        keywords=("graduates", "graduate count", "how many graduates", "number of graduates"),
        patterns=("how many graduates does pnc have", "how many students graduated from pnc"),
    ),
    KnowledgeItem(
        topic="employment_rate",
        answer="According to the official Cambodia page, 92% of PNC graduates are employed within 3 months of graduation.",
        keywords=("employment rate", "92%", "employed", "job rate", "graduate employment"),
        patterns=("what is the employment rate of pnc", "how many pnc graduates get jobs"),
    ),
    KnowledgeItem(
        topic="sdg",
        answer=(
            "The official PN site says the organization contributes to 6 Sustainable Development Goals, "
            "including No Poverty, Quality Education, Gender Equality, Reduced Inequalities, Decent Work "
            "and Economic Growth, and Partnerships for the Goals."
        ),
        keywords=("sdg", "sustainable development goals", "goals"),
    ),
    KnowledgeItem(
        topic="selection",
        answer=(
            "PN describes its student selection as fair and rigorous. The official site says the selection team "
            "runs a 4-step process and works with local partners, high schools, community organizations, and NGOs."
        ),
        keywords=("select", "selection", "admission", "admissions", "apply", "application", "choose"),
        patterns=("how are students selected", "how can i apply to pnc"),
    ),
    KnowledgeItem(
        topic="selection_timeline",
        answer=(
            "The official Cambodia page says the selection process runs every year from February to November. "
            "It begins with information sessions from February to April, followed by written tests from June to July."
        ),
        keywords=("selection timeline", "admission timeline", "february to november", "written tests"),
        patterns=("when does pnc selection happen", "what is the pnc selection timeline"),
    ),
    KnowledgeItem(
        topic="eligibility",
        answer=(
            "PNC mainly targets disadvantaged youth with motivation and potential. Admission is not only about "
            "academic results, but also social background, commitment, and the ability to benefit from the program."
        ),
        keywords=("eligible", "eligibility", "requirements", "requirement", "qualify", "qualification"),
        patterns=("who can apply to pnc", "what are the requirements for pnc"),
    ),
    KnowledgeItem(
        topic="admission_capacity",
        answer=(
            "The official PN mission page says the Cambodia program enrolls about 75 students each year. "
            "The official Cambodia center page also says around 150 students are trained at the Phnom Penh center."
        ),
        keywords=("admit", "admission capacity", "intake", "cohort size", "75", "100"),
        patterns=("how many students are admitted to pnc each year", "what is pnc intake"),
    ),
    KnowledgeItem(
        topic="target_students",
        answer=(
            "PNC serves underserved or disadvantaged Cambodian youth, especially those facing socio-economic "
            "barriers to higher education and career opportunities."
        ),
        keywords=("who does pnc serve", "serve", "students", "target", "beneficiaries"),
    ),
    KnowledgeItem(
        topic="gender",
        answer=(
            "According to the official Cambodia page, 52% of PNC's current students are young women. The selection "
            "process also aims for at least 50% female students in each new cohort."
        ),
        keywords=("gender", "female", "girls", "women", "equality", "female enrollment"),
        patterns=("does pnc support female students", "what about gender equality at pnc"),
    ),
    KnowledgeItem(
        topic="rural_background",
        answer=(
            "The official Cambodia page highlights that Cambodia has a large rural population, and the selection "
            "team works across the country with local partners to reach disadvantaged youth, including in remote areas."
        ),
        keywords=("rural", "remote areas", "countryside", "provinces"),
        patterns=("does pnc help students from rural areas", "does pnc recruit in remote provinces"),
    ),
    KnowledgeItem(
        topic="location",
        answer=OFFICIAL_CONTACT,
        keywords=("location", "address", "contact", "phone", "email", "where"),
        patterns=("where is pnc located", "how can i contact pnc"),
    ),
    KnowledgeItem(
        topic="country_director",
        answer="According to the official PNC Cambodia page, the Country Director is Hybunna HANG.",
        keywords=("country director", "director", "leader", "head of pnc", "who runs pnc"),
        patterns=("who is the country director of pnc", "who is the director of pnc"),
    ),
    KnowledgeItem(
        topic="team_contacts",
        answer=(
            "The official PNC Cambodia page lists these key contacts: Hybunna HANG, Country Director; "
            "Sreynich LENG, External Relations Manager; Thaina SEANG, Selection Project Manager; "
            "Sim HUL, Education Manager; Lihuy HOK, Training Manager; and Sreysros SOK, Admin & Finance Manager."
        ),
        keywords=("team", "contacts", "managers", "management", "staff roles"),
        patterns=("who is on the pnc team", "who are the key contacts at pnc"),
    ),
    KnowledgeItem(
        topic="donation",
        answer=(
            "You can support PNC by donating, volunteering, or becoming a partner. "
            "The official PN website also has a 'Get Involved' section for donations and volunteering."
        ),
        keywords=("donate", "donation", "volunteer", "support pnc", "help pnc", "partner"),
        patterns=("how can i support pnc", "how can i help pnc"),
    ),
    KnowledgeItem(
        topic="partners",
        answer=(
            "The official PNC Cambodia page says businesses can partner through internships, graduate recruitment, "
            "laptop donations, financial support, and other forms of collaboration."
        ),
        keywords=("partner", "partners", "company partner", "employer", "collaboration"),
        patterns=("who are pnc partners", "how do partners help pnc"),
    ),
    KnowledgeItem(
        topic="partner_contact",
        answer=(
            "For partnership questions, the official PNC Cambodia page says to contact "
            "Sreynich LENG, External Relations Manager, at sreynich.leng@passerellesnumeriques.org."
        ),
        keywords=("partner contact", "external relations", "business contact", "company contact"),
        patterns=("who should i contact for partnership with pnc", "how can a company partner with pnc"),
    ),
    KnowledgeItem(
        topic="jobs_volunteering",
        answer=(
            "The official PNC Cambodia page says PNC offers employment and volunteer opportunities. "
            "For a spontaneous application, candidates can send an updated CV and cover letter to "
            "info.cambodia@passerellesnumeriques.org."
        ),
        keywords=("job opening", "jobs at pnc", "work at pnc", "volunteer", "employment opportunities"),
        patterns=("how can i work at pnc", "does pnc have volunteer opportunities"),
    ),
    KnowledgeItem(
        topic="career_forum",
        answer="The official PNC history says the first PNC Career Forum was launched in 2014.",
        keywords=("career forum", "job fair", "employment event"),
        patterns=("does pnc have a career forum", "when did pnc start the career forum"),
    ),
    KnowledgeItem(
        topic="ngo_status",
        answer=(
            "PNC is part of Passerelles Numeriques, a non-profit NGO focused on education and social impact "
            "for disadvantaged youth."
        ),
        keywords=("ngo", "non profit", "nonprofit", "organization type", "charity"),
        patterns=("is pnc an ngo", "is pnc a non profit"),
    ),
    KnowledgeItem(
        topic="governance",
        answer=(
            "According to the official FAQ, PN is registered as a non-profit association in France with a board "
            "governing PN Global, and in each country where it works, PN is registered as an international NGO."
        ),
        keywords=("governance", "governed", "board", "registration", "registered"),
        patterns=("how is pnc governed", "how is passerelles numeriques governed"),
    ),
    KnowledgeItem(
        topic="impact_measurement",
        answer=(
            "According to the official FAQ, PN measures impact using alumni impact surveys, student self-assessment "
            "surveys, company internship surveys, and by comparing family resources before and after graduation."
        ),
        keywords=("measure impact", "impact measurement", "survey", "assessment", "how measure success"),
        patterns=("how does pnc measure impact", "how does passerelles numeriques measure its impact"),
    ),
    KnowledgeItem(
        topic="student_count",
        answer=(
            "The official Cambodia page says around 150 students are trained each year at the Phnom Penh center. "
            "I do not want to claim an exact current student count unless PNC publishes a newer number."
        ),
        keywords=("student count", "number of students", "students", "how many students"),
        patterns=("how many students at pnc", "number of students in pnc"),
    ),
    KnowledgeItem(
        topic="recognition",
        answer="The official Cambodia page says PNC's program is recognized by the Cambodian Ministry of Education.",
        keywords=("recognized", "recognition", "ministry", "ministry of education", "official recognition"),
        patterns=("is pnc recognized", "is pnc recognized by the ministry of education"),
    ),
    KnowledgeItem(
        topic="it_sector",
        answer="According to the official Cambodia page, 98% of PNC graduates work in the IT sector.",
        keywords=("it sector", "work in it", "graduates work in it", "98%"),
        patterns=("how many pnc graduates work in it", "do pnc graduates work in the it sector"),
    ),
    KnowledgeItem(
        topic="nomadlab",
        answer=(
            "The official Cambodia page presents NomadLab as a modular, open-source, inclusive, and easy-to-build "
            "ICT infrastructure and educational tool designed to help bridge the digital divide in rural and "
            "disadvantaged communities."
        ),
        keywords=("nomadlab", "digital divide", "ict infrastructure", "rural digital project"),
        patterns=("what is nomadlab", "does pnc have a project for rural digital access"),
    ),
    KnowledgeItem(
        topic="history_milestones",
        answer=(
            "Official PNC milestones include: 2005 first program in Phnom Penh with 25 students in SNA, "
            "2009 launch of Web Programming, 2011 first time 100 new students were enrolled, 2020 support from "
            "Cambodia's Skills Development Fund and ADB, and 2024 the BRIDGES Project partnership."
        ),
        keywords=("milestones", "through the years", "timeline", "history milestones"),
        patterns=("what are important milestones of pnc", "tell me pnc milestones"),
    ),
)

STOP_WORDS = {
    "a", "an", "and", "are", "at", "can", "do", "does", "for", "how", "i", "in", "is",
    "me", "of", "on", "please", "tell", "the", "to", "what", "when", "where", "who",
    "why", "with", "about", "you", "your",
}

RELATED_TOPICS = (
    "mission",
    "programs",
    "student support",
    "location",
    "values",
    "admission",
    "history",
    "internships",
    "graduates",
    "team",
    "jobs",
)

TOPIC_LOOKUP = {item.topic: item for item in KNOWLEDGE_BASE}

PHRASE_ALIASES = {
    "passerelles numeriques cambodia": "pnc",
    "passerelles numeriques": "pnc",
    "pn cambodia": "pnc",
    "scholar ship": "scholarship",
    "financial help": "financial support",
    "money support": "financial support",
    "study for free": "free program",
    "apply scholarship": "apply for scholarship",
    "join pnc": "apply to pnc",
    "register at pnc": "apply to pnc",
    "enroll at pnc": "apply to pnc",
    "major subject": "major",
    "subjects": "curriculum",
    "lessons": "curriculum",
    "dorm": "dormitory",
    "hostel": "accommodation",
    "food support": "meals allowance",
    "health care": "healthcare",
    "job support": "employment support",
    "find a job": "employment",
    "get a job": "employment",
    "girls": "female students",
    "women students": "female students",
    "rural students": "rural areas",
    "remote province": "remote areas",
}

TOPIC_HINTS = {
    "scholarship": ("scholarship", "financial", "aid", "bursary"),
    "selection": ("apply", "application", "selection", "admission", "register"),
    "cost": ("free", "fee", "fees", "cost", "tuition", "pay", "payment"),
    "curriculum": ("curriculum", "subjects", "learn", "study", "modules", "skills"),
    "housing": ("accommodation", "dormitory", "dorm", "housing", "live"),
    "food_allowance": ("food", "meal", "meals", "allowance"),
    "health_support": ("health", "medical", "healthcare", "hospital"),
    "internship_duration": ("internship", "duration", "when", "august", "november", "16"),
    "country_director": ("director", "country director", "leader", "head"),
    "partner_contact": ("partner", "company", "business", "contact", "email"),
    "jobs_volunteering": ("job", "jobs", "work", "career", "volunteer"),
    "recognition": ("recognized", "recognition", "ministry"),
}

