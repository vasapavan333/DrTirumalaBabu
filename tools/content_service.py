"""Pages for the three services that are a service rather than a condition.

Seven of the ten services on services.html restate a condition the site
already covers in depth — "Depression Care" and "Depression" would be two
pages saying the same thing to the same search, which splits the ranking
rather than adding to it. Those link across to the condition page; the
mapping lives in SERVICES in content_pages.py.

These three do not restate a condition, so they get pages of their own:

    psychiatric-consultation-guntur   what actually happens in a consultation
    counselling-guntur                what counselling here involves
    de-addiction-services-guntur      de-addiction across all substances

The same register rules apply: no outcome promises, no medicine names, no
claim that a therapy is available unless it is confirmed.

Nothing here has been reviewed by Dr. Tirumala Babu. See TODO-CONTENT.md §11.
"""

SERVICE_DETAIL: dict[str, dict] = {}

SERVICE_DETAIL["psychiatric-consultation-guntur"] = dict(
    name="Psychiatric Consultation",
    title="Psychiatric Consultation in Guntur | Dr. Tirumala Babu",
    meta="What happens in a psychiatric consultation in Guntur — how long it "
         "takes, what you will be asked, whether family can attend, and what "
         "you leave with.",
    keyword="psychiatric consultation in Guntur",
    intro="Most people arriving for a first psychiatric consultation have no "
          "idea what to expect, and a fair number are apprehensive about it. "
          "This page sets out what actually happens, because knowing tends to "
          "make the appointment easier.",
    sections=[
        ("What the consultation is",
         [
             "A psychiatric consultation is a structured medical assessment. "
             "It looks at the symptoms you have noticed, how long they have "
             "been present, what was happening when they started, how they "
             "affect your day, your medical and medication history, your "
             "sleep, and your use of alcohol or other substances.",
             "It is a conversation rather than a test, and there is no right "
             "answer to give. The more accurate the account, the more useful "
             "the assessment — including the parts that are uncomfortable to "
             "say out loud.",
         ]),
        ("What you will be asked",
         [
             "What brought you in, and when it started",
             "How your sleep, appetite, energy and concentration are",
             "What a typical day looks like now compared with before",
             "Your medical history and any medicines you take",
             "Alcohol, tobacco and any other substance use",
             "Whether anyone in the family has had similar difficulties",
             "What you have already tried, and what happened",
         ]),
        ("What happens afterwards",
         [
             "The findings are discussed with you — what the assessment "
             "suggests, what it does not, and what the options are. Where "
             "blood tests or a physical opinion are needed before anything is "
             "concluded, that is arranged.",
             "A plan is agreed rather than issued. Where medication is one of "
             "the options, the reasoning, what it is expected to do and what "
             "to report back are explained before anything is started. Where "
             "it is not needed, that is said plainly.",
             "A review is usually arranged. Psychiatric treatment depends on "
             "follow-up more than most branches of medicine, because the "
             "response to treatment is itself part of the information.",
         ]),
    ],
    faqs=[
        ("How long does a first consultation take?",
         "Longer than a routine medical appointment, because the history "
         "matters. The clinic will tell you what to expect when you book."),
        ("Can a family member come with me?",
         "Yes, and their observations are often useful. Part of the "
         "consultation may still be conducted with you alone, which is normal "
         "clinical practice."),
        ("Will I be given medication on the first visit?",
         "Not automatically. It depends entirely on what the assessment finds, "
         "and it is discussed with you first. Many consultations end with "
         "advice and a review instead."),
        ("Is it confidential?",
         "Consultations are treated as confidential medical information, in "
         "line with professional practice and applicable law. You are welcome "
         "to ask what is recorded and what is shared."),
        ("What should I bring?",
         "Any previous prescriptions, discharge summaries or test results, and "
         "a list of everything you currently take — including anything bought "
         "without a prescription."),
    ],
)

SERVICE_DETAIL["counselling-guntur"] = dict(
    name="Counselling and Support",
    title="Counselling in Guntur | Dr. M. Tirumala Babu",
    meta="Counselling at Maruthi Hospital, Guntur — CBT-informed, family and "
         "couple counselling alongside psychiatric care, and how it is decided "
         "what suits you.",
    keyword="counselling in Guntur",
    intro="Counselling here is provided alongside psychiatric assessment "
          "rather than separately from it. Which approach suits you is a "
          "clinical decision that follows the assessment — it is not a menu "
          "choice, and it is not the same answer for everyone.",
    sections=[
        ("What is available",
         [
             "Cognitive behavioural therapy (CBT), a structured, practical "
             "approach used for depression, anxiety, panic, phobias, OCD and "
             "insomnia.",
             "Family counselling, where a condition affects the household and "
             "the household affects the condition — used particularly in "
             "schizophrenia, bipolar disorder, substance use and adolescent "
             "concerns.",
             "Couple counselling, where relationship difficulties are part of "
             "the picture or a condition has begun to strain the "
             "relationship.",
             "Supportive work and psychoeducation as part of ongoing care, and "
             "referral onward where a different approach is indicated.",
         ]),
        ("How it fits with medication",
         [
             "Sometimes counselling is the main treatment. Sometimes "
             "medication is what makes counselling possible. Often the two "
             "run together, and for some conditions the evidence favours the "
             "combination over either alone.",
             "What this page will not tell you is that talking therapy "
             "replaces medication in every situation, because that is not "
             "true and acting on it can be harmful. The question is answered "
             "by the assessment, condition by condition and person by "
             "person.",
         ]),
        ("What to expect",
         [
             "Counselling is not advice-giving, and it is not being told what "
             "to do. Most approaches involve identifying a pattern, testing it "
             "and practising something different between sessions.",
             "It asks something of you. The work between sessions is where "
             "most of the change happens, and approaches that require it do "
             "considerably less without it.",
             "Progress is reviewed. Sessions that continue indefinitely "
             "without review are a recognised way for therapy to drift, which "
             "is why review is built in.",
         ]),
    ],
    faqs=[
        ("How do I know which type of counselling I need?",
         "You do not need to know in advance — that is what the assessment "
         "is for. It depends on the condition, its severity and your "
         "circumstances."),
        ("Is counselling confidential?",
         "Sessions are treated as confidential medical information, in line "
         "with professional practice and applicable law."),
        ("How many sessions will it take?",
         "Structured therapies such as CBT are usually time-limited and "
         "reviewed as they go. Nobody can give a number before an assessment, "
         "and a fixed course quoted in advance is worth questioning."),
        ("Can counselling replace my medication?",
         "Sometimes, and sometimes not — it depends on the condition and the "
         "assessment. What should not happen is stopping medication on your "
         "own because a website suggested therapy would do instead."),
    ],
)

SERVICE_DETAIL["de-addiction-services-guntur"] = dict(
    name="De-addiction Support",
    title="De-addiction Treatment in Guntur | Dr. Tirumala Babu",
    meta="De-addiction support in Guntur for alcohol, tobacco and other "
         "substances — confidential assessment, safe withdrawal planning, "
         "relapse prevention and family involvement.",
    keyword="de-addiction treatment in Guntur",
    intro="De-addiction care here covers alcohol, tobacco and other "
          "substances, and it starts from a medical assessment rather than a "
          "moral one. An honest account of what is being used is the single "
          "thing that most improves the treatment you get.",
    sections=[
        ("What is covered",
         [
             "Alcohol use disorder — assessment, withdrawal planning, "
             "treatment and relapse prevention.",
             "Tobacco dependence, smoked and chewed, including planned quit "
             "attempts and managing withdrawal.",
             "Other substance use, including cannabis, sedatives and sleeping "
             "tablets, and opioids.",
             "Problematic screen and phone use, where it has displaced sleep, "
             "study, work or relationships.",
             "The mental health conditions that travel with substance use — "
             "depression, anxiety and psychotic symptoms — which are assessed "
             "and treated alongside rather than afterwards.",
         ]),
        ("Withdrawal comes first, and safely",
         [
             "Withdrawal risk differs enormously between substances. Stopping "
             "sedatives abruptly can be dangerous, and abrupt cessation after "
             "heavy, sustained drinking can cause seizures or delirium. This "
             "is the reason to ask for advice before stopping rather than "
             "afterwards.",
             "Where withdrawal needs medical supervision, or where inpatient "
             "care is the safer setting, the consultation will say so plainly "
             "and help arrange it.",
         ]),
        ("What treatment involves",
         [
             "A confidential assessment of what is used, how much, for how "
             "long, and what happens when it stops.",
             "Treatment of any mental illness alongside — sometimes cause, "
             "sometimes consequence, often both.",
             "Motivational work, which starts from the assumption that feeling "
             "two ways about stopping is normal rather than a sign of not "
             "being ready.",
             "Relapse prevention: personal triggers, early warning signs, and "
             "an agreed plan for what happens when they appear.",
             "Family involvement with the patient's consent, which measurably "
             "improves how well recovery holds.",
         ]),
    ],
    faqs=[
        ("Is the consultation confidential?",
         "Consultations are treated as confidential medical information, in "
         "line with professional practice and applicable law. If you want to "
         "know what is recorded and what is shared, ask at the start."),
        ("Can I stop drinking on my own?",
         "After heavy, sustained drinking, stopping abruptly can cause "
         "seizures or delirium and is genuinely dangerous. Ask for advice "
         "before you stop, not after symptoms begin."),
        ("Will my family be told?",
         "Not without your agreement. Family involvement is encouraged because "
         "it helps, but it is your decision."),
        ("What if I relapse?",
         "Relapse is common in the course of recovery and is treated as "
         "information about what the plan did not yet cover, not as a reason "
         "to stop treatment or to stay away."),
        ("Do you guarantee I will stay off it?",
         "No, and neither should anyone else. What treatment does is improve "
         "the odds substantially, particularly with follow-up, relapse "
         "planning and family involvement."),
    ],
)
