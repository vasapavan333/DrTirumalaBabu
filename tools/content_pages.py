"""Content for the condition pages, the conditions index and the therapies page.

This is the source of truth for those pages — `python tools/build_pages.py`
regenerates the HTML from it. The other pages (index, about, services, contact,
privacy) stay hand-edited; only the condition pages are generated, because
there are 22 of them sharing one structure.

Register rules, which the audit enforces and which the copy must keep:
  - never guarantee an outcome or a cure
  - never let a reader self-diagnose from a symptom list
  - never name a medicine or a dose
  - screening questionnaires are aids to assessment, never diagnostic tests
  - say plainly when something needs urgent care

Nothing here has been reviewed by Dr. Tirumala Babu. See TODO-CONTENT.md §11.
"""

DOCTOR = "Dr. Manchikalapudi Tirumala Babu"
DISPLAY_TITLE = "Neuropsychiatric Consultant"
CLINIC = "Maruthi Hospital and Diagnostics"
CITY = "Guntur"

# --------------------------------------------------------------------------
# Categories, in the order they appear on conditions.html
# --------------------------------------------------------------------------

CATEGORIES = [
    (
        "mental-health",
        "Mental Health Conditions",
        "Concerns affecting mood, worry, thinking and behaviour.",
    ),
    (
        "neuro-cognitive",
        "Neurological &amp; Cognitive Conditions",
        "Concerns involving attention, development, memory, headache and sleep.",
    ),
    (
        "de-addiction",
        "De-addiction &amp; Substance-Related Concerns",
        "Support for alcohol, tobacco, substance use and problematic screen use.",
    ),
    (
        "psychosomatic",
        "Sexual &amp; Psychosomatic Health",
        "Concerns where emotional and physical health are closely linked.",
    ),
]

# --------------------------------------------------------------------------
# The 22 conditions. `page` is the slug when a full page exists; None means the
# card renders without a "Learn more" link, so the audit never sees a dead one.
# --------------------------------------------------------------------------

CONDITIONS = [
    # --- mental health -----------------------------------------------------
    dict(name="Stress", cat="mental-health", icon="i-leaf",
         card="Ongoing pressure that starts to affect sleep, mood, concentration or physical health.",
         page=None),
    dict(name="Depression", cat="mental-health", icon="i-cloud",
         card="Persistent low mood, loss of interest and fatigue lasting two weeks or more.",
         page="depression-treatment-guntur", short="depression"),
    dict(name="Anxiety Disorders", cat="mental-health", icon="i-activity",
         card="Worry or fear that is hard to control and interferes with everyday life.",
         page="anxiety-treatment-guntur", short="anxiety"),
    dict(name="Panic Disorder", cat="mental-health", icon="i-alert",
         card="Sudden episodes of intense fear with strong physical symptoms.",
         page=None),
    dict(name="Phobias", cat="mental-health", icon="i-shield",
         card="Strong, persistent fear of a specific object, place or situation.",
         page=None),
    dict(name="Obsessive-Compulsive Disorder (OCD)",
         cat="mental-health", icon="i-loop",
         card="Intrusive thoughts and repetitive behaviours that take up time and cause distress.",
         page=None),
    dict(name="Bipolar Disorder", cat="mental-health", icon="i-repeat",
         card="Episodes of markedly elevated and lowered mood, energy and activity.",
         page=None),
    dict(name="Schizophrenia", cat="mental-health", icon="i-compass",
         card="A condition affecting thinking, perception and behaviour, with treatment and follow-up.",
         page=None),
    dict(name="Psychosis", cat="mental-health", icon="i-compass",
         card="Loss of contact with reality, which may include hearing voices or fixed false beliefs.",
         page=None),
    dict(name="Anger Management Concerns", cat="mental-health", icon="i-flame",
         card="Difficulty managing anger in a way that affects relationships, work or safety.",
         page=None),
    dict(name="Mental Wellbeing", cat="mental-health", icon="i-heart",
         card="Preventive support, coping skills and early advice before difficulties become entrenched.",
         page=None),

    # --- neurological & cognitive -----------------------------------------
    dict(name="Migraine", cat="neuro-cognitive", icon="i-activity",
         card="Recurrent headache, often with nausea and sensitivity to light or sound.",
         page=None),
    dict(name="Autism Spectrum Disorder", cat="neuro-cognitive", icon="i-child",
         card="A developmental condition affecting communication, social interaction and behaviour.",
         page=None),
    dict(name="ADHD", cat="neuro-cognitive", icon="i-child",
         card="Difficulty with attention, activity level and impulse control, in children or adults.",
         page=None),
    dict(name="Dementia", cat="neuro-cognitive", icon="i-file",
         card="Progressive difficulty with memory, thinking and daily tasks, usually in later life.",
         page=None),
    dict(name="Sleep Disorders", cat="neuro-cognitive", icon="i-moon",
         card="Difficulty falling asleep, staying asleep or feeling rested, and its effect on mood.",
         page=None),

    # --- de-addiction ------------------------------------------------------
    dict(name="Alcohol Use Disorder", cat="de-addiction", icon="i-ban",
         card="When drinking becomes hard to control and continues despite harm.",
         page="alcohol-de-addiction-guntur", short="alcohol use"),
    dict(name="Tobacco Dependence", cat="de-addiction", icon="i-ban",
         card="Difficulty stopping smoking or chewing tobacco despite wanting to quit.",
         page=None),
    dict(name="Problematic Smartphone Use", cat="de-addiction", icon="i-ban",
         card="Screen or phone use that displaces sleep, study, work or relationships.",
         page=None),
    dict(name="Other Substance Use Disorders", cat="de-addiction", icon="i-ban",
         card="Assessment and treatment support for other substances, where clinically relevant.",
         page=None),

    # --- sexual & psychosomatic -------------------------------------------
    dict(name="Sexual Health Concerns", cat="psychosomatic", icon="i-users",
         card="Confidential assessment of sexual difficulties, including their emotional contributors.",
         page=None),
    dict(name="Somatic Symptom Disorder", cat="psychosomatic", icon="i-stetho",
         card="Distressing physical symptoms where investigations do not fully explain the picture.",
         page=None),
]

# --------------------------------------------------------------------------
# Non-pharmacological therapies.
# `offered` marks the three printed on the clinic's own poster. Everything else
# is described as something that may be recommended or referred — see the
# brief's rule about not claiming availability without confirmation.
# --------------------------------------------------------------------------

THERAPIES = [
    dict(key="cbt", name="Cognitive Behavioural Therapy (CBT)", icon="i-loop", offered=True,
         what="A structured, practical talking therapy that looks at the link between thoughts, "
              "feelings and behaviour, and at the patterns that keep a difficulty going.",
         helps="Sessions focus on noticing unhelpful thinking habits, testing them against "
               "evidence, and building alternative responses. It is usually time-limited, with "
               "work to practise between sessions.",
         used=["Depression", "Anxiety disorders", "Panic disorder", "Phobias", "OCD",
               "Insomnia and sleep difficulties"]),
    dict(key="family", name="Family Therapy", icon="i-users", offered=True,
         what="Sessions involving family members alongside the patient, looking at how a "
              "difficulty affects the household and how the household can support recovery.",
         helps="Family members learn what the condition is and is not, how to respond during "
               "difficult periods, and how to look after their own wellbeing while caring.",
         used=["Schizophrenia and psychosis", "Bipolar disorder", "Substance use disorders",
               "Child and adolescent concerns"]),
    dict(key="couple", name="Couple Therapy", icon="i-heart", offered=True,
         what="Joint sessions for partners where relationship difficulties are part of the "
              "picture, or where a mental health condition is affecting the relationship.",
         helps="Work focuses on communication, shared understanding of the condition, and "
               "practical agreements that reduce conflict.",
         used=["Relationship difficulties", "Sexual health concerns", "Depression and anxiety "
               "affecting a relationship"]),
    dict(key="psychoeducation", name="Psychoeducation", icon="i-file", offered=False,
         what="Structured explanation of the condition, its course, the treatment options and "
              "the early warning signs, given to the patient and usually to family too.",
         helps="Understanding what is happening tends to reduce fear, improve participation in "
               "treatment and make relapse easier to catch early.",
         used=["Almost every condition, as part of the consultation"]),
    dict(key="behavioural", name="Behavioural Therapy", icon="i-activity", offered=False,
         what="Approaches that change what a person does rather than working first on thoughts "
              "— for example gradually re-engaging with avoided activities or situations.",
         helps="Useful where avoidance, inactivity or a specific habit is maintaining the "
               "problem.",
         used=["Depression", "Phobias", "OCD", "Habit-related difficulties"]),
    dict(key="supportive", name="Supportive Psychotherapy", icon="i-chat", offered=False,
         what="Regular sessions focused on emotional support, problem-solving and maintaining "
              "day-to-day functioning, rather than on a specific technique.",
         helps="Often appropriate during a difficult period, while a person is stabilising, or "
               "alongside other treatment.",
         used=["Adjustment difficulties", "Chronic conditions", "Periods of high stress"]),
    dict(key="motivational", name="Motivational Interviewing", icon="i-repeat", offered=False,
         what="A conversational approach that helps a person explore their own reasons for "
              "change, rather than being told what to do.",
         helps="Particularly suited to situations where someone feels two ways about changing a "
               "behaviour.",
         used=["Alcohol and tobacco dependence", "Other substance use", "Lifestyle change"]),
    dict(key="stress", name="Stress Management", icon="i-leaf", offered=False,
         what="Practical training in relaxation, breathing, routine and workload strategies.",
         helps="Reduces the physical arousal that accompanies stress and builds a more "
               "sustainable daily structure.",
         used=["Stress-related difficulties", "Anxiety", "Somatic symptoms"]),
    dict(key="sleep", name="Sleep Hygiene &amp; Behavioural Sleep Interventions", icon="i-moon",
         offered=False,
         what="Changes to sleep timing, environment and pre-sleep habits, and behavioural "
              "methods for persistent insomnia.",
         helps="Often tried before considering any medication for sleep, and used alongside "
               "treatment of an underlying condition.",
         used=["Insomnia", "Sleep difficulties in depression and anxiety"]),
    dict(key="social", name="Social Skills Training", icon="i-users", offered=False,
         what="Structured practice of conversation, everyday interaction and self-care skills.",
         helps="Supports a return to study, work and social life where a condition has affected "
               "confidence or day-to-day functioning.",
         used=["Schizophrenia", "Autism spectrum disorder", "Social anxiety"]),
    dict(key="relapse", name="Relapse Prevention &amp; Recovery Support", icon="i-shield",
         offered=False,
         what="Identifying personal triggers and early warning signs, and agreeing a plan for "
              "what to do when they appear.",
         helps="Usually involves family, and is planned once the acute phase has settled.",
         used=["Substance use disorders", "Bipolar disorder", "Recurrent depression",
               "Schizophrenia"]),
]

# `short` is the wording used in a card's "Read about ..." link, so the link
# text stays one line. Conditions without one fall back to their full name.
for _c in CONDITIONS:
    _c.setdefault("short", _c["name"].split(" (")[0].lower())

THERAPY_BY_KEY = {t["key"]: t for t in THERAPIES}

# --------------------------------------------------------------------------
# The site-wide FAQs. These were already written and already sat in the
# FAQPage JSON-LD of four pages — but the visible copy had been lost during
# the multi-page restructure, and the surrounding JSON had been spliced badly
# enough that the whole graph stopped parsing. They now live here, render
# visibly on contact.html, and feed that page's schema from the same source.
# --------------------------------------------------------------------------

GENERAL_FAQS = [
    (
        "Are psychiatric consultations confidential?",
        "Consultations are treated as confidential medical information, in line "
        "with professional practice and applicable law. If you have questions "
        "about what is recorded or shared, you are welcome to ask during the "
        "consultation.",
    ),
    (
        "Does every mental health condition require medication?",
        "No. Treatment depends on the clinical assessment. Some concerns are "
        "managed with counselling, lifestyle and follow-up alone; others are "
        "helped by medication, sometimes alongside therapy. The options, and the "
        "reasons behind them, are discussed with you before anything is started.",
    ),
    (
        "Can family members accompany the patient?",
        "Yes. Family members are welcome, and their observations are often "
        "useful during an assessment. Part of the consultation may still be "
        "conducted with the patient alone, which is normal clinical practice.",
    ),
    (
        "How can I book an appointment?",
        "Call the clinic on +91 89850 14488, message the same number on "
        "WhatsApp, or send an appointment enquiry through the form on this "
        "website. The clinic will confirm a time with you.",
    ),
    (
        "Where is the clinic located?",
        "Maruthi Hospital and Diagnostics, 126-151, Ground Floor, Opp. 10th Lane "
        "of Sriram Nagar, M.G. Inner Ring Road, Phase-II, Main Road, Gorantla, "
        "Guntur 522034, Andhra Pradesh. It is directly opposite Ushodaya Super "
        "Market.",
    ),
]

# --------------------------------------------------------------------------
# One page per condition. The slug is the URL and the SEO phrase, so it is
# written the way someone would search rather than the way a textbook would
# name the condition ("ocd-treatment-guntur", not
# "obsessive-compulsive-disorder-treatment-guntur").
#
# A slug here does not by itself create a page: tools/build_pages.py only
# builds and links a condition that also has copy, in content_detail.py (the
# long ten-section form) or content_short.py (the five-section form).
# --------------------------------------------------------------------------

SLUGS = {
    "Stress": ("stress-management-guntur", "stress"),
    "Panic Disorder": ("panic-disorder-treatment-guntur", "panic attacks"),
    "Phobias": ("phobia-treatment-guntur", "phobias"),
    "Obsessive-Compulsive Disorder (OCD)": ("ocd-treatment-guntur", "OCD"),
    "Bipolar Disorder": ("bipolar-disorder-treatment-guntur", "bipolar disorder"),
    "Schizophrenia": ("schizophrenia-treatment-guntur", "schizophrenia"),
    "Psychosis": ("psychosis-treatment-guntur", "psychosis"),
    "Anger Management Concerns": ("anger-management-guntur", "anger"),
    "Mental Wellbeing": ("mental-wellbeing-guntur", "mental wellbeing"),
    "Migraine": ("migraine-treatment-guntur", "migraine"),
    "Autism Spectrum Disorder": ("autism-assessment-guntur", "autism"),
    "ADHD": ("adhd-treatment-guntur", "ADHD"),
    "Dementia": ("dementia-care-guntur", "dementia"),
    "Sleep Disorders": ("sleep-disorder-treatment-guntur", "sleep problems"),
    "Tobacco Dependence": ("tobacco-de-addiction-guntur", "quitting tobacco"),
    "Problematic Smartphone Use": ("smartphone-addiction-help-guntur", "screen use"),
    "Other Substance Use Disorders": ("substance-use-treatment-guntur", "substance use"),
    "Sexual Health Concerns": ("sexual-health-consultation-guntur", "sexual health"),
    "Somatic Symptom Disorder": ("somatic-symptom-treatment-guntur", "somatic symptoms"),
}

for _c in CONDITIONS:
    if not _c.get("page") and _c["name"] in SLUGS:
        _c["page"], _c["short"] = SLUGS[_c["name"]]

# --------------------------------------------------------------------------
# The ten services, in the order they appear on services.html.
#
# `page` is a page of its own; `link` points at a condition page instead.
# Seven of the ten restate a condition the site already covers in depth —
# "Depression Care" and "Depression" would be two pages saying the same thing
# in the same words to the same search, and Google splits the ranking between
# them rather than adding it up. So those link across, and only the three that
# are genuinely a service rather than a condition get their own page.
# --------------------------------------------------------------------------

SERVICES = [
    dict(name="Psychiatric Consultation", icon="i-stetho",
         card="A structured assessment of your symptoms, history and daily functioning, "
              "and a discussion of what the findings suggest.",
         page="psychiatric-consultation-guntur", link=None),
    dict(name="Counselling and Support", icon="i-chat",
         card="Supportive conversations and guidance where clinically appropriate, "
              "including CBT-informed, family and couple counselling.",
         page="counselling-guntur", link=None),
    dict(name="Stress and Anxiety Management", icon="i-leaf",
         card="Professional evaluation and individualised care for persistent stress, "
              "worry, panic and phobia-related concerns.",
         page=None, link="anxiety-treatment-guntur"),
    dict(name="Depression Care", icon="i-cloud",
         card="Assessment and treatment planning for low mood, loss of interest, "
              "fatigue and related depressive symptoms.",
         page=None, link="depression-treatment-guntur"),
    dict(name="OCD Care", icon="i-loop",
         card="Psychiatric assessment and evidence-informed treatment for intrusive "
              "thoughts and repetitive behaviours.",
         page=None, link="ocd-treatment-guntur"),
    dict(name="Bipolar Disorder Care", icon="i-activity",
         card="Evaluation and ongoing management of mood swings and episodic changes in "
              "energy and behaviour, when clinically indicated.",
         page=None, link="bipolar-disorder-treatment-guntur"),
    dict(name="Schizophrenia Care", icon="i-compass",
         card="Assessment and treatment for psychotic symptoms and related concerns, "
              "with follow-up and family guidance.",
         page=None, link="schizophrenia-treatment-guntur"),
    dict(name="Sleep Disorder Care", icon="i-moon",
         card="Evaluation of sleep-related concerns and the mental health symptoms that "
              "often accompany them.",
         page=None, link="sleep-disorder-treatment-guntur"),
    dict(name="De-addiction Support", icon="i-ban",
         card="Assessment and treatment support for alcohol, tobacco and other substance "
              "use disorders, with follow-up care.",
         page="de-addiction-services-guntur", link=None),
    dict(name="Anger Management", icon="i-flame",
         card="Professional guidance for difficulty managing anger and related emotional "
              "difficulties.",
         page=None, link="anger-management-guntur"),
]

# --------------------------------------------------------------------------
# Therapy page slugs. Same rule: a slug is not a page until content_therapy.py
# has copy for it.
# --------------------------------------------------------------------------

THERAPY_SLUGS = {
    "cbt": "cbt-therapy-guntur",
    "family": "family-therapy-guntur",
    "couple": "couple-therapy-guntur",
    "psychoeducation": "psychoeducation-guntur",
    "behavioural": "behavioural-therapy-guntur",
    "supportive": "supportive-psychotherapy-guntur",
    "motivational": "motivational-interviewing-guntur",
    "stress": "stress-management-therapy-guntur",
    "sleep": "sleep-therapy-guntur",
    "social": "social-skills-training-guntur",
    "relapse": "relapse-prevention-guntur",
}

# Two therapy names are too long to sit in a dropdown column without pushing
# into the next one. `menu` is the label used in the navigation only; the
# pages and the therapies index keep the full name.
THERAPY_MENU_LABEL = {
    "sleep": "Sleep &amp; Insomnia Therapy",
    "relapse": "Relapse Prevention",
    "cbt": "Cognitive Behavioural Therapy",
}

for _t in THERAPIES:
    _t["page"] = THERAPY_SLUGS.get(_t["key"])
    _t["menu"] = THERAPY_MENU_LABEL.get(_t["key"], _t["name"].split(" (")[0])


# --------------------------------------------------------------------------
# Social. The share-sheet link Instagram hands you carries utm_source and an
# stkn token tied to the account that copied it; neither belongs in a page
# served to the public, so this is the plain profile URL.
# --------------------------------------------------------------------------

INSTAGRAM_URL = "https://www.instagram.com/dr_healing_minds/"
INSTAGRAM_LABEL = "Follow us on Instagram"
INSTAGRAM_HANDLE = "@dr_healing_minds"
