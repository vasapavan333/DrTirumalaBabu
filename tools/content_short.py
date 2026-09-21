"""Five-section copy for the conditions that do not have a full page.

`python tools/build_pages.py` renders each of these as:

    1. page title and short introduction
    2. what the condition is
    3. signs and symptoms
    4. when to consult a psychiatrist
    5. treatment and management
    6. frequently asked questions
    7. appointment call to action

The long ten-section form lives in content_detail.py; a slug in either file
gets a page, and anything in both is taken from content_detail.py. Moving a
condition from here to there is how a page gets promoted to the full template.

Register rules — the same ones that govern content_detail.py:
  - plain language first, the clinical term in brackets after
  - a symptom list is a description, never a checklist to diagnose yourself
    with; the template adds that framing automatically
  - causes are contributors, never "the cause"
  - no medicine names, no doses, no duration promises, no outcome promises
  - `urgent` switches on the red-flag callout, and `urgent_text` replaces its
    opening sentence when the risk is specific to that condition

Nothing here has been reviewed by Dr. Tirumala Babu. See TODO-CONTENT.md §11.
"""

MENTAL_HEALTH = "Mental Health Conditions"
NEURO = "Neurological &amp; Cognitive Conditions"
DE_ADDICTION = "De-addiction &amp; Substance-Related Concerns"
PSYCHOSOMATIC = "Sexual &amp; Psychosomatic Health"

SHORT: dict[str, dict] = {}

# ===========================================================================
# Mental health
# ===========================================================================

SHORT["stress-management-guntur"] = dict(
    name="Stress",
    category=MENTAL_HEALTH,
    title="Stress Management in Guntur | Dr. M. Tirumala Babu",
    meta="Help for persistent stress in Guntur — when ongoing pressure starts "
         "affecting sleep, mood, concentration or physical health, and what a "
         "psychiatric assessment offers.",
    keyword="stress management in Guntur",
    intro="Stress is the body's normal response to demand, and in short bursts "
          "it is useful. It becomes a clinical concern when it does not switch "
          "off — when the pressure is constant, and sleep, mood, concentration "
          "or physical health start to give way under it.",
    urgent=False,
    what=[
        "Stress is not itself a psychiatric diagnosis. It is a state of "
        "sustained physical and mental arousal, and the reason it matters in "
        "psychiatry is that prolonged stress is one of the most common routes "
        "into anxiety disorders, depression, insomnia and stress-related "
        "physical symptoms.",
        "Two people under identical pressure will not be affected identically. "
        "What tends to decide the outcome is how long it lasts, how much "
        "control the person has over it, what support surrounds them and what "
        "else they are carrying at the time.",
    ],
    symptoms=[
        "Feeling constantly on edge, rushed or unable to switch off",
        "Sleep that is hard to start, broken, or unrefreshing",
        "Irritability, a shorter temper, or tearfulness that is out of character",
        "Difficulty concentrating, or forgetting things that are normally easy",
        "Headaches, muscle tension, stomach upsets or palpitations with no other cause found",
        "Appetite that has clearly gone up or down",
        "Withdrawing from people, or dropping activities that used to help",
        "Relying more on alcohol, tobacco or sleep aids to wind down",
    ],
    when=[
        "The pressure has been constant for weeks or months rather than days",
        "Sleep has been disturbed for more than two or three weeks",
        "Work, study or family life is measurably suffering",
        "Physical symptoms have been investigated and nothing physical was found",
        "You are using alcohol, tobacco or other substances to cope",
        "Low mood or persistent worry has started on top of the stress",
    ],
    treatment=[
        ("Assessment first",
         "The consultation establishes whether this is stress alone or whether "
         "an anxiety disorder, a depressive episode or a physical illness has "
         "developed underneath it. That distinction changes what is "
         "appropriate, which is why it comes first."),
        ("Practical stress management",
         "Structured work on sleep timing, routine, workload, breathing and "
         "relaxation. For stress that has not yet become a disorder, this is "
         "usually the main part of the plan."),
        ("Talking approaches",
         "Where unhelpful thinking patterns or avoidance are keeping the cycle "
         "going, a structured talking approach can be useful. Which one suits "
         "is decided from the assessment."),
        ("Medication, only if indicated",
         "Stress on its own is not usually treated with medicine. Where an "
         "anxiety disorder, depression or persistent insomnia has developed, "
         "medication may be one of the options discussed — with the reasons "
         "for and against it explained."),
    ],
    therapies=["stress", "cbt", "sleep", "supportive", "psychoeducation"],
    faqs=[
        ("Is stress a mental illness?",
         "No. Stress is a normal response, not a diagnosis. It becomes a "
         "medical concern when it is prolonged enough to disturb sleep, mood, "
         "concentration or physical health, or when an anxiety or depressive "
         "condition has developed alongside it."),
        ("Do I need medicine for stress?",
         "Usually not. Stress by itself is generally managed with practical "
         "changes and talking approaches. Medication becomes a question only "
         "if the assessment finds a condition that calls for it, and that is "
         "discussed with you before anything is started."),
        ("My tests came back normal but I still feel unwell. Why?",
         "Sustained stress produces real physical symptoms — tension "
         "headaches, palpitations, stomach upsets, fatigue. Normal "
         "investigations do not mean the symptoms are imagined; they mean the "
         "explanation is likely to lie elsewhere, and that is worth assessing "
         "rather than ignoring."),
    ],
)

SHORT["panic-disorder-treatment-guntur"] = dict(
    name="Panic Disorder",
    category=MENTAL_HEALTH,
    title="Panic Attack Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Panic disorder treatment in Guntur. Sudden episodes of intense fear "
         "with chest tightness, breathlessness and palpitations — what they "
         "are and how they are treated.",
    keyword="panic attack treatment in Guntur",
    intro="A panic attack is a surge of intense fear that peaks within minutes "
          "and brings strong physical symptoms with it — a pounding heart, "
          "chest tightness, breathlessness, shaking, a feeling of losing "
          "control. It is frightening, it is common, and it is treatable.",
    urgent=False,
    what=[
        "A panic attack is an episode, not a condition. Many people have one "
        "at some point and never have another. Panic disorder is diagnosed "
        "when the attacks recur and the person starts living around them — "
        "dreading the next one, avoiding places where one happened, or "
        "checking constantly for the first physical signs.",
        "The symptoms are genuinely physical, which is why so many people "
        "first present to a casualty department convinced they are having a "
        "heart attack. Being told the heart is fine is reassuring for an hour "
        "and rarely for longer, because the fear itself has not been "
        "addressed. That is what treatment is for.",
    ],
    symptoms=[
        "Sudden intense fear that peaks within a few minutes",
        "Pounding or racing heartbeat, chest tightness or chest pain",
        "Breathlessness, or a feeling of choking or smothering",
        "Trembling, sweating, chills or hot flushes",
        "Dizziness, light-headedness or a feeling of being about to faint",
        "Numbness or tingling, often in the hands or around the mouth",
        "A sense of unreality, or of being detached from yourself",
        "Fear of dying, losing control or going mad during the episode",
        "Between episodes: persistent worry about the next one, and avoiding places where one happened",
    ],
    when=[
        "You have had more than one unexpected attack",
        "You have started avoiding places, travel or situations because of them",
        "You are worrying between attacks about when the next will come",
        "Cardiac and other physical causes have been checked and found clear",
        "The attacks are affecting work, study, driving or family life",
        "You are using alcohol or sedatives to keep them at bay",
    ],
    treatment=[
        ("Ruling out physical causes",
         "Thyroid problems, heart rhythm disturbances, certain medicines and "
         "withdrawal states can all produce identical symptoms. Where these "
         "have not already been checked, that is arranged first."),
        ("Understanding the cycle",
         "A large part of treatment is learning how a normal bodily sensation "
         "gets interpreted as danger, which produces more symptoms, which "
         "confirms the danger. Seeing the loop clearly is often the point at "
         "which attacks start to lose their grip."),
        ("Cognitive behavioural therapy",
         "CBT has a strong evidence base in panic disorder. It works on the "
         "catastrophic interpretation of physical sensations and on the "
         "avoidance that keeps the fear alive."),
        ("Medication where appropriate",
         "Medication is an option for some people, particularly where attacks "
         "are frequent or an anxiety or depressive disorder sits alongside "
         "them. What is suitable, and whether it is needed at all, is decided "
         "in the consultation."),
    ],
    therapies=["cbt", "behavioural", "stress", "psychoeducation", "supportive"],
    faqs=[
        ("Can a panic attack harm me?",
         "A panic attack is intensely unpleasant but is not itself dangerous, "
         "and it does not cause a heart attack. That said, chest pain and "
         "breathlessness should always be assessed medically the first time "
         "rather than assumed to be panic."),
        ("Why do they come out of nowhere?",
         "They often feel unprovoked, but an assessment frequently finds "
         "triggers the person had not connected — poor sleep, caffeine, a "
         "period of stress, or a bodily sensation that was misread. Part of "
         "the work is identifying them."),
        ("Will I need medicine for life?",
         "No one can answer that before an assessment, and any claim about "
         "duration made in advance should be treated with caution. Many people "
         "with panic disorder do well with a time-limited course of therapy, "
         "with or without medication for a period."),
    ],
)

SHORT["phobia-treatment-guntur"] = dict(
    name="Phobias",
    category=MENTAL_HEALTH,
    title="Phobia Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Treatment for specific phobias and social phobia in Guntur — "
         "persistent fear of a place, object or situation that leads to "
         "avoidance, and how it is assessed and treated.",
    keyword="phobia treatment in Guntur",
    intro="A phobia is a strong, persistent fear of a particular object, place "
          "or situation, out of proportion to the actual risk, which the "
          "person starts arranging their life to avoid. The avoidance is "
          "usually what does the damage, and it is also what treatment "
          "targets.",
    urgent=False,
    what=[
        "Almost everyone dislikes something. A phobia is different in degree: "
        "the fear is intense, it is reliably triggered, and avoiding the "
        "trigger has started to cost the person something — a job, a journey, "
        "a treatment they need, a social life.",
        "Specific phobias attach to one thing: heights, injections, blood, "
        "dogs, lifts, flying, examinations. Social phobia (social anxiety "
        "disorder) attaches to being observed or judged, and tends to be more "
        "pervasive because so much of ordinary life involves other people. "
        "Both respond well to treatment, and both tend to persist untreated.",
    ],
    symptoms=[
        "Immediate, intense fear whenever the trigger is present or expected",
        "Physical symptoms on exposure — racing heart, sweating, shaking, nausea",
        "Going out of your way to avoid the trigger, sometimes at real cost",
        "Anticipatory dread for days before an unavoidable encounter",
        "Knowing the fear is out of proportion and still being unable to override it",
        "In social phobia: fear of blushing, shaking or saying the wrong thing in front of others",
        "In blood or injection phobia: faintness rather than a racing heart, and occasional actual fainting",
    ],
    when=[
        "Avoidance is interfering with work, study, travel or relationships",
        "You are avoiding medical or dental treatment because of it",
        "The fear has widened from one situation to several",
        "You are drinking or taking something to get through the situation",
        "Low mood or general anxiety has developed on top of it",
        "A child's fear is stopping them attending school or mixing with other children",
    ],
    treatment=[
        ("Assessment",
         "The consultation establishes which phobia it is, how far the "
         "avoidance has spread, and whether another condition — panic "
         "disorder, depression, generalised anxiety — has grown alongside it."),
        ("Graded exposure",
         "The core treatment for most phobias is planned, gradual contact with "
         "the feared situation, at a pace the person agrees to, until the fear "
         "response settles. It is structured work, not being thrown in at the "
         "deep end."),
        ("Cognitive behavioural therapy",
         "Alongside exposure, CBT addresses the predictions that keep the fear "
         "going — what the person expects will happen, and what actually does."),
        ("Medication, in specific circumstances",
         "Medication is not the mainstay for a specific phobia. It may be "
         "considered in social phobia, or where a depressive or anxiety "
         "disorder sits alongside, and that is a decision made after "
         "assessment."),
    ],
    therapies=["behavioural", "cbt", "social", "psychoeducation", "supportive"],
    faqs=[
        ("Will I be forced to face the thing I fear?",
         "No. Exposure work is planned with you, starts well below the level "
         "that frightens you, and only moves on when you are ready. Being "
         "pushed past your consent is not treatment and does not work."),
        ("Is social shyness the same as social phobia?",
         "No. Shyness is a temperament; social phobia is a condition in which "
         "the fear of being judged is intense enough to make a person avoid "
         "situations that matter to them. The dividing line is the "
         "interference, and that is a clinical judgement."),
        ("My child is terrified of school. Is that a phobia?",
         "It might be, and it might be several other things — bullying, a "
         "learning difficulty, separation anxiety, low mood. School refusal "
         "always deserves an assessment rather than pressure."),
    ],
)

SHORT["ocd-treatment-guntur"] = dict(
    name="Obsessive-Compulsive Disorder (OCD)",
    category=MENTAL_HEALTH,
    title="OCD Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="OCD treatment in Guntur. Intrusive thoughts, repeated washing, "
         "checking or counting — what obsessive-compulsive disorder is, how it "
         "is assessed and what treatment involves.",
    keyword="OCD treatment in Guntur",
    intro="Obsessive-compulsive disorder involves unwanted thoughts, images or "
          "urges that keep returning (obsessions), and things the person feels "
          "driven to do to relieve the distress they cause (compulsions). It "
          "is not fussiness or a liking for order, and it responds to proper "
          "treatment.",
    urgent=False,
    what=[
        "The obsession is the intrusive thought — contamination, harm, doubt, "
        "symmetry, a blasphemous or violent image that horrifies the person "
        "having it. The compulsion is what they do to make the feeling "
        "subside: washing, checking, counting, repeating, arranging, seeking "
        "reassurance, or a mental ritual nobody can see.",
        "The relief a compulsion brings is real and brief, and each repetition "
        "teaches the brain that the ritual is what kept the disaster away. "
        "That is the loop. People with OCD usually know the fear is out of "
        "proportion, which is exactly why the condition is so exhausting to "
        "live with and so often hidden.",
    ],
    symptoms=[
        "Intrusive thoughts, images or urges that return however hard you push them away",
        "Fear of contamination, and washing or cleaning far beyond what is needed",
        "Repeated checking — locks, gas, switches, documents, the body",
        "Counting, repeating actions, or needing things arranged in an exact way",
        "Mental rituals: praying, repeating phrases, reviewing memories for reassurance",
        "Asking others repeatedly for reassurance about the same fear",
        "Rituals taking up an hour a day or much more",
        "Distress or panic when a ritual is interrupted or prevented",
        "Knowing the fear is excessive but being unable to stop acting on it",
    ],
    when=[
        "Rituals are taking up significant time each day",
        "Work, study, sleep or relationships are being affected",
        "Family members are being drawn into performing or enabling the rituals",
        "The intrusive thoughts are violent, sexual or blasphemous and causing shame",
        "Skin damage from washing, or physical harm from any ritual",
        "Low mood has developed alongside",
    ],
    treatment=[
        ("Assessment",
         "The consultation maps what the obsessions and compulsions actually "
         "are, how much time they consume, and whether depression or another "
         "anxiety condition has developed alongside — which is common."),
        ("Exposure and response prevention",
         "The best-evidenced psychological treatment for OCD: planned contact "
         "with the trigger while deliberately not performing the ritual, at an "
         "agreed pace, so the brain learns the feared outcome does not follow."),
        ("Cognitive behavioural therapy",
         "Works on the beliefs that give the intrusive thoughts their power — "
         "particularly the idea that having a thought is the same as wanting "
         "or causing it."),
        ("Medication where indicated",
         "Medication has an established place in OCD, often alongside therapy "
         "rather than instead of it. Whether it is appropriate, and what form "
         "it takes, is decided in the consultation."),
        ("Working with the family",
         "Relatives frequently end up providing reassurance or performing "
         "rituals to reduce distress. Unwinding that, gently and with "
         "everyone's agreement, is usually part of the plan."),
    ],
    therapies=["behavioural", "cbt", "family", "psychoeducation", "relapse"],
    faqs=[
        ("I have violent or disturbing thoughts. Does that make me dangerous?",
         "Intrusive thoughts of this kind are a recognised feature of OCD and "
         "are distressing precisely because they are so far from what the "
         "person wants. They are a symptom, not an intention. It is worth "
         "saying out loud in a consultation rather than carrying alone."),
        ("Isn't everyone a bit OCD?",
         "No. Liking order or double-checking a lock is ordinary. OCD is "
         "diagnosed when obsessions and compulsions consume significant time "
         "and cause real distress or impairment — a difference of kind, not "
         "just degree."),
        ("Can OCD be treated without medicine?",
         "For some people, yes — exposure and response prevention is a "
         "treatment in its own right. For others, medication makes the therapy "
         "possible. It depends on severity and on the individual assessment, "
         "so it is not something this page can decide for you."),
    ],
)

SHORT["bipolar-disorder-treatment-guntur"] = dict(
    name="Bipolar Disorder",
    category=MENTAL_HEALTH,
    title="Bipolar Disorder Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Bipolar disorder treatment in Guntur — episodes of elevated and "
         "lowered mood, how the condition is assessed, and what long-term "
         "management and relapse prevention involve.",
    keyword="bipolar disorder treatment in Guntur",
    intro="Bipolar disorder involves episodes in which mood, energy and "
          "activity are markedly raised, and episodes in which they are "
          "markedly lowered, with periods of stability in between. It is a "
          "long-term condition, and it is one that responds well to consistent "
          "treatment and follow-up.",
    urgent=True,
    urgent_text="<strong>A severe manic or depressive episode can put someone "
                "at immediate risk, and needs urgent assessment rather than an "
                "appointment in a few days.</strong>",
    what=[
        "The depressive side looks much like depression: low mood, loss of "
        "interest, fatigue, disturbed sleep and appetite, hopelessness. The "
        "elevated side — mania, or its milder form hypomania — brings raised "
        "mood or irritability, reduced need for sleep, rapid speech and "
        "thought, inflated confidence, and decisions that carry real "
        "consequences.",
        "Because the depressive episodes are what usually bring someone to a "
        "doctor, bipolar disorder is frequently treated as depression for "
        "years before the pattern is recognised. That matters, because the "
        "treatment of the two is not the same. A careful history — including "
        "what family members have observed — is what tells them apart.",
    ],
    symptoms=[
        "During an elevated episode: unusually high or irritable mood lasting days",
        "Needing far less sleep than usual and not feeling tired",
        "Talking faster than usual, or thoughts racing too quickly to follow",
        "Inflated confidence, or plans well beyond what is realistic",
        "Spending, risk-taking or decisions that are out of character",
        "During a depressive episode: persistent low mood and loss of interest",
        "Fatigue, disturbed sleep, poor concentration, feelings of worthlessness",
        "A clear pattern of episodes with more settled periods in between",
        "Family noticing the change before the person does",
    ],
    when=[
        "Mood has swung well beyond your normal range and stayed there for days",
        "You have needed much less sleep than usual without feeling tired",
        "Someone close to you has raised concern about your behaviour or spending",
        "A previous diagnosis of depression has not responded as expected",
        "A depressive episode has brought thoughts of self-harm — seek help the same day",
        "There is a family history of bipolar disorder and you are noticing episodes",
    ],
    treatment=[
        ("Careful diagnosis",
         "Distinguishing bipolar disorder from depression, from ADHD, and from "
         "the effects of substances or a physical illness takes a full history "
         "and usually information from family. Getting this right is the "
         "single most important step."),
        ("Treating the current episode",
         "What is appropriate depends on whether the person is currently "
         "elevated, depressed or stable. The options and their reasons are "
         "discussed with you and, where you wish, with your family."),
        ("Long-term management",
         "Bipolar disorder is managed over years rather than weeks. Regular "
         "review, stable sleep and routine, and continuity with one clinician "
         "all make a material difference to how often episodes recur."),
        ("Relapse prevention",
         "Most people have early warning signs that are consistent from "
         "episode to episode — a change in sleep, in spending, in speed of "
         "speech. Identifying yours, and agreeing in advance what happens when "
         "they appear, is a central part of the plan."),
        ("Family involvement",
         "With the patient's agreement, involving family helps enormously: "
         "they often see an episode starting before the person does."),
    ],
    therapies=["psychoeducation", "family", "relapse", "cbt", "sleep", "supportive"],
    faqs=[
        ("Is bipolar disorder the same as mood swings?",
         "No. Everyday mood swings last hours and respond to events. Bipolar "
         "episodes last days to weeks, change energy, sleep and judgement as "
         "well as mood, and are often visible to everyone around the person."),
        ("Do I have to take medication for life?",
         "That is a question for your psychiatrist and your own circumstances, "
         "not for a website. What can be said is that bipolar disorder is "
         "usually managed long-term, that stopping treatment abruptly is a "
         "well-recognised trigger for relapse, and that any change should be "
         "planned rather than sudden."),
        ("Can I work with bipolar disorder?",
         "Many people do, particularly where the condition is treated, sleep "
         "and routine are protected, and there is a plan for what happens if "
         "early warning signs appear."),
        ("Should my family be involved?",
         "Where you are comfortable with it, yes — it is one of the more "
         "useful things you can do. Family members often notice an episode "
         "beginning, and they cope far better when they understand what they "
         "are seeing."),
    ],
)

SHORT["schizophrenia-treatment-guntur"] = dict(
    name="Schizophrenia",
    category=MENTAL_HEALTH,
    title="Schizophrenia Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Schizophrenia treatment and follow-up in Guntur — what the condition "
         "involves, when to seek an assessment, and how treatment and family "
         "support work together.",
    keyword="schizophrenia treatment in Guntur",
    intro="Schizophrenia is a condition that affects how a person thinks, "
          "perceives and behaves. It is widely misunderstood and heavily "
          "stigmatised. It is also treatable, and outcomes are meaningfully "
          "better when treatment starts early and continues consistently.",
    urgent=True,
    what=[
        "Symptoms are usually described in two groups. The first covers "
        "experiences that are added — hearing voices, fixed beliefs that are "
        "not shared by others, disorganised speech or thinking. The second "
        "covers what is reduced: motivation, emotional expression, speech, "
        "social contact. The second group is less dramatic and often more "
        "disabling over time.",
        "Schizophrenia does not mean a split personality, and the large "
        "majority of people with the condition are not violent — they are "
        "considerably more likely to be victims of violence than perpetrators "
        "of it. What they do face is a condition that interferes with study, "
        "work and relationships, and which responds to treatment, follow-up "
        "and a family that understands what is happening.",
    ],
    symptoms=[
        "Hearing voices, or other perceptions others do not share",
        "Fixed beliefs that are not shared by those around the person and do not shift with evidence",
        "Speech or thinking that is hard for others to follow",
        "Suspiciousness, or a sense of being watched, followed or interfered with",
        "Marked drop in motivation, self-care or day-to-day functioning",
        "Flattened emotional expression, or reduced speech",
        "Withdrawal from friends, family, study or work",
        "Sleep reversal, or a gradual change in behaviour noticed first by family",
    ],
    when=[
        "Any of the above has been present for weeks rather than days",
        "A young adult's functioning at study or work has dropped sharply without clear reason",
        "The person believes something that others around them find impossible, and cannot be reasoned out of it",
        "There is talk of harm to themselves or anyone else — seek help immediately",
        "Self-care, eating or sleeping has broken down",
        "A previous episode is showing the same early signs again",
    ],
    treatment=[
        ("Assessment and ruling out other causes",
         "Substance use, certain physical illnesses and some medicines can "
         "produce similar symptoms. A full assessment establishes what is "
         "actually happening before treatment is planned."),
        ("Treating the episode",
         "Medication has an established role in treating psychotic symptoms. "
         "What is suitable is an individual decision made in the consultation, "
         "with the reasoning explained to the patient and, where they agree, "
         "to the family."),
        ("Continuity of follow-up",
         "This is the part that most affects the long term. Regular review "
         "allows treatment to be adjusted, side effects to be managed, and "
         "early signs of relapse to be caught."),
        ("Family psychoeducation",
         "Families carry most of the care in practice. Understanding what the "
         "condition is, how to respond during a difficult period, and how to "
         "protect their own wellbeing changes outcomes for everyone involved."),
        ("Rebuilding function",
         "Social skills work, a graded return to study or work, and structure "
         "in the day are part of recovery rather than an afterthought."),
    ],
    therapies=["psychoeducation", "family", "social", "relapse", "supportive", "cbt"],
    faqs=[
        ("Does schizophrenia mean a split personality?",
         "No. That is a persistent myth and describes something else entirely. "
         "Schizophrenia affects thinking, perception and motivation."),
        ("Are people with schizophrenia dangerous?",
         "The great majority are not. People with the condition are more "
         "likely to be harmed by others than to harm anyone. Risk rises in "
         "untreated acute episodes, which is an argument for early treatment "
         "rather than for fear."),
        ("Can someone recover?",
         "Many people live full lives — working, studying, raising families — "
         "with treatment and follow-up. Others have a more relapsing course. "
         "Nobody can predict which before an assessment, and anyone promising "
         "a particular outcome in advance should be treated with caution."),
        ("What can the family do?",
         "Learn what the condition is, keep the routine and the follow-up "
         "steady, notice early warning signs, and avoid arguing someone out of "
         "a fixed belief — it rarely helps and usually costs trust. "
         "Psychoeducation sessions cover all of this."),
    ],
)

SHORT["psychosis-treatment-guntur"] = dict(
    name="Psychosis",
    category=MENTAL_HEALTH,
    title="Psychosis Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Assessment and treatment of psychosis in Guntur — hearing voices, "
         "fixed false beliefs and confused thinking, and why early treatment "
         "matters.",
    keyword="psychosis treatment in Guntur",
    intro="Psychosis describes a loss of contact with shared reality — hearing "
          "or seeing things others do not, holding beliefs others find "
          "impossible, or thinking that has become hard to follow. It is a "
          "symptom rather than a single illness, and the first task is always "
          "to find out what is causing it.",
    urgent=True,
    what=[
        "Psychosis can arise in schizophrenia, in bipolar disorder, in severe "
        "depression, after substance use, in delirium from a physical illness, "
        "after a head injury, and in some neurological conditions. These are "
        "genuinely different situations with genuinely different treatments, "
        "which is why an assessment matters more here than almost anywhere "
        "else in psychiatry.",
        "The period between symptoms starting and treatment beginning — the "
        "duration of untreated psychosis — is one of the few factors "
        "consistently linked to how well someone does afterwards. Shorter is "
        "better. That is the single strongest argument against waiting to see "
        "whether it passes.",
    ],
    symptoms=[
        "Hearing voices when no one is present, or other perceptions others do not share",
        "Fixed beliefs that others find impossible and that do not shift with evidence",
        "Strong suspicion of being watched, followed, poisoned or plotted against",
        "Speech that jumps between unconnected ideas, or is hard to follow",
        "Marked change in behaviour, self-care or sleep",
        "Withdrawal, or responding to something others cannot perceive",
        "Confusion or disorientation — which can point to a physical cause needing urgent attention",
    ],
    when=[
        "Any of these symptoms is present — psychosis is assessed early, not watched",
        "There is confusion, fever or a recent head injury alongside — treat this as a medical emergency",
        "The person is not eating, drinking or sleeping",
        "There is any talk of harm to themselves or others — seek help immediately",
        "Symptoms followed the use of, or withdrawal from, alcohol or another substance",
        "A previous episode is showing the same early signs",
    ],
    treatment=[
        ("Finding the cause",
         "The first consultation establishes what is driving the psychosis — a "
         "psychiatric condition, a substance, a physical illness or a "
         "neurological problem. Physical investigations are arranged where the "
         "picture calls for them."),
        ("Treating the episode",
         "Treatment is directed at the underlying cause as well as the "
         "symptoms. What is appropriate differs completely between, say, a "
         "substance-induced episode and a first episode of schizophrenia."),
        ("Keeping the person safe",
         "Where someone is at risk, or unable to care for themselves, "
         "inpatient care may be the right setting. The consultation will say "
         "so plainly and help arrange it."),
        ("Family involvement and follow-up",
         "Families need to know what they are seeing and what to do. Regular "
         "review after the acute phase is what reduces the chance of the next "
         "episode."),
    ],
    therapies=["psychoeducation", "family", "supportive", "relapse", "social"],
    faqs=[
        ("Is psychosis permanent?",
         "Not necessarily. Some episodes are brief and related to a substance, "
         "a physical illness or an acute stress; others are part of a longer-"
         "term condition. Which it is can only be established by assessment "
         "and, often, by following what happens over time."),
        ("Should I argue with a fixed false belief?",
         "Arguing rarely works and usually damages trust. It is generally "
         "better to avoid both agreeing and confronting — acknowledge the "
         "distress, stay calm, and focus on getting an assessment."),
        ("Can substance use cause this?",
         "Yes. Cannabis and several other substances can precipitate psychotic "
         "symptoms, and withdrawal states can too. It is one of the first "
         "things an assessment asks about, and answering honestly changes the "
         "treatment for the better."),
    ],
)

SHORT["anger-management-guntur"] = dict(
    name="Anger Management Concerns",
    category=MENTAL_HEALTH,
    title="Anger Management Help in Guntur | Dr. M. Tirumala Babu",
    meta="Anger management support in Guntur — when temper starts damaging "
         "relationships, work or safety, what usually lies underneath it, and "
         "how it is assessed and treated.",
    keyword="anger management in Guntur",
    intro="Anger is a normal emotion and not a diagnosis. It becomes a reason "
          "to seek help when it arrives faster than you can manage it, lasts "
          "longer than the situation warrants, or leaves damage behind — to "
          "relationships, to work, or to someone's safety.",
    urgent=True,
    urgent_text="<strong>If anyone is at risk of being hurt, that comes before "
                "an appointment.</strong>",
    what=[
        "In psychiatry, persistent anger is usually treated as a signal rather "
        "than the whole story. It sits on top of something often enough that "
        "looking underneath is the first thing an assessment does: depression, "
        "which in men in particular frequently presents as irritability rather "
        "than sadness; anxiety; untreated ADHD; alcohol or substance use; "
        "chronic pain or poor sleep; the aftermath of a difficult event; and "
        "sometimes a neurological cause.",
        "That is not a way of excusing the behaviour. Anger that harms people "
        "is a problem in its own right and needs to stop. But treating what is "
        "driving it is usually what makes the change hold, rather than "
        "willpower alone.",
    ],
    symptoms=[
        "Losing your temper faster or more often than you used to",
        "Reactions that feel out of proportion to what triggered them",
        "Shouting, breaking things, or physical aggression",
        "Regret, shame or blankness afterwards",
        "People at home or work changing their behaviour to avoid setting you off",
        "Anger that is worse when you have been drinking",
        "Persistent irritability alongside poor sleep, low mood or loss of interest",
        "Physical build-up beforehand — tension, heat, a racing heart",
    ],
    when=[
        "Anyone has been hurt, or has been frightened that they might be",
        "Your relationships, job or studies are suffering because of it",
        "You are drinking or using something and the anger is worse for it",
        "There is low mood, anxiety or poor sleep alongside",
        "You have noticed a change in temperament that others have commented on",
        "You want to stop and have not been able to on your own",
    ],
    treatment=[
        ("Looking for what is underneath",
         "The assessment screens for depression, anxiety, ADHD, substance use, "
         "sleep disorder, pain and, where the history suggests it, "
         "neurological causes. Treating a missed depression often does more "
         "for the anger than anger work alone."),
        ("Recognising the build-up",
         "Anger has a physical run-up — tension, heat, a quickening pulse. "
         "Learning to catch it early enough to act is the practical core of "
         "the work, because once it peaks there is very little left to "
         "control."),
        ("Cognitive behavioural approaches",
         "Work on the interpretations that turn an event into a provocation, "
         "and on building a response other than the automatic one."),
        ("Involving the family, carefully",
         "Where it is safe and everyone agrees, family or couple sessions help "
         "— both to change the pattern and to make sure the people affected "
         "are not carrying it alone."),
        ("Addressing alcohol and substances",
         "Where these are part of the picture they are treated as part of the "
         "plan, not afterwards. Anger work rarely holds while heavy drinking "
         "continues."),
    ],
    therapies=["cbt", "behavioural", "stress", "family", "couple", "motivational"],
    faqs=[
        ("Is anger a mental illness?",
         "Not by itself. It becomes a clinical matter when it is severe, "
         "persistent or harmful, or when it is a symptom of a condition such "
         "as depression, anxiety, ADHD or a substance problem — which is what "
         "the assessment looks for."),
        ("My partner says I need help but I think I'm fine. Should I come?",
         "A consultation is not a verdict. It is an hour spent finding out "
         "whether there is something treatable underneath, and people quite "
         "often leave with an answer they did not expect — in either "
         "direction."),
        ("Can this be treated without medicine?",
         "Often, yes. Where the anger is not driven by an underlying condition "
         "that calls for medication, the work is behavioural and practical. "
         "Where there is an underlying condition, treating it is usually what "
         "makes the rest possible."),
    ],
)

SHORT["mental-wellbeing-guntur"] = dict(
    name="Mental Wellbeing",
    category=MENTAL_HEALTH,
    title="Mental Wellbeing Support in Guntur | Dr. M. Tirumala Babu",
    meta="Preventive mental health support in Guntur — coping skills, early "
         "advice and a professional opinion before difficulties become "
         "entrenched. You do not need a diagnosis to come.",
    keyword="mental wellbeing support in Guntur",
    intro="Not every reason to see a psychiatrist is a diagnosis. Some people "
          "come because something has changed and they want an informed "
          "opinion on it, or because a difficult period is coming and they "
          "would rather prepare than cope afterwards. That is a legitimate use "
          "of a consultation.",
    urgent=False,
    what=[
        "Mental health conditions rarely arrive fully formed. There is usually "
        "a period beforehand in which sleep is slipping, worry is rising, "
        "concentration is going or a person simply does not feel like "
        "themselves. Attending at that stage tends to mean shorter, simpler "
        "treatment than attending a year later.",
        "A wellbeing consultation covers what has changed and over what "
        "period, what is loading you at the moment, how sleep and routine are "
        "holding up, and whether what you are describing is within normal "
        "variation or the early part of something worth treating. Sometimes "
        "the useful answer is that nothing is wrong — that is a real result, "
        "not a wasted visit.",
    ],
    symptoms=[
        "Not feeling like yourself, without being able to say exactly why",
        "Sleep, appetite or energy that has shifted and not come back",
        "Finding work or study harder than it used to be",
        "Worrying more, or enjoying things less",
        "A major life change ahead — exams, a move, a new baby, retirement, a bereavement",
        "A family history of a mental health condition and wanting to know the early signs",
        "Wanting coping strategies before a demanding period rather than during it",
    ],
    when=[
        "Something has changed and has not settled after a few weeks",
        "You are managing, but with noticeably more effort than before",
        "Other people have commented on a change in you",
        "You want to know whether what you are experiencing is normal",
        "You would like practical coping skills ahead of a demanding period",
        "There is a family history and you want to know what to watch for",
    ],
    treatment=[
        ("A proper assessment, not a quick reassurance",
         "The consultation is the same structured assessment anyone else "
         "receives. Being told nothing is wrong means more when the question "
         "has actually been examined."),
        ("Practical skills",
         "Sleep, routine, workload, relaxation and the habits that protect "
         "mental health through a demanding period — concrete, and specific to "
         "your circumstances."),
        ("Knowing your own early warning signs",
         "Particularly useful where there is a family history or a previous "
         "episode: what your own early signs are, and what you would do if "
         "they appeared."),
        ("A clear route back",
         "If nothing needs treating now, you leave knowing what would make it "
         "worth returning. That is often the most valuable part."),
    ],
    therapies=["psychoeducation", "stress", "sleep", "supportive", "cbt"],
    faqs=[
        ("Can I see a psychiatrist without a diagnosis?",
         "Yes. A consultation is a professional assessment of what you are "
         "experiencing, and one legitimate outcome is that no condition is "
         "present and no treatment is needed."),
        ("Will I be put on medication?",
         "Not unless an assessment finds a condition where medication is "
         "appropriate, and not without discussing it with you first. Many "
         "consultations end with advice and a review rather than a "
         "prescription."),
        ("Is it confidential?",
         "Consultations are treated as confidential medical information, in "
         "line with professional practice and applicable law. You are welcome "
         "to ask at the start what is recorded and what is shared."),
    ],
)

# ===========================================================================
# Neurological and cognitive
# ===========================================================================

SHORT["migraine-treatment-guntur"] = dict(
    name="Migraine",
    category=NEURO,
    title="Migraine Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Migraine assessment and treatment in Guntur — recurrent headache "
         "with nausea and light sensitivity, and how migraine and mood "
         "interact.",
    keyword="migraine treatment in Guntur",
    intro="Migraine is a neurological condition, not simply a bad headache. "
          "It brings recurrent attacks of head pain, often with nausea and "
          "sensitivity to light or sound, and often enough to interfere "
          "seriously with work, study and family life.",
    urgent=True,
    urgent_text="<strong>A headache that is sudden and severe, the worst you "
                "have had, or comes with fever, neck stiffness, weakness, "
                "confusion or a fit, needs emergency assessment now — not an "
                "appointment.</strong>",
    what=[
        "A migraine attack typically builds over hours, lasts from several "
        "hours to a few days, and is often one-sided and throbbing. Movement "
        "makes it worse. Many people need to lie down in a dark, quiet room. "
        "Some have an aura beforehand — visual disturbance, tingling or speech "
        "difficulty — which is a recognised part of the condition.",
        "Migraine sits in this clinic's scope because the traffic between "
        "migraine and mental health runs both ways: depression, anxiety and "
        "poor sleep are all more common in people with frequent migraine, and "
        "each of them makes attacks more frequent in turn. Treating only one "
        "side of that and ignoring the other tends to disappoint.",
    ],
    symptoms=[
        "Recurrent headache, often one-sided and throbbing",
        "Nausea or vomiting during an attack",
        "Sensitivity to light, sound or smell",
        "Pain that worsens with routine movement",
        "Aura before the headache — visual disturbance, tingling, speech difficulty",
        "Attacks lasting from a few hours to a few days",
        "Identifiable triggers: missed meals, poor sleep, stress, certain foods, menstrual cycle",
        "Low mood, anxiety or disturbed sleep between attacks",
    ],
    when=[
        "Attacks are frequent enough to affect work, study or family life",
        "The pattern of your headaches has changed",
        "You are using pain relief on most days — this can itself drive headache",
        "Low mood, anxiety or insomnia has developed alongside",
        "Attacks started after a head injury",
        "Any new headache after the age of 50 deserves assessment",
    ],
    treatment=[
        ("Assessment and red flags",
         "The consultation establishes the headache pattern and checks for "
         "features that point to something other than migraine. Imaging is "
         "arranged where the picture calls for it, not routinely."),
        ("A headache diary",
         "Recording attacks, their timing and what preceded them is the most "
         "useful single thing most patients can do. Patterns become visible "
         "over a few weeks that are invisible in a single consultation."),
        ("Trigger and lifestyle work",
         "Regular meals, consistent sleep, hydration and stress management "
         "reduce attack frequency for many people, and cost nothing."),
        ("Medication, acute and preventive",
         "Treatment of an attack and prevention of future attacks are "
         "different questions with different answers. Both are individual "
         "decisions made after assessment, and this page does not name "
         "medicines or doses for either."),
        ("Treating what travels with it",
         "Where depression, anxiety or insomnia is present, treating it "
         "usually improves the headaches as well — and the reverse."),
    ],
    therapies=["stress", "sleep", "cbt", "psychoeducation", "supportive"],
    faqs=[
        ("Is migraine just a severe headache?",
         "No. It is a neurological condition with a characteristic pattern — "
         "recurrent attacks, often with nausea and sensitivity to light and "
         "sound, worsened by movement, sometimes preceded by an aura."),
        ("Why would I see a psychiatrist about headaches?",
         "Because migraine and mental health are closely linked in both "
         "directions. Where depression, anxiety or insomnia sits alongside "
         "frequent migraine, treating the headaches alone usually gets you "
         "only part of the way."),
        ("Can taking too many painkillers make it worse?",
         "Frequent use of acute pain relief can itself sustain headache — "
         "medication-overuse headache is well recognised. If you are taking "
         "something for headache on most days, that is worth raising at the "
         "consultation."),
    ],
)

SHORT["autism-assessment-guntur"] = dict(
    name="Autism Spectrum Disorder",
    category=NEURO,
    title="Autism Assessment in Guntur | Dr. M. Tirumala Babu",
    meta="Autism spectrum assessment in Guntur — differences in communication, "
         "social interaction and behaviour, what an assessment involves, and "
         "the support that follows it.",
    keyword="autism assessment in Guntur",
    intro="Autism spectrum disorder is a developmental condition affecting how "
          "a person communicates, relates to others and experiences the world "
          "around them. It is present from early development, it varies "
          "enormously between individuals, and an assessment is about "
          "understanding a person rather than labelling them.",
    urgent=False,
    what=[
        "Autism is described as a spectrum because its presentation ranges so "
        "widely. One person may have no speech and need substantial daily "
        "support; another may be academically able, employed, and struggling "
        "mainly with social exhaustion and change. Both are autistic, and "
        "neither description fits the other.",
        "Common threads are differences in social communication — reading "
        "unspoken cues, holding back-and-forth conversation, managing eye "
        "contact — alongside repetitive behaviours, intense specific "
        "interests, a strong preference for routine, and unusual sensitivity "
        "to sound, light, texture or touch. These are differences in wiring, "
        "not in effort or upbringing.",
    ],
    symptoms=[
        "Delayed speech, or unusual patterns of language use",
        "Limited eye contact, or difficulty reading facial expressions and tone",
        "Difficulty starting or holding a back-and-forth conversation",
        "Playing or working alongside others rather than with them",
        "Repetitive movements — rocking, hand-flapping, spinning objects",
        "Strong, narrow interests pursued in great depth",
        "Marked distress when routine changes",
        "Over- or under-sensitivity to noise, light, texture, taste or touch",
        "In adults: long-standing social exhaustion, and coping by copying others",
    ],
    when=[
        "A child is not meeting speech or social milestones",
        "A child has lost speech or social skills they previously had — arrange this promptly",
        "School has raised concerns about communication or behaviour",
        "Change of routine causes distress out of proportion to the event",
        "An adult recognises a lifelong pattern and wants it properly assessed",
        "Anxiety, low mood or sleep difficulty has developed alongside",
    ],
    treatment=[
        ("Developmental assessment",
         "A detailed developmental history, information from family and, where "
         "available, from school, and observation. Hearing is checked, because "
         "hearing loss can look like a social communication difficulty."),
        ("Explaining the findings",
         "The assessment produces a description of how this particular person "
         "works — strengths as well as difficulties — rather than a label on "
         "its own. That description is what makes school and workplace support "
         "possible."),
        ("Support, not a cure",
         "Autism is not an illness to be cured, and any treatment offered on "
         "that basis should be regarded with suspicion. What helps is "
         "communication support, structure, predictable routine, a sensory "
         "environment that fits, and skills work."),
        ("Treating what sits alongside",
         "Anxiety, depression, ADHD, sleep difficulty and epilepsy are all "
         "more common in autistic people. These are treatable in their own "
         "right, and treating them often makes the largest practical "
         "difference."),
        ("Working with the family",
         "Parents and siblings are the people who make a plan work day to day. "
         "Psychoeducation and practical guidance are part of the process."),
    ],
    therapies=["psychoeducation", "family", "social", "behavioural", "supportive"],
    faqs=[
        ("Can autism be cured?",
         "No, and it is not an illness. It is a difference in development that "
         "lasts a lifetime. What changes with support is how well the "
         "environment fits the person and how much they can do within it — and "
         "any treatment claiming to cure autism should be treated with real "
         "caution."),
        ("Is it caused by vaccines or by parenting?",
         "No. Neither claim is supported by evidence. Autism has a strong "
         "developmental and genetic basis, and parents are not the cause."),
        ("Is it too late to assess an adult?",
         "No. Adults are assessed regularly, often after recognising a "
         "lifelong pattern. Many find that understanding it changes how they "
         "manage work, relationships and their own expectations of "
         "themselves."),
    ],
)

SHORT["adhd-treatment-guntur"] = dict(
    name="ADHD",
    category=NEURO,
    title="ADHD Assessment and Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="ADHD assessment in Guntur for children and adults — difficulty with "
         "attention, activity level and impulse control, how it is assessed "
         "and what treatment involves.",
    keyword="ADHD treatment in Guntur",
    intro="Attention deficit hyperactivity disorder affects attention, "
          "activity level and impulse control. It begins in childhood, and for "
          "a substantial proportion of people it does not stop there — it "
          "simply changes shape in adult life.",
    urgent=False,
    what=[
        "ADHD is usually described as having two dimensions. Inattention "
        "covers difficulty sustaining focus, losing things, missing details, "
        "being easily diverted and struggling to finish what was started. "
        "Hyperactivity and impulsivity cover restlessness, difficulty "
        "remaining seated, interrupting, and acting before thinking it "
        "through. A person may have mostly one, mostly the other, or both.",
        "Two things routinely delay diagnosis. Children who are inattentive "
        "but not disruptive tend to be described as dreamy rather than "
        "referred, and girls in particular are missed for this reason. And in "
        "adults, the visible hyperactivity often fades while the inattention, "
        "disorganisation and impulsivity remain — so the person is assessed "
        "for anxiety or depression instead, which may also be present, without "
        "the underlying ADHD ever being considered.",
    ],
    symptoms=[
        "Difficulty sustaining attention on tasks that are not immediately interesting",
        "Careless mistakes, missed details, unfinished work",
        "Losing things needed for daily tasks, and frequent forgetfulness",
        "Being easily diverted by anything happening nearby",
        "Restlessness, fidgeting, difficulty staying seated",
        "Talking excessively, interrupting, or answering before the question is finished",
        "Acting on impulse — spending, decisions, remarks later regretted",
        "Difficulty organising tasks, time and belongings",
        "In adults: chronic lateness, unfinished projects, and a history of underachievement relative to ability",
    ],
    when=[
        "School has raised concerns about attention, activity or behaviour",
        "A child's performance is clearly below what their ability suggests",
        "An adult recognises a lifelong pattern that predates their current difficulties",
        "Work or study is suffering despite genuine effort",
        "Relationships are strained by forgetfulness, lateness or impulsivity",
        "Anxiety, low mood or substance use has developed alongside",
    ],
    treatment=[
        ("Assessment across settings",
         "ADHD is diagnosed from a pattern present in more than one setting "
         "and beginning in childhood. That means a developmental history, "
         "information from family and, for children, from school. Rating "
         "scales support this; they do not replace it."),
        ("Ruling out what looks similar",
         "Poor sleep, hearing difficulty, learning disorder, anxiety, "
         "depression, thyroid problems and substance use can all produce "
         "inattention. Each is checked, because treating the wrong one wastes "
         "time."),
        ("Practical and behavioural strategies",
         "Structure, externalised reminders, broken-down tasks, adjustments at "
         "school or work, and consistent routines. For children, work with "
         "parents on behaviour management is a core part of treatment."),
        ("Medication where appropriate",
         "Medication is well established in ADHD, and is also not automatic. "
         "Whether it is suitable, what is expected of it and how it is "
         "reviewed are discussed in the consultation. No medicine is named or "
         "recommended here."),
        ("Treating what sits alongside",
         "Anxiety, depression, sleep difficulty and substance use are common "
         "alongside ADHD and are treated in their own right."),
    ],
    therapies=["behavioural", "psychoeducation", "family", "cbt", "sleep", "social"],
    faqs=[
        ("Is ADHD just poor discipline?",
         "No. It is a neurodevelopmental condition with a strong genetic "
         "component, and it is not caused by parenting, sugar or screens — "
         "although sleep and screen habits can make the symptoms harder to "
         "manage."),
        ("Can adults have ADHD?",
         "Yes, and many are diagnosed for the first time in adult life, often "
         "after a child of theirs is assessed. The symptoms must have been "
         "present in childhood, even if nobody recognised them at the time."),
        ("Does an ADHD diagnosis mean medication?",
         "Not necessarily. Some people are managed with practical and "
         "behavioural strategies and adjustments. Whether medication is "
         "appropriate depends on severity, age and the individual assessment, "
         "and is decided with you."),
        ("Is an online ADHD test enough?",
         "No. Online questionnaires are screening aids at best. A score does "
         "not establish or rule out a diagnosis, which requires a full "
         "assessment across settings."),
    ],
)

SHORT["dementia-care-guntur"] = dict(
    name="Dementia",
    category=NEURO,
    title="Dementia Assessment and Care in Guntur | Dr. M. Tirumala Babu",
    meta="Dementia assessment in Guntur — memory and thinking difficulties in "
         "later life, why reversible causes must be excluded first, and the "
         "support available to families.",
    keyword="dementia assessment in Guntur",
    intro="Dementia describes a progressive decline in memory, thinking and "
          "the ability to manage daily tasks, beyond what ageing alone "
          "explains. An early assessment matters — partly because some causes "
          "of the same picture are treatable and reversible, and partly "
          "because planning is far easier while the person can take part in "
          "it.",
    urgent=False,
    what=[
        "Forgetting a name and retrieving it later is ordinary. Dementia "
        "involves a sustained decline — repeated questions within a single "
        "conversation, difficulty with familiar tasks, getting lost on known "
        "routes, losing the thread of language, and changes in judgement, mood "
        "and personality. Family usually notices the pattern well before the "
        "person does.",
        "Several conditions produce this picture, and they behave differently. "
        "Just as importantly, so do a number of treatable problems: "
        "depression, thyroid disease, vitamin B12 deficiency, the side effects "
        "of medicines, poor sleep, and delirium from an infection. Those must "
        "be excluded before anyone concludes that a decline is permanent.",
    ],
    symptoms=[
        "Short-term memory loss that is getting worse over months",
        "Repeating questions or stories within the same conversation",
        "Difficulty with familiar tasks — cooking, handling money, taking medicines",
        "Getting lost on routes that were once routine",
        "Word-finding difficulty, or losing the thread mid-sentence",
        "Confusion about time, date or place",
        "Changes in mood, personality or judgement",
        "Withdrawal from conversation and activity",
        "Neglect of self-care or of the household",
    ],
    when=[
        "Memory or thinking has declined steadily over months",
        "Daily tasks such as money, cooking or medicines are becoming unsafe",
        "There has been a change in personality, judgement or behaviour",
        "Confusion has come on suddenly over hours or days — this suggests delirium and needs urgent medical attention",
        "The person has become lost, or left something dangerous unattended",
        "The family is struggling to cope and needs support",
    ],
    treatment=[
        ("Assessment and excluding reversible causes",
         "Cognitive testing, a history from the family, and investigation for "
         "the treatable causes that mimic dementia — thyroid disease, B12 "
         "deficiency, depression, medicine side effects, infection. Imaging "
         "where indicated."),
        ("Establishing what kind of decline it is",
         "Different conditions cause dementia and they progress differently, "
         "so the distinction affects both management and what the family can "
         "expect."),
        ("Treating what can be treated",
         "Depression and anxiety are common alongside and are treatable. "
         "Sleep, pain and sensory problems all affect cognition and are worth "
         "addressing. Where medication for the dementia itself is appropriate, "
         "that is discussed individually."),
        ("Managing behaviour and distress",
         "Agitation, suspicion, sleep reversal and wandering are often the "
         "hardest part for families. Practical, non-medication approaches are "
         "tried first, and usually help more than families expect."),
        ("Supporting the carers",
         "Carer exhaustion is the single most common reason a home "
         "arrangement breaks down. Psychoeducation, realistic expectations and "
         "planning are part of the care, not an extra."),
    ],
    therapies=["psychoeducation", "family", "supportive", "behavioural", "sleep"],
    faqs=[
        ("Is forgetfulness in old age always dementia?",
         "No. Mild slowing of recall is a normal part of ageing. Dementia "
         "involves a progressive decline that interferes with daily function — "
         "and depression, thyroid problems, B12 deficiency and medicine side "
         "effects can all imitate it, which is why assessment matters."),
        ("Why assess it if it cannot be cured?",
         "Because reversible causes are found more often than people expect; "
         "because treatable conditions alongside it can be addressed; because "
         "some forms have specific management; and because planning is far "
         "easier while the person can still be part of the decisions."),
        ("My relative refuses to come. What can I do?",
         "It is common. Framing it as a general check-up rather than a memory "
         "assessment often helps, as does coming along yourself — family "
         "observations are a legitimate and valuable part of the assessment."),
        ("Confusion started suddenly. Is that dementia?",
         "Sudden confusion over hours or days is more likely to be delirium — "
         "often from an infection, dehydration or a medicine — and that needs "
         "urgent medical attention rather than a routine appointment."),
    ],
)

SHORT["sleep-disorder-treatment-guntur"] = dict(
    name="Sleep Disorders",
    category=NEURO,
    title="Sleep Disorder Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Treatment for insomnia and other sleep problems in Guntur — trouble "
         "falling or staying asleep, unrefreshing sleep, and the two-way link "
         "between sleep and mental health.",
    keyword="sleep disorder treatment in Guntur",
    intro="Difficulty falling asleep, staying asleep, or waking unrefreshed is "
          "one of the most common reasons people come to a psychiatrist — and "
          "one of the most rewarding to treat, because improving sleep "
          "improves almost everything else.",
    urgent=False,
    what=[
        "Insomnia is the commonest pattern: trouble getting to sleep, waking "
        "in the night or waking too early, with daytime consequences. But "
        "sleep problems are not one condition. Sleep apnoea, restless legs, "
        "disrupted body-clock timing, nightmares and the sleep disturbance "
        "that comes with depression, anxiety, pain or substance use are all "
        "different problems requiring different answers.",
        "The relationship with mental health runs in both directions. Poor "
        "sleep is a symptom of depression and anxiety, and it is also a risk "
        "factor for both. Persistent early-morning waking is a recognised "
        "feature of depression; difficulty falling asleep because the mind "
        "will not stop is characteristic of anxiety. Treating the sleep alone "
        "and ignoring what is underneath tends not to hold.",
    ],
    symptoms=[
        "Taking a long time to fall asleep most nights",
        "Waking repeatedly, or lying awake in the early hours",
        "Waking much earlier than intended and being unable to return to sleep",
        "Sleeping through the night and still waking unrefreshed",
        "Daytime sleepiness, poor concentration, irritability",
        "Loud snoring, or being told you stop breathing in your sleep",
        "Unpleasant sensations in the legs at night with an urge to move them",
        "Dread of bedtime, or clock-watching through the night",
        "Relying on alcohol or sedatives to get to sleep",
    ],
    when=[
        "Sleep has been disturbed for more than three or four weeks",
        "Daytime functioning, driving or work safety is affected",
        "You have been told you snore heavily or stop breathing in your sleep",
        "Low mood, anxiety or irritability has developed alongside",
        "You are using alcohol or over-the-counter sedatives to sleep",
        "Early-morning waking with low mood — this pattern deserves prompt assessment",
    ],
    treatment=[
        ("Working out which problem it is",
         "The assessment separates insomnia from sleep apnoea, body-clock "
         "problems, restless legs, and the sleep disturbance of another "
         "condition. Where sleep apnoea is suspected, onward referral for a "
         "sleep study is arranged."),
        ("Sleep hygiene and behavioural methods",
         "Consistent timing, light exposure, what happens in the hour before "
         "bed, and structured behavioural methods for persistent insomnia. "
         "These are first-line and are more effective than most people "
         "expect."),
        ("Treating the underlying condition",
         "Where depression, anxiety, pain or substance use is driving the "
         "sleep problem, that is treated — and the sleep usually follows."),
        ("Medication, cautiously and briefly",
         "Sleep medication has a place, generally short-term and alongside "
         "behavioural work rather than instead of it. Long-term reliance "
         "creates its own problems, which is why this is a decision made "
         "carefully in the consultation."),
    ],
    therapies=["sleep", "cbt", "stress", "psychoeducation", "supportive"],
    faqs=[
        ("How much sleep should I get?",
         "Most adults need somewhere between seven and nine hours, but there "
         "is real individual variation. The practical test is how you function "
         "in the day, not the number itself."),
        ("Is it safe to take sleeping tablets long-term?",
         "Long-term use carries well-recognised problems, including tolerance "
         "and difficulty stopping. That is why behavioural treatment is "
         "first-line and why any medication is reviewed rather than repeated "
         "indefinitely."),
        ("Does alcohol help me sleep?",
         "Alcohol shortens the time to fall asleep and then fragments the "
         "second half of the night, so sleep is lighter and less restorative. "
         "It is one of the more common reasons for waking at three in the "
         "morning."),
        ("I snore loudly and wake up tired. Is that insomnia?",
         "That pattern points more towards sleep apnoea than insomnia, and it "
         "is worth assessing — it is treatable, and untreated it carries "
         "cardiovascular risk as well as daytime sleepiness."),
    ],
)

# ===========================================================================
# De-addiction and substance-related
# ===========================================================================

SHORT["tobacco-de-addiction-guntur"] = dict(
    name="Tobacco Dependence",
    category=DE_ADDICTION,
    title="Quit Smoking and Tobacco Help in Guntur | Dr. Tirumala Babu",
    meta="Help to stop smoking or chewing tobacco in Guntur — why quitting is "
         "hard, what withdrawal involves, and the medical and behavioural "
         "support available at the clinic.",
    keyword="tobacco de-addiction in Guntur",
    intro="Most people who use tobacco want to stop, and most have already "
          "tried. That is not a failure of will — nicotine is among the more "
          "strongly dependence-forming substances in common use, and quitting "
          "with proper support works considerably better than quitting alone.",
    urgent=False,
    what=[
        "Dependence has two halves that need separate handling. The physical "
        "half is nicotine withdrawal: irritability, restlessness, poor "
        "concentration, disturbed sleep, increased appetite and intense "
        "craving, worst in the first week and easing substantially over two to "
        "four. The behavioural half is longer-lived — tobacco tied to tea, to "
        "meals, to driving, to stress, to particular company.",
        "Chewed tobacco, gutkha and khaini carry the same dependence and their "
        "own risks, including oral cancer, and are treated with the same "
        "seriousness as smoking. The clinic's role here is assessment, "
        "planning a quit attempt properly, managing withdrawal, and treating "
        "the anxiety or low mood that often surfaces once the tobacco stops.",
    ],
    symptoms=[
        "Needing tobacco within a short time of waking",
        "Strong cravings when you cannot use it",
        "Irritability, restlessness or poor concentration without it",
        "Continuing despite a cough, breathlessness, mouth problems or a doctor's advice",
        "Repeated attempts to stop that have not held",
        "Using more than intended, or than you tell others",
        "Arranging the day around when you can use it",
        "Mouth ulcers, white patches or difficulty opening the mouth with chewed tobacco — have these examined",
    ],
    when=[
        "You want to stop and previous attempts have not lasted",
        "Withdrawal symptoms have defeated earlier attempts",
        "You have a heart, lung or mouth condition made worse by tobacco",
        "Low mood or anxiety rises whenever you try to stop",
        "You use alcohol or another substance alongside",
        "There are white patches, ulcers or restricted mouth opening — arrange examination promptly",
    ],
    treatment=[
        ("Assessment and a quit plan",
         "How much, for how long, what previous attempts looked like and what "
         "ended them. A quit date, a plan for the first fortnight, and a plan "
         "for the predictable triggers."),
        ("Managing withdrawal",
         "Withdrawal is time-limited and much easier to face when you know "
         "what to expect and when it eases. Where medical support for "
         "withdrawal is appropriate, that is discussed individually."),
        ("Motivational work",
         "Most people feel two ways about stopping, and that ambivalence is "
         "normal rather than an obstacle. Motivational approaches work with "
         "it instead of arguing against it."),
        ("Breaking the behavioural links",
         "Identifying the situations tied to tobacco and planning something "
         "else for them — this is what most often decides whether a quit "
         "attempt survives past the first month."),
        ("Treating mood and anxiety",
         "Low mood and anxiety commonly surface when tobacco stops. Treating "
         "them is part of the plan, not a separate matter."),
    ],
    therapies=["motivational", "cbt", "relapse", "psychoeducation", "behavioural", "stress"],
    faqs=[
        ("Is chewing tobacco safer than smoking?",
         "No. It carries its own serious risks, including oral cancer, and the "
         "nicotine dependence is comparable. Both are treated with the same "
         "seriousness."),
        ("How long does withdrawal last?",
         "The physical symptoms are usually at their worst in the first week "
         "and ease substantially over two to four weeks. Situational cravings "
         "can surface for longer, which is why the behavioural work matters."),
        ("I have failed several times. Is it worth trying again?",
         "Yes. Most people who stop permanently have several attempts behind "
         "them, and each one usually teaches something about what defeats it. "
         "Planned attempts with support do better than unplanned ones."),
    ],
)

SHORT["smartphone-addiction-help-guntur"] = dict(
    name="Problematic Smartphone Use",
    category=DE_ADDICTION,
    title="Help for Problematic Screen Use in Guntur | Dr. Tirumala Babu",
    meta="Support in Guntur when phone, gaming or screen use starts displacing "
         "sleep, study, work or relationships — what is actually going on, and "
         "how it is assessed.",
    keyword="help for problematic smartphone use in Guntur",
    intro="Phones are not the problem in themselves. The concern is a pattern "
          "in which screen use has started displacing the things a person "
          "needs — sleep, study, work, food, people — and attempts to cut back "
          "have not held.",
    urgent=False,
    what=[
        "There is genuine scientific debate about how best to classify this, "
        "and the honest position is that it is less settled than headlines "
        "suggest. What is clear in clinical practice is that heavy, "
        "compulsive screen use is frequently a symptom rather than the whole "
        "problem — commonly sitting on top of social anxiety, depression, "
        "ADHD, loneliness, bullying or a difficult home situation.",
        "That is why an assessment looks past the screen time figure. The "
        "useful questions are what the screen is being used to avoid or to "
        "supply, what happens when it is not available, and what has been "
        "displaced. In adolescents especially, taking the phone away without "
        "addressing what sits underneath tends to produce conflict rather than "
        "change.",
    ],
    symptoms=[
        "Screen use regularly displacing sleep — particularly late at night",
        "Study or work performance falling",
        "Meals, exercise and self-care being skipped",
        "Irritability, restlessness or distress when the phone is unavailable",
        "Repeated unsuccessful attempts to cut back",
        "Concealing the amount of use from family",
        "Withdrawal from face-to-face friendships and family time",
        "Spending on games or in-app purchases beyond what was intended",
        "Neck, eye or wrist symptoms from prolonged use",
    ],
    when=[
        "Sleep is consistently being lost to screen use",
        "School or college performance has dropped noticeably",
        "Attempts to cut back have repeatedly failed",
        "There is significant conflict at home about it",
        "Low mood, anxiety or social withdrawal has appeared alongside",
        "There is gambling, or spending that is causing difficulty",
    ],
    treatment=[
        ("Assessment that looks underneath",
         "The consultation screens for depression, social anxiety, ADHD, "
         "bullying, learning difficulty and family stress. Treating what is "
         "found usually does more than any restriction on its own."),
        ("A realistic picture of the use",
         "What is actually being done on the screen, when, and what it "
         "replaces. Specifics are far more workable than a total hours "
         "figure."),
        ("Protecting sleep first",
         "Getting devices out of the bedroom and restoring a consistent sleep "
         "time is usually the first practical step, and often the one that "
         "improves mood and concentration fastest."),
        ("Agreed structure rather than confiscation",
         "Boundaries that the young person has helped set, with alternatives "
         "planned for the displaced time, hold up better than rules imposed "
         "during an argument."),
        ("Working with the family",
         "Where an adolescent is involved, the parents are part of the plan. "
         "Sessions cover how to set limits without the household turning into "
         "a standoff."),
    ],
    therapies=["cbt", "behavioural", "family", "sleep", "motivational", "social"],
    faqs=[
        ("Is smartphone addiction a real diagnosis?",
         "Its classification is still debated, and this page will not "
         "overstate it. What is not in doubt is that the pattern causes real "
         "harm to sleep, study and relationships, and that it is assessable "
         "and treatable — usually by treating what sits underneath it."),
        ("How many hours a day is too much?",
         "There is no clinically meaningful threshold. What matters is what "
         "the use is displacing and whether the person can stop when they "
         "want to."),
        ("Should I just take my child's phone away?",
         "Abrupt confiscation usually produces conflict rather than change, "
         "especially if the phone is doing a job — managing anxiety, or "
         "supplying the only social contact that feels safe. Agreed limits, "
         "with the underlying problem addressed, work better."),
    ],
)

SHORT["substance-use-treatment-guntur"] = dict(
    name="Other Substance Use Disorders",
    category=DE_ADDICTION,
    title="Substance Use Treatment in Guntur | Dr. M. Tirumala Babu",
    meta="Confidential assessment and treatment for substance use in Guntur — "
         "cannabis, sedatives, opioids and other substances, including "
         "withdrawal safety and relapse prevention.",
    keyword="substance use treatment in Guntur",
    intro="Substance use disorders are assessed and treated confidentially "
          "here. The consultation is a medical one, not a judgement, and an "
          "honest account of what is being used and how much is the single "
          "thing that most improves the treatment you get.",
    urgent=True,
    urgent_text="<strong>Stopping some substances abruptly — particularly "
                "sedatives — can be medically dangerous, and withdrawal from "
                "others can be severe. Do not stop suddenly on your own: ask "
                "for advice first.</strong>",
    what=[
        "The pattern that defines a substance use disorder is consistent "
        "whatever the substance: use that is harder to control than intended, "
        "more time and thought given over to it, other activities dropped, "
        "tolerance rising, withdrawal when it stops, and use continuing "
        "despite clear harm. Cannabis, sedatives and sleeping tablets, "
        "opioids, inhalants and stimulants all produce their own version of "
        "it.",
        "Two points matter clinically. First, withdrawal risk differs "
        "enormously between substances — sedative withdrawal in particular can "
        "be dangerous and sometimes needs medical supervision. Second, "
        "substance use and mental illness travel together often enough that "
        "each must be assessed; treating one and ignoring the other is a "
        "common reason treatment does not hold.",
    ],
    symptoms=[
        "Using more, or for longer, than you intended",
        "Wanting to cut down and not managing to",
        "Significant time spent obtaining, using or recovering",
        "Strong cravings",
        "Use interfering with work, study, family or responsibilities",
        "Continuing despite harm to health, relationships or money",
        "Needing more to get the same effect",
        "Withdrawal symptoms when stopping, or using to prevent them",
        "Dropping activities that used to matter",
    ],
    when=[
        "You want to stop or cut down and have not managed on your own",
        "Withdrawal symptoms appear when you stop — get advice before stopping suddenly",
        "Use is affecting work, study, money or family",
        "Low mood, anxiety, suspiciousness or unusual experiences have appeared alongside",
        "Someone close to you has raised serious concern",
        "There has been an overdose, an injury, or any use by injection — seek help promptly",
    ],
    treatment=[
        ("Confidential assessment",
         "What is used, how much, for how long, what happens on stopping, and "
         "what else is going on medically and psychiatrically. Consultations "
         "are treated as confidential medical information."),
        ("Managing withdrawal safely",
         "Withdrawal is planned rather than improvised, because for some "
         "substances stopping abruptly is genuinely risky. Where inpatient or "
         "supervised withdrawal is the safer course, the consultation will say "
         "so and help arrange it."),
        ("Treating mental illness alongside",
         "Depression, anxiety and psychotic symptoms are all common "
         "alongside substance use — sometimes cause, sometimes consequence, "
         "often both. Both sides are assessed and treated."),
        ("Motivational work",
         "Feeling two ways about stopping is the normal starting point, not a "
         "sign that someone is not ready. Motivational approaches work with "
         "that rather than against it."),
        ("Relapse prevention and family involvement",
         "Identifying personal triggers and early warning signs, agreeing what "
         "happens when they appear, and — with the patient's consent — "
         "involving family, which measurably improves how well recovery "
         "holds."),
    ],
    therapies=["motivational", "relapse", "cbt", "family", "psychoeducation", "supportive"],
    faqs=[
        ("Is what I say confidential?",
         "Consultations are treated as confidential medical information, in "
         "line with professional practice and applicable law. If you want to "
         "know what is recorded and what is shared, ask at the start of the "
         "consultation."),
        ("Is cannabis harmless?",
         "No. Regular use is associated with dependence, with difficulties in "
         "motivation and memory, and — in vulnerable people — with "
         "precipitating psychotic symptoms. That does not make every user ill, "
         "but it is not a risk-free substance."),
        ("Can I just stop on my own?",
         "For some substances that is reasonable; for others, particularly "
         "sedatives and sleeping tablets, stopping abruptly can be medically "
         "dangerous. Ask before you stop rather than afterwards."),
        ("Does relapse mean treatment failed?",
         "No. Relapse is common in the course of recovery and is treated as "
         "information about what the plan did not yet cover, rather than as a "
         "verdict on the person."),
    ],
)

# ===========================================================================
# Sexual and psychosomatic health
# ===========================================================================

SHORT["sexual-health-consultation-guntur"] = dict(
    name="Sexual Health Concerns",
    category=PSYCHOSOMATIC,
    title="Sexual Health Consultation in Guntur | Dr. Tirumala Babu",
    meta="Confidential psychiatric consultation in Guntur for sexual "
         "difficulties — including performance anxiety, the effects of stress "
         "and mood, and relationship factors.",
    keyword="sexual health consultation in Guntur",
    intro="Sexual difficulties are common, they are rarely discussed, and they "
          "very often have a treatable psychological component alongside any "
          "physical one. The consultation is confidential and the questions "
          "are medical ones.",
    urgent=False,
    what=[
        "Sexual function involves physical health, hormones, medication, mood, "
        "anxiety and the state of a relationship, all at once. Difficulties "
        "commonly arise where several of these overlap — for example a "
        "physical factor starts the problem, anxiety about recurrence "
        "maintains it, and relationship strain follows. Untangling that is "
        "what an assessment does.",
        "A psychiatric consultation in this area covers performance anxiety "
        "and the anticipatory worry that sustains it; the effect of "
        "depression, anxiety, stress and poor sleep on desire and function; "
        "the sexual side effects of medicines, which are common and "
        "under-discussed; alcohol and substance use; relationship and "
        "communication difficulties; and the considerable amount of "
        "misinformation people arrive carrying. Where a physical or hormonal "
        "cause is likely, you are referred appropriately rather than treated "
        "here.",
    ],
    symptoms=[
        "Loss of interest in sex that is out of character",
        "Anxiety before or during sex, or anticipatory dread",
        "Difficulty with arousal or with maintaining it",
        "Difficulties with timing or control",
        "Pain or discomfort — this should always be examined medically",
        "Avoiding intimacy, and tension in the relationship as a result",
        "Preoccupation, shame or guilt about sexual matters",
        "Difficulties that began after starting a new medicine",
        "Distress driven by misinformation rather than by any actual problem",
    ],
    when=[
        "The difficulty has persisted for more than a few weeks",
        "It is causing distress, or strain in your relationship",
        "It began after a change in medication",
        "Low mood, anxiety or heavy stress is present alongside",
        "Alcohol or substance use is part of the picture",
        "There is pain, bleeding or a physical change — see a doctor for examination first",
    ],
    treatment=[
        ("A confidential, factual assessment",
         "Medical history, medication, alcohol and substance use, mood, sleep, "
         "stress and relationship context. Where a physical or hormonal cause "
         "is likely, onward referral is arranged."),
        ("Correcting misinformation",
         "A substantial proportion of the distress seen in this area comes "
         "from myths rather than from any dysfunction. Accurate information is "
         "often a large part of the treatment."),
        ("Treating anxiety and mood",
         "Performance anxiety responds well to structured psychological work. "
         "Where depression or an anxiety disorder is present, treating it "
         "frequently resolves the sexual difficulty as well."),
        ("Reviewing medication",
         "Sexual side effects are common with several classes of medicine and "
         "are worth raising. Any change is a decision made with the "
         "prescribing doctor, never independently."),
        ("Involving the partner, where you wish",
         "Couple sessions are available where both partners want them and the "
         "difficulty involves the relationship as well as the individual."),
    ],
    therapies=["cbt", "couple", "psychoeducation", "stress", "supportive"],
    faqs=[
        ("Is this confidential?",
         "Yes. Consultations are treated as confidential medical information, "
         "in line with professional practice and applicable law."),
        ("Is this a physical or a psychological problem?",
         "Very often both, and the proportions differ between people. That is "
         "precisely what an assessment is for, and why being referred for a "
         "physical opinion where appropriate is part of the process."),
        ("Can my partner come with me?",
         "Yes, if you would like them to. Part of the consultation may still "
         "be conducted with you alone, which is normal clinical practice."),
        ("I read something online that worries me. Is it true?",
         "Possibly not. A great deal of what circulates on this subject is "
         "inaccurate, and some of it is written to sell something. Bring the "
         "question — an accurate answer is often all that is needed."),
    ],
)

SHORT["somatic-symptom-treatment-guntur"] = dict(
    name="Somatic Symptom Disorder",
    category=PSYCHOSOMATIC,
    title="Treatment for Somatic Symptoms in Guntur | Dr. Tirumala Babu",
    meta="Help in Guntur for distressing physical symptoms that investigations "
         "do not fully explain — the symptoms are real, and there is a "
         "treatable pattern behind the distress.",
    keyword="somatic symptom treatment in Guntur",
    intro="Some people live with physical symptoms that are genuinely "
          "distressing and disabling, and that repeated investigations do not "
          "fully explain. The first thing to say is that the symptoms are "
          "real. The second is that there is a recognised, treatable pattern "
          "here.",
    urgent=False,
    what=[
        "Somatic symptom disorder is not a diagnosis of exclusion and it does "
        "not mean the symptoms are imagined or deliberate. It describes a "
        "situation in which physical symptoms — pain, fatigue, giddiness, "
        "palpitations, breathlessness, digestive trouble — are accompanied by "
        "disproportionate worry, time and energy spent on them, and a "
        "substantial effect on daily life.",
        "A person can have a diagnosed physical illness and this pattern at "
        "the same time; the two are not alternatives. The usual course is "
        "years of tests, several opinions, mounting cost and mounting anxiety, "
        "with each normal result reassuring briefly and then fuelling the "
        "search for the next explanation. The aim of treatment is not to prove "
        "the symptoms wrong, but to reduce the distress and disability that "
        "have grown around them.",
    ],
    symptoms=[
        "Physical symptoms that persist despite normal investigations",
        "Substantial time and thought given to the symptoms",
        "High anxiety about what they might mean",
        "Repeated consultations, tests or second opinions",
        "Brief reassurance after a normal result, then renewed worry",
        "Checking the body frequently, or searching online for explanations",
        "Reduced activity, work or social life because of the symptoms",
        "Frustration at feeling disbelieved by doctors or family",
        "Low mood, poor sleep or anxiety alongside",
    ],
    when=[
        "Symptoms have persisted for months despite investigation",
        "Worry about health is taking up a large part of the day",
        "You are seeking repeated tests or opinions and none has settled it",
        "Work, study or social life has narrowed because of the symptoms",
        "Low mood or anxiety has developed alongside",
        "Any new, changing or worsening symptom — have that examined medically first",
    ],
    treatment=[
        ("Taking the symptoms seriously",
         "Treatment starts from the position that the symptoms are real and "
         "the distress is warranted. It does not start from an argument about "
         "whether they exist."),
        ("A single coordinating doctor",
         "One clinician holding the overall picture, with planned review "
         "rather than investigation driven by each new worry, reduces both "
         "anxiety and cost. Fragmented care tends to make this pattern worse."),
        ("Explaining the mechanism",
         "How attention, anxiety and the nervous system amplify physical "
         "sensation is a genuine physiological account, not a polite way of "
         "saying the symptoms are imaginary. Most people find it a relief to "
         "have one that fits."),
        ("Cognitive behavioural therapy",
         "The best-evidenced psychological treatment here. It works on the "
         "checking, the reassurance-seeking and the interpretations that keep "
         "the cycle turning."),
        ("Restoring function",
         "Graded return to activity, work and social life, planned rather than "
         "waiting for the symptoms to disappear first."),
        ("Treating mood and anxiety",
         "Depression and anxiety are common alongside and treatable, and "
         "treating them usually reduces the physical distress as well."),
    ],
    therapies=["cbt", "stress", "psychoeducation", "supportive", "behavioural", "family"],
    faqs=[
        ("Are you saying it is all in my head?",
         "No. The symptoms are real and are experienced physically. What this "
         "diagnosis describes is the distress and disability that have built "
         "up around them, and that part is treatable."),
        ("What if the doctors have missed something?",
         "That possibility is taken seriously, which is why any new, changing "
         "or worsening symptom is examined medically. What treatment changes "
         "is the cycle of repeated investigation for symptoms that have "
         "already been thoroughly assessed."),
        ("Will I be told to stop seeing other doctors?",
         "No. What is usually suggested is that one doctor coordinates, so "
         "that care is planned rather than driven by each new worry — which "
         "tends to reduce both anxiety and expense."),
    ],
)
