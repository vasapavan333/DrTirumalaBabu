"""Full page content for the conditions that have a dedicated page.

Every entry follows the same ten-part structure, so `build_pages.py` can render
them all identically. Add a new entry here and set `page=<slug>` on the matching
card in content_pages.py, and the page appears with a working "Learn more" link.

Writing rules for anything added here:
  - plain language first, the clinical term in brackets after
  - symptom lists always carry the "this is not a checklist to diagnose
    yourself with" framing, which the template adds automatically
  - causes are contributors, never "the cause"
  - no medicine names, no doses, no duration promises
  - `urgent` switches on the red-flag callout; set it for anything where
    delay is dangerous
"""

DETAIL = {

# =========================================================================
"depression-treatment-guntur": dict(
    name="Depression",
    category="Mental Health Conditions",
    title="Depression Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Depression treatment in Guntur by Dr. Manchikalapudi Tirumala Babu, "
         "M.D. (Psychiatry). Understand the symptoms, causes, diagnosis and "
         "treatment options, and when to consult.",
    keyword="depression treatment in Guntur",
    secondary=["depression doctor Guntur", "psychiatrist for depression Guntur",
               "low mood treatment Guntur", "depression counselling Guntur"],
    intro="Depression is one of the most common reasons people consult a psychiatrist, "
          "and one of the most treatable. This page explains what it is, what the "
          "symptoms look like, and when it is worth getting an assessment.",
    urgent=True,

    what=[
        "Depression — clinically, major depressive disorder — is a persistent low mood "
        "or loss of interest that lasts at least two weeks and affects how a person "
        "functions day to day. It is not the same as sadness, and it is not a matter "
        "of willpower or character.",
        "Feeling low for a few days after a setback is an ordinary human response, and "
        "it is not depression. What distinguishes depression is how long it lasts, how "
        "much of the day it occupies, and how far it interferes with work, study, "
        "relationships, sleep and self-care.",
    ],

    symptoms=[
        ("Mood and emotions", [
            "Low mood most of the day, most days",
            "Loss of interest or pleasure in things that were previously enjoyed",
            "Hopelessness about the future",
            "Guilt, or a sense of being worthless or a burden",
            "Irritability, which is often the most visible sign in men and in younger people",
        ]),
        ("Physical changes", [
            "Tiredness and low energy that rest does not fix",
            "Sleeping much more or much less than usual, or waking early",
            "Appetite and weight going up or down",
            "Aches, headaches or digestive symptoms without a clear physical cause",
        ]),
        ("Thinking and concentration", [
            "Difficulty concentrating, following conversations or reading",
            "Finding ordinary decisions unusually hard",
            "Memory complaints, particularly in older adults",
        ]),
        ("Behaviour", [
            "Withdrawing from family, friends or social contact",
            "Falling behind at work or in studies",
            "Neglecting self-care or household responsibilities",
            "Drinking more, or using substances to cope",
        ]),
    ],

    causes=[
        ("Biological factors", "Differences in brain chemistry and function, and a family "
         "history of depression or other mental health conditions, both raise "
         "susceptibility. Having a family history does not mean a person will develop "
         "depression."),
        ("Psychological factors", "Long-standing patterns of self-critical thinking, "
         "difficulty with emotion regulation, and earlier adverse experiences can all "
         "contribute."),
        ("Life circumstances and stress", "Bereavement, relationship breakdown, financial "
         "pressure, job loss, examination stress, caring responsibilities and isolation "
         "are frequent triggers."),
        ("Physical health", "Thyroid problems, anaemia, vitamin deficiencies, chronic pain, "
         "and some prescribed medicines can produce or worsen depressive symptoms. This "
         "is part of why an assessment includes physical health."),
        ("Lifestyle factors", "Disrupted sleep, alcohol and substance use, and prolonged "
         "inactivity all interact with mood, often in both directions."),
    ],
    causes_note="Depression rarely has one single cause. Usually several of these "
                "interact, and in many people no clear trigger is ever identified — "
                "which does not make the condition any less real or any less treatable.",

    when=[
        "Low mood or loss of interest has lasted more than two weeks",
        "It is affecting work, study, relationships or the ability to run a household",
        "Sleep or appetite has changed noticeably",
        "You have stopped enjoying things you used to look forward to",
        "Family members have noticed a change before you did",
        "You are using alcohol or other substances to get through the day",
    ],

    diagnosis=[
        ("Clinical interview", "A conversation about what you have been experiencing, how "
         "long it has been going on, and how it affects daily life."),
        ("History", "Previous episodes, physical health, current medicines, alcohol and "
         "substance use, and family history."),
        ("Mental state examination", "A structured observation of mood, thinking, "
         "concentration and risk, carried out during the consultation."),
        ("Screening questionnaires", "Standard rating scales may be used to gauge severity "
         "and to track change over time. They support the assessment — they do not make "
         "the diagnosis, and a score on its own means very little."),
        ("Medical investigations", "Blood tests are sometimes requested where a physical "
         "contributor such as thyroid dysfunction or anaemia needs to be excluded."),
    ],

    treatment=[
        ("Psychiatric consultation", "The starting point is an assessment of severity, "
         "risk and the individual picture. What follows depends on that, not on a fixed "
         "protocol."),
        ("Psychological therapy", "Structured talking therapy, particularly CBT and "
         "behavioural approaches, has good evidence in depression and may be used alone "
         "in milder presentations or alongside medication in more severe ones."),
        ("Medication", "Considered where clinically indicated, with the reasons, expected "
         "timeframe and possible side effects discussed with you first. No medicine is "
         "recommended or started without an individual assessment."),
        ("Lifestyle and routine", "Re-establishing sleep, activity and daily structure is "
         "part of treatment rather than an afterthought."),
        ("Family involvement", "With your agreement, involving family often helps — both "
         "for practical support and so that those around you understand what is "
         "happening."),
        ("Follow-up", "Depression is reviewed over time. Treatment is adjusted based on "
         "how you respond, and continued for a period after improvement to reduce the "
         "chance of relapse."),
    ],
    treatment_note="How well treatment works, and how quickly, varies from person to "
                   "person. Outcomes are discussed honestly at the consultation and "
                   "nothing is promised in advance.",

    therapies=["cbt", "behavioural", "supportive", "psychoeducation", "family", "sleep",
               "relapse"],

    faqs=[
        ("Is depression the same as feeling sad?",
         "No. Sadness is a normal response to difficult events and usually lifts. "
         "Depression is persistent, lasts at least two weeks, occupies most of the day "
         "and interferes with functioning. Many people with depression say they feel "
         "flat or empty rather than sad."),
        ("Will I definitely need medication?",
         "No. Treatment depends on severity and on the individual assessment. Milder "
         "depression is often managed with psychological therapy, lifestyle change and "
         "follow-up. Medication is considered where it is clinically indicated, and the "
         "reasoning is explained to you before anything is started."),
        ("How long does treatment take?",
         "That varies and cannot be predicted at the first visit. What can be said is "
         "that improvement is usually gradual rather than sudden, that review "
         "appointments are part of the process, and that treatment is normally "
         "continued for a period after you feel better."),
        ("Can I recover without telling my family?",
         "Consultations are confidential, and the decision about who to involve is "
         "yours. That said, family support helps in most cases, and many people find it "
         "easier once someone at home understands what is going on."),
        ("What if I have had depression before?",
         "Tell the doctor at the assessment. Previous episodes, what helped and what did "
         "not, and how long recovery took are all useful in planning treatment and in "
         "watching for early warning signs."),
    ],
),

# =========================================================================
"anxiety-treatment-guntur": dict(
    name="Anxiety Disorders",
    category="Mental Health Conditions",
    title="Anxiety Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Anxiety treatment in Guntur by Dr. Manchikalapudi Tirumala Babu, "
         "M.D. (Psychiatry). Symptoms, causes, diagnosis and treatment options for "
         "anxiety, panic and phobias.",
    keyword="anxiety treatment in Guntur",
    secondary=["anxiety doctor Guntur", "panic attack treatment Guntur",
               "psychiatrist for anxiety Guntur", "anxiety consultation Guntur"],
    intro="Anxiety becomes a clinical concern when worry or fear stops being useful and "
          "starts getting in the way. This page covers what that looks like, how it is "
          "assessed and what treatment involves.",
    urgent=False,

    what=[
        "Anxiety is a normal and useful response to threat — it sharpens attention before "
        "an examination or an interview. It becomes a disorder when it is out of "
        "proportion to the situation, hard to control, persists over weeks or months, and "
        "interferes with daily life.",
        "\"Anxiety disorders\" is a group rather than a single condition. It includes "
        "generalised anxiety disorder, panic disorder, social anxiety and specific "
        "phobias. They share a core of excessive fear or worry but differ in what "
        "triggers them and how they present, which is why assessment matters before "
        "treatment.",
    ],

    symptoms=[
        ("Worry and fear", [
            "Worry that is difficult to switch off, often moving from topic to topic",
            "A persistent sense that something bad is about to happen",
            "Fear of specific situations, places or objects",
            "Fear of being judged in social or performance situations",
        ]),
        ("Physical symptoms", [
            "Racing or pounding heartbeat",
            "Breathlessness or a feeling of tightness in the chest",
            "Sweating, trembling or shakiness",
            "Stomach upset, nausea or a churning sensation",
            "Dizziness, tingling, or a feeling of being detached",
        ]),
        ("Thinking", [
            "Difficulty concentrating because worry keeps intruding",
            "Mind going blank under pressure",
            "Anticipating the worst outcome as the most likely one",
        ]),
        ("Behaviour", [
            "Avoiding places, people or situations that trigger the anxiety",
            "Seeking repeated reassurance",
            "Difficulty falling asleep because the mind will not settle",
            "Using alcohol or other substances to take the edge off",
        ]),
    ],
    symptoms_note="Physical symptoms of anxiety can closely resemble heart, thyroid or "
                  "respiratory conditions. That overlap is exactly why a proper "
                  "assessment matters rather than assuming either explanation.",

    causes=[
        ("Biological factors", "Family history, temperament and differences in the brain's "
         "threat-response systems all contribute to susceptibility."),
        ("Psychological factors", "Patterns of interpreting situations as threatening, "
         "difficulty tolerating uncertainty, and earlier frightening experiences."),
        ("Stress and environment", "Work or examination pressure, financial insecurity, "
         "relationship difficulty, illness in the family and major life change."),
        ("Physical health", "Thyroid disorders, anaemia, heart rhythm problems and some "
         "medicines can produce anxiety-like symptoms, which is why physical health forms "
         "part of the assessment."),
        ("Substances", "Caffeine, nicotine, alcohol withdrawal and stimulant use commonly "
         "worsen anxiety, sometimes substantially."),
    ],
    causes_note="Anxiety disorders usually arise from several factors interacting rather "
                "than one cause, and the trigger is not always identifiable.",

    when=[
        "Worry or fear is persistent and difficult to control",
        "It is interfering with work, study, sleep or relationships",
        "You are avoiding situations you used to manage",
        "Panic episodes are occurring, or you are afraid of the next one",
        "Physical symptoms are present and heart or thyroid causes have been excluded",
        "You are relying on alcohol or other substances to manage it",
    ],

    diagnosis=[
        ("Clinical interview", "What the anxiety feels like, what sets it off, how long it "
         "has been present and what you have stopped doing because of it."),
        ("History", "Physical health, current medicines, caffeine and substance use, and "
         "family history."),
        ("Mental state examination", "Structured assessment during the consultation, "
         "including how the anxiety is affecting thinking and functioning."),
        ("Screening questionnaires", "Rating scales may be used to gauge severity and "
         "track progress. They are aids to assessment, not diagnostic tests."),
        ("Medical investigations", "Where physical symptoms are prominent, tests may be "
         "requested — or previous results reviewed — to exclude a physical contributor."),
    ],

    treatment=[
        ("Psychiatric consultation", "Assessment first: which anxiety disorder, how "
         "severe, what is maintaining it, and whether anything physical is contributing."),
        ("Psychological therapy", "CBT has strong evidence across the anxiety disorders. "
         "Graded, planned exposure to avoided situations is often central, particularly "
         "in phobias and panic."),
        ("Medication", "Considered where clinically indicated, especially in moderate to "
         "severe presentations. Options, expected timeframe and side effects are "
         "discussed before anything is started."),
        ("Lifestyle and behavioural changes", "Sleep, regular activity, and reducing "
         "caffeine, nicotine and alcohol often make a measurable difference."),
        ("Breathing and relaxation techniques", "Practical methods for managing the "
         "physical arousal that accompanies anxiety and panic."),
        ("Follow-up", "Anxiety treatment is reviewed and adjusted. Avoidance tends to "
         "rebuild quietly, so follow-up matters."),
    ],
    treatment_note="Response to treatment varies between individuals and between the "
                   "different anxiety disorders. No particular outcome or timeframe is "
                   "promised.",

    therapies=["cbt", "behavioural", "stress", "sleep", "supportive", "psychoeducation",
               "social"],

    faqs=[
        ("Are panic attacks dangerous?",
         "A panic attack is intensely unpleasant and can feel like a medical emergency, "
         "but the attack itself is not physically dangerous. Because the symptoms "
         "overlap with heart and thyroid conditions, a first episode should still be "
         "assessed properly rather than assumed to be panic."),
        ("Is anxiety just stress?",
         "They overlap but are not the same. Stress is a response to an identifiable "
         "pressure and usually eases when the pressure does. An anxiety disorder "
         "persists, is often out of proportion to the situation, and may continue with "
         "no obvious trigger."),
        ("Will I have to take medication for life?",
         "In most cases, no. Duration depends on the diagnosis, severity and how you "
         "respond, and it is reviewed at follow-up. Many people are treated for a "
         "defined period. Any decision about starting, continuing or stopping is made "
         "with you and never without assessment."),
        ("Can therapy work without medication?",
         "For mild to moderate anxiety, psychological therapy alone is often effective "
         "and is frequently the first choice. In more severe presentations the two are "
         "commonly combined. Which applies to you is a clinical judgement made at the "
         "assessment."),
        ("I have had every test and nothing was found. What now?",
         "That is a common and frustrating position, and it does not mean the symptoms "
         "are imagined. Anxiety produces genuine physical symptoms through real "
         "physiological mechanisms. Bring the reports to the consultation — they are "
         "useful, not wasted."),
    ],
),

# =========================================================================
"alcohol-de-addiction-guntur": dict(
    name="Alcohol Use Disorder",
    category="De-addiction &amp; Substance-Related Concerns",
    title="Alcohol De-addiction Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Alcohol de-addiction treatment in Guntur by Dr. M. Tirumala Babu, M.D. "
         "(Psychiatry). Confidential assessment, withdrawal safety, treatment "
         "options and relapse prevention.",
    keyword="alcohol de-addiction treatment in Guntur",
    secondary=["de-addiction centre Guntur", "alcohol treatment Guntur",
               "psychiatrist for alcohol addiction Guntur", "alcohol withdrawal Guntur"],
    intro="Alcohol dependence is a medical condition, not a failure of character, and it "
          "responds to treatment. This page explains what it involves and why stopping "
          "suddenly on your own can be unsafe.",
    urgent=True,
    urgent_text="Stopping alcohol abruptly after heavy, regular drinking can cause severe "
                "withdrawal, including seizures and delirium, which can be "
                "life-threatening. If you drink daily and heavily, seek medical advice "
                "before stopping rather than quitting on your own. If someone is "
                "confused, shaking severely, hallucinating or having a seizure, treat it "
                "as an emergency.",

    what=[
        "Alcohol use disorder is a pattern of drinking that a person finds hard to "
        "control and that continues despite causing harm — to health, work, finances or "
        "relationships. It sits on a spectrum from mild to severe rather than being "
        "something a person either has or does not have.",
        "Dependence is not defined by how much someone drinks or by what they drink. It "
        "is defined by the loss of control, the difficulty stopping, and the "
        "continuation despite consequences.",
    ],

    symptoms=[
        ("Loss of control", [
            "Drinking more, or for longer, than intended",
            "Repeated unsuccessful attempts to cut down or stop",
            "Strong cravings or urges to drink",
            "A great deal of time spent drinking or recovering from drinking",
        ]),
        ("Physical signs", [
            "Needing more alcohol to get the same effect (tolerance)",
            "Shaking, sweating, nausea or agitation when not drinking (withdrawal)",
            "Drinking in the morning to steady oneself",
            "Disturbed sleep, poor appetite, weight change",
        ]),
        ("Effects on life", [
            "Difficulty meeting responsibilities at work, in studies or at home",
            "Conflict in the family or the breakdown of relationships",
            "Giving up activities that used to matter",
            "Continuing to drink despite a doctor's advice or a health problem",
        ]),
        ("Mental health", [
            "Low mood, anxiety or irritability, often worse the day after drinking",
            "Memory gaps or blackouts",
            "Thoughts of self-harm, which need urgent attention",
        ]),
    ],

    causes=[
        ("Biological factors", "Family history is one of the stronger risk factors. "
         "Differences in how alcohol is metabolised and in the brain's reward system "
         "both play a part."),
        ("Mental health", "Depression, anxiety and trauma-related difficulties often sit "
         "alongside alcohol use, each making the other harder to treat. Assessing both "
         "together matters."),
        ("Social and environmental factors", "Availability, peer and workplace drinking "
         "culture, and stress at home or at work."),
        ("Early and prolonged use", "Starting young and drinking heavily over years both "
         "increase the likelihood of dependence developing."),
    ],
    causes_note="No single factor explains dependence. It develops through an "
                "interaction of biology, mental health and circumstances, and blame is "
                "not a useful part of the clinical picture.",

    when=[
        "You have tried to cut down or stop and have not been able to",
        "You feel shaky, sweaty or agitated when you have not had a drink",
        "Drinking is affecting work, finances, health or family life",
        "Family members have raised concerns about your drinking",
        "You are drinking to manage low mood, anxiety or sleep",
        "You want to stop and need it to be done safely",
    ],

    diagnosis=[
        ("Clinical interview", "A confidential, non-judgemental conversation about the "
         "pattern of drinking, previous attempts to stop, and what has happened as a "
         "result."),
        ("History", "Physical health, mental health, previous withdrawal episodes or "
         "seizures, current medicines, and other substance use."),
        ("Mental state examination", "Including assessment of mood and of risk, since "
         "depression and alcohol use frequently occur together."),
        ("Screening questionnaires", "Standard tools may be used to gauge severity and "
         "guide planning. They inform the assessment rather than replace it."),
        ("Medical investigations", "Blood tests, including liver function, may be "
         "requested where clinically indicated."),
    ],

    treatment=[
        ("Assessment and planning", "Severity, withdrawal risk, physical health and any "
         "co-existing mental health condition are assessed before a plan is made."),
        ("Medically supervised withdrawal", "Where dependence is significant, stopping "
         "needs medical supervision. This is a safety matter, not a formality."),
        ("Medication", "Medicines to manage withdrawal, and in some cases to support "
         "continued abstinence, may be considered where clinically indicated, with the "
         "reasoning explained to you."),
        ("Motivational and psychological work", "Motivational interviewing, relapse "
         "prevention and CBT-based approaches address the patterns that maintain "
         "drinking."),
        ("Treating co-existing conditions", "Where depression or anxiety is present, "
         "treating it alongside the alcohol use gives a better chance than treating "
         "either alone."),
        ("Family involvement", "With consent, family involvement substantially supports "
         "recovery, and family members often need support and information themselves."),
        ("Follow-up and relapse prevention", "Recovery is monitored over time. A lapse is "
         "treated as clinical information to work with, not as a reason to stop "
         "treatment."),
    ],
    treatment_note="Recovery from alcohol dependence is realistic and common, but it is "
                   "a process rather than a single event, and no outcome is guaranteed. "
                   "Relapse is frequent and is managed, not punished.",

    therapies=["motivational", "relapse", "cbt", "family", "psychoeducation", "supportive",
               "stress"],

    faqs=[
        ("Can I just stop drinking on my own?",
         "If you drink heavily and daily, stopping suddenly without medical advice can "
         "be dangerous — withdrawal can include seizures and delirium. Get an assessment "
         "first so that stopping can be done safely. Lighter, less regular drinking is a "
         "different situation, and the assessment will tell you which applies."),
        ("Is this confidential? Will my employer or family find out?",
         "Consultations are treated as confidential medical information. What is shared, "
         "and with whom, is discussed with you. Many people choose to involve family "
         "because it helps, but that decision is yours."),
        ("Do I have to accept that I can never drink again?",
         "Goals are set individually. For some people, particularly where dependence is "
         "severe or there is organ damage, abstinence is the clinically appropriate "
         "goal. For others, reduction may be discussed. This is a clinical conversation, "
         "not a moral one."),
        ("What if I relapse?",
         "Relapse is common in recovery from dependence and is treated as part of the "
         "process. It is useful clinical information about triggers, and a reason to "
         "come back rather than to stay away."),
        ("My family member drinks but refuses to come. What can I do?",
         "Families can consult for guidance on how to approach the conversation and what "
         "support is available. Treatment works best when the person is willing, and "
         "motivational approaches exist precisely because willingness often develops "
         "gradually."),
    ],
),

}
