"""A page for each non-pharmacological therapy.

The short description, what it helps with and the conditions it is used for
already live in content_pages.py, in THERAPIES — that entry is the single
source for the therapies index and for the cards on condition pages, and this
file only adds what a page of its own needs:

    intro    one paragraph under the page title
    session  what actually happens in a session, in plain terms
    suits    who it tends to suit
    limits   what it does not do — stated plainly, because a therapy page that
             only lists benefits reads as an advertisement and is not honest
    faqs     three questions per page

Availability wording is generated, not written here: a therapy marked
offered=True in THERAPIES says it is provided at the clinic, and every other
one says it may be recommended or referred. Nothing in this file should claim
availability, and nothing should promise an outcome or a number of sessions.

Nothing here has been reviewed by Dr. Tirumala Babu. See TODO-CONTENT.md §11.
"""

THERAPY_DETAIL: dict[str, dict] = {}

THERAPY_DETAIL["cbt"] = dict(
    title="CBT in Guntur | Cognitive Behavioural Therapy",
    meta="Cognitive behavioural therapy at Maruthi Hospital, Guntur — a "
         "structured, practical talking therapy for depression, anxiety, "
         "panic, OCD and insomnia.",
    keyword="cognitive behavioural therapy in Guntur",
    intro="CBT is the most thoroughly researched talking therapy in "
          "psychiatry. It works on the link between what you think, how you "
          "feel and what you do — and specifically on the patterns that keep a "
          "difficulty going long after whatever started it has passed.",
    session="Sessions are structured rather than open-ended. You and the "
            "therapist agree what to work on, look at specific recent "
            "situations in detail — what happened, what went through your "
            "mind, what you felt, what you did — and test those thoughts "
            "against the evidence rather than against reassurance. Most "
            "sessions end with something to practise before the next one, and "
            "that practice is where most of the change actually happens.",
    suits=[
        "People who prefer a practical, structured approach with clear goals",
        "Difficulties maintained by a recognisable loop — avoidance, checking, rumination",
        "Anyone wanting a time-limited course rather than open-ended therapy",
        "People who would rather learn a method they can reuse later on their own",
    ],
    limits=[
        "It asks for work between sessions; without that, results are limited",
        "It is not a quick fix, and it can feel uncomfortable before it feels better",
        "It suits some conditions far better than others — the assessment decides",
        "It is not a replacement for medication in every situation",
    ],
    faqs=[
        ("How many sessions will I need?",
         "CBT is usually time-limited and reviewed as it goes, but the number "
         "depends on the condition and on you. Nobody can give you a figure "
         "before an assessment, and a fixed course quoted in advance is worth "
         "questioning."),
        ("Do I have to talk about my childhood?",
         "Not necessarily. CBT concentrates on what is keeping the problem "
         "going now. History comes in where it helps explain a current "
         "pattern, not as a requirement."),
        ("Can CBT replace medication?",
         "Sometimes, and sometimes not. For some conditions it is a treatment "
         "in its own right; for others medication is what makes therapy "
         "possible; often the two are used together. It depends on the "
         "assessment."),
    ],
)

THERAPY_DETAIL["family"] = dict(
    title="Family Therapy in Guntur | Dr. M. Tirumala Babu",
    meta="Family therapy at Maruthi Hospital, Guntur — sessions with family "
         "alongside the patient, used in schizophrenia, bipolar disorder and "
         "substance use.",
    keyword="family therapy in Guntur",
    intro="A mental health condition is rarely experienced by one person "
          "alone. Family therapy brings relatives into the room alongside the "
          "patient, to look at how the difficulty affects the household and "
          "how the household can support recovery rather than accidentally "
          "work against it.",
    session="Sessions involve the patient and whichever family members they "
            "want present. The work usually starts with explaining what the "
            "condition is and is not, because a great deal of family conflict "
            "comes from misreading symptoms as choices. It then moves to "
            "practical matters: how to respond during a difficult period, what "
            "to do about early warning signs, how to handle medication and "
            "appointments without the house turning into a supervision "
            "arrangement, and how relatives look after their own health while "
            "caring.",
    suits=[
        "Conditions where family support materially changes the outcome — schizophrenia, bipolar disorder",
        "Substance use disorders, where the household is affected and involved",
        "Child and adolescent concerns, where the parents are part of any plan",
        "Families who are exhausted, at odds with each other, or unsure what they are dealing with",
    ],
    limits=[
        "It needs the patient's agreement — nobody is discussed without their consent",
        "It does not work where a family member is unsafe or unwilling to participate",
        "It is not a way of getting someone treated against their will",
        "It does not replace the patient's own treatment",
    ],
    faqs=[
        ("Will my family be told everything I say?",
         "No. What is shared in family sessions is agreed with you. "
         "Individual consultations remain confidential, and part of your care "
         "may still be conducted with you alone."),
        ("My relative refuses treatment. Can family therapy help?",
         "It can help the family respond more effectively and look after "
         "themselves, and it sometimes changes the situation enough that the "
         "person becomes willing. It is not a mechanism for treating someone "
         "who has not consented."),
        ("Is this about blaming the family?",
         "No. Families do not cause schizophrenia or bipolar disorder, and "
         "that idea has done real harm historically. The work is about "
         "understanding and support, not fault."),
    ],
)

THERAPY_DETAIL["couple"] = dict(
    title="Couple Therapy in Guntur | Dr. M. Tirumala Babu",
    meta="Couple therapy at Maruthi Hospital, Guntur — joint sessions where "
         "relationship difficulties are part of the picture, or a condition is "
         "straining the relationship.",
    keyword="couple therapy in Guntur",
    intro="Couple therapy is offered where relationship difficulties are part "
          "of what brought someone to the clinic, or where a mental health "
          "condition has begun to strain the relationship — which, given "
          "enough time, most of them do.",
    session="Both partners attend. The work is practical: how each person "
            "understands what is happening, where communication is breaking "
            "down, and what agreements would reduce the conflict. Where one "
            "partner has a diagnosed condition, a substantial part of the "
            "early work is explaining it — many couples arrive having "
            "interpreted symptoms as indifference, laziness or rejection, and "
            "that interpretation does more damage than the symptoms.",
    suits=[
        "Couples where a mental health condition is affecting the relationship",
        "Sexual difficulties with a relationship or anxiety component",
        "Repeated conflict that neither partner can find a way out of",
        "One partner adjusting to the other's diagnosis",
    ],
    limits=[
        "Both partners have to want to attend; it does not work with one dragged along",
        "It is not appropriate where there is violence or intimidation in the relationship",
        "It does not decide whether a relationship should continue",
        "It is not a substitute for treating an individual condition",
    ],
    faqs=[
        ("Will the therapist take sides?",
         "No. The work is on the pattern between you rather than on who is "
         "right, and a therapist who starts adjudicating has stopped being "
         "useful to either of you."),
        ("What if only one of us wants to come?",
         "Then couple therapy is not the right starting point. Individual work "
         "is still available, and sometimes changes things enough that joint "
         "sessions become possible later."),
        ("Is it confidential?",
         "Sessions are treated as confidential medical information. What is "
         "raised in a joint session is, by definition, shared between you "
         "both — anything you want kept separate is better raised in an "
         "individual consultation."),
    ],
)

THERAPY_DETAIL["psychoeducation"] = dict(
    title="Psychoeducation in Guntur | Understanding Your Diagnosis",
    meta="Psychoeducation in Guntur — structured explanation of a condition, "
         "its course, treatment options and early warning signs, given to the "
         "patient and usually to the family too.",
    keyword="psychoeducation in Guntur",
    intro="Psychoeducation is the least dramatic thing in psychiatry and one "
          "of the most consistently useful: sitting down and explaining, "
          "properly, what the condition is, what it is not, what treatment is "
          "meant to do and what to watch for.",
    session="It is a structured explanation rather than a lecture, usually "
            "given to the patient and, with their agreement, to the family. It "
            "covers what the diagnosis means and what it does not, the usual "
            "course of the condition, what each part of the treatment is for, "
            "what side effects to expect and report, the early warning signs "
            "specific to this person, and what to do when those appear. "
            "Questions are the point of it, not an interruption.",
    suits=[
        "Almost every condition, as part of the consultation rather than a separate treatment",
        "Newly diagnosed patients and their families",
        "Conditions with a relapsing course, where catching the early signs matters",
        "Anyone who has been treated for years without a clear explanation of why",
    ],
    limits=[
        "Information alone does not treat a condition",
        "It works best repeated over time rather than delivered once",
        "It needs the patient's consent before family are involved",
    ],
    faqs=[
        ("Is this just being told what is wrong with me?",
         "It is closer to being given the map. Understanding what is "
         "happening tends to reduce fear, improve participation in treatment "
         "and make relapse easier to catch early — which is why it is treated "
         "as part of the care rather than as a courtesy."),
        ("Can my family attend?",
         "With your agreement, yes, and for several conditions it is actively "
         "recommended. Relatives who understand what they are seeing cope far "
         "better and respond more helpfully."),
        ("I was diagnosed years ago. Is it too late?",
         "No. People are often treated for a long time without ever having had "
         "the condition properly explained, and going through it afresh is "
         "frequently worthwhile."),
    ],
)

THERAPY_DETAIL["behavioural"] = dict(
    title="Behavioural Therapy in Guntur | Dr. M. Tirumala Babu",
    meta="Behavioural therapy in Guntur — changing what a person does rather "
         "than working first on thoughts. Used for depression, phobias, OCD "
         "and habit-related difficulties.",
    keyword="behavioural therapy in Guntur",
    intro="Behavioural therapy starts from what a person does rather than from "
          "what they think. Where avoidance, inactivity or a specific habit is "
          "what keeps a problem alive, changing the behaviour often shifts the "
          "thinking and the mood with it.",
    session="The work is concrete and planned. In depression it usually means "
            "graded re-engagement with activities that have dropped away, "
            "scheduled rather than waiting for motivation to return — because "
            "in depression it generally does not return first. In phobias and "
            "OCD it means planned, gradual contact with what is feared while "
            "deliberately not performing the avoidance or the ritual, at a "
            "pace you agree to in advance. Nothing is sprung on you.",
    suits=[
        "Depression where activity and interest have fallen away",
        "Phobias and panic, where avoidance has narrowed daily life",
        "OCD, as exposure and response prevention",
        "Habit-related difficulties with a clear behavioural pattern",
    ],
    limits=[
        "It requires doing the agreed tasks between sessions",
        "It is uncomfortable by design — the discomfort is part of how it works",
        "It is less suited to difficulties without a clear behavioural pattern",
        "It does not replace treatment of a severe underlying condition",
    ],
    faqs=[
        ("Will I be forced into a situation I fear?",
         "No. Exposure work is planned with you, starts well below the level "
         "that frightens you and only moves on when you are ready. Consent is "
         "part of the method, not a formality."),
        ("Why work on behaviour and not on the cause?",
         "Because what started a problem and what maintains it are often "
         "different things. Avoidance in particular keeps fear alive long "
         "after the original cause has gone."),
        ("Is this the same as CBT?",
         "It is closely related and often delivered together. CBT works on "
         "thoughts and behaviour; behavioural therapy concentrates on the "
         "behaviour, which for some difficulties is the more direct route."),
    ],
)

THERAPY_DETAIL["supportive"] = dict(
    title="Supportive Psychotherapy in Guntur | Dr. Tirumala Babu",
    meta="Supportive psychotherapy in Guntur — regular sessions focused on "
         "emotional support, problem-solving and keeping daily life going "
         "through a difficult period.",
    keyword="supportive psychotherapy in Guntur",
    intro="Not every difficulty calls for a specific technique. Supportive "
          "psychotherapy is regular, structured contact focused on getting "
          "through — emotional support, practical problem-solving, and keeping "
          "day-to-day functioning intact while something difficult is worked "
          "out or waited out.",
    session="Sessions are led more by what is happening in your life than by a "
            "protocol. Typical work includes talking through what has happened "
            "since the last session, problem-solving specific practical "
            "difficulties, strengthening the coping that already works for "
            "you, and keeping sleep, routine, work and relationships from "
            "coming apart while the main difficulty is addressed.",
    suits=[
        "Adjustment difficulties after a loss, a diagnosis or a major change",
        "Periods of high stress where the priority is getting through intact",
        "Long-term conditions, alongside other treatment",
        "People for whom a structured therapy is not currently appropriate or available",
    ],
    limits=[
        "It is not a specific treatment for a specific disorder",
        "Where a condition needs targeted treatment, this does not substitute for it",
        "Without a clear focus it can continue longer than it is useful — so it is reviewed",
    ],
    faqs=[
        ("Is this just talking?",
         "It is structured talking with a purpose: support, problem-solving "
         "and maintaining function. That is a legitimate treatment in its own "
         "right, particularly during a crisis or while someone is "
         "stabilising."),
        ("How long does it go on?",
         "For as long as it is useful, with regular review. Open-ended "
         "sessions that nobody reviews are a recognised way for therapy to "
         "drift, which is why review is built in."),
        ("Can I have this alongside medication?",
         "Yes. Supportive work is frequently used alongside medication rather "
         "than instead of it."),
    ],
)

THERAPY_DETAIL["motivational"] = dict(
    title="Motivational Interviewing in Guntur | Dr. Tirumala Babu",
    meta="Motivational interviewing in Guntur — a conversational approach for "
         "people who feel two ways about changing a behaviour, used in alcohol "
         "and tobacco dependence.",
    keyword="motivational interviewing in Guntur",
    intro="Most people who need to change a behaviour already know they should "
          "and feel two ways about it. Motivational interviewing works with "
          "that ambivalence instead of arguing against it, which turns out to "
          "be far more effective than being told what to do.",
    session="The conversation is deliberately not a lecture. It explores your "
            "own reasons for and against changing, in your words, without the "
            "clinician taking one side and pushing. Being argued at reliably "
            "produces defence of the behaviour; being asked what you make of "
            "it produces something else. The aim is that any decision to "
            "change is yours and therefore holds.",
    suits=[
        "Alcohol and tobacco dependence",
        "Other substance use, at the point where someone is unsure about stopping",
        "Lifestyle change where previous attempts have failed",
        "Anyone who has been told repeatedly to change and has stopped listening",
    ],
    limits=[
        "It does not manage withdrawal — that is a medical matter and comes first where relevant",
        "It is not a standalone treatment for a severe dependence",
        "It respects your decision, including a decision not to change yet",
    ],
    faqs=[
        ("Will I be lectured about my drinking?",
         "No. That approach reliably produces defensiveness and rarely "
         "produces change. The conversation is about your own view of it."),
        ("What if I am not sure I want to stop?",
         "That is the normal starting point and is precisely what this "
         "approach is designed for. Being unsure is not a reason to stay "
         "away."),
        ("Is this instead of other treatment?",
         "Usually alongside. Where withdrawal needs medical management, that "
         "is handled first — stopping some substances abruptly can be "
         "dangerous."),
    ],
)

THERAPY_DETAIL["stress"] = dict(
    title="Stress Management Therapy in Guntur | Dr. Tirumala Babu",
    meta="Stress management in Guntur — practical training in relaxation, "
         "breathing, routine and workload strategies, for stress-related "
         "difficulties, anxiety and somatic symptoms.",
    keyword="stress management therapy in Guntur",
    intro="Stress management is the practical end of psychiatric care: "
          "concrete training in relaxation, breathing, routine and workload, "
          "aimed at bringing down the physical arousal that sustained stress "
          "produces and building a daily structure that can actually be kept "
          "up.",
    session="The work is specific to your circumstances rather than generic "
            "advice. It typically covers breathing and relaxation methods "
            "practised until they are usable under pressure rather than only "
            "in a quiet room; sleep timing and what happens in the hour before "
            "bed; realistic workload and boundary-setting; the place of "
            "physical activity; and identifying the particular situations that "
            "reliably wind you up, with a plan for them.",
    suits=[
        "Stress-related difficulties that have not yet become a disorder",
        "Anxiety, alongside other treatment",
        "Somatic symptoms with a strong arousal component",
        "People whose work or family pressure is unlikely to change soon",
    ],
    limits=[
        "It does not remove the source of the stress",
        "It is not sufficient on its own for a moderate or severe disorder",
        "The methods need regular practice to be available when you need them",
    ],
    faqs=[
        ("Is this just being told to relax?",
         "No. Relaxation and breathing are trained methods that work when "
         "practised to the point of being usable under pressure. Being told to "
         "relax is not a treatment; learning how is."),
        ("My workload is not going to change. Is there any point?",
         "Yes. A large part of the work is about what you can control — sleep, "
         "routine, recovery, boundaries, physical arousal — which matters "
         "precisely when the workload itself is fixed."),
        ("Do I need medication as well?",
         "Often not. Stress on its own is generally managed without it. Where "
         "an anxiety disorder or depression has developed, that is a separate "
         "assessment."),
    ],
)

THERAPY_DETAIL["sleep"] = dict(
    title="Insomnia Therapy in Guntur | Behavioural Sleep Treatment",
    meta="Behavioural treatment for insomnia in Guntur — changes to sleep "
         "timing, environment and pre-sleep habits, usually tried before any "
         "medication for sleep is considered.",
    keyword="insomnia therapy in Guntur",
    intro="Behavioural treatment for insomnia is first-line — tried before "
          "medication rather than after it — and it is considerably more "
          "effective than most people expect, particularly for insomnia that "
          "has become self-sustaining.",
    session="The work starts with a sleep diary, because what people believe "
            "about their sleep and what the diary shows are often different. "
            "From there it covers consistent rise time (which matters more "
            "than bedtime), what happens in the hour before bed, what the bed "
            "is used for, what to do when you have been lying awake, caffeine "
            "and alcohol timing, and the anxiety about not sleeping that in "
            "chronic insomnia becomes the main thing keeping you awake.",
    suits=[
        "Persistent insomnia, particularly where it has outlasted its original cause",
        "Sleep difficulty within depression or anxiety, alongside treatment of those",
        "People wanting to reduce or stop long-term sleep medication, under supervision",
        "Anyone whose sleep problem has become a nightly source of dread",
    ],
    limits=[
        "It does not treat sleep apnoea, restless legs or other physical sleep disorders",
        "It usually gets worse before it gets better for a week or two",
        "It requires keeping to the agreed timing, which is the hard part",
    ],
    faqs=[
        ("Why not just take a sleeping tablet?",
         "Sleep medication has a place, usually short-term. Long-term use "
         "brings tolerance and difficulty stopping, and it does not address "
         "what is sustaining the insomnia — which is why behavioural treatment "
         "is first-line."),
        ("I snore and wake unrefreshed. Will this help?",
         "That pattern points more towards sleep apnoea, which is a physical "
         "condition needing different assessment and treatment. It is worth "
         "raising, because it is treatable."),
        ("Can I come off my sleeping tablets?",
         "Often, yes, but it is planned with the prescribing doctor and done "
         "gradually. Stopping some sleep medicines abruptly is not safe."),
    ],
)

THERAPY_DETAIL["social"] = dict(
    title="Social Skills Training in Guntur | Dr. Tirumala Babu",
    meta="Social skills training in Guntur — structured practice of "
         "conversation, everyday interaction and self-care, supporting a "
         "return to study, work and social life.",
    keyword="social skills training in Guntur",
    intro="Where a condition has eroded confidence or day-to-day functioning, "
          "the route back is usually practice rather than advice. Social "
          "skills training is structured, graded rehearsal of the ordinary "
          "interactions that study, work and social life are built from.",
    session="The work is broken down and rehearsed rather than discussed in "
            "the abstract: starting and holding a conversation, making and "
            "taking a phone call, asking for something, handling an interview "
            "or a first day back, managing everyday self-care and routine. "
            "Sessions use role-play and agreed practice outside, with the "
            "difficulty increasing only as each step becomes comfortable.",
    suits=[
        "Schizophrenia, where functioning has narrowed during or after an episode",
        "Autism spectrum disorder, alongside other support",
        "Social anxiety, alongside exposure work",
        "Anyone returning to study or work after a long period away",
    ],
    limits=[
        "It does not change someone's personality, and it is not meant to",
        "Progress is gradual and depends on practice outside sessions",
        "It does not substitute for treating the underlying condition",
    ],
    faqs=[
        ("Is this about becoming more outgoing?",
         "No. It is about having the practical skills available when you want "
         "them. Being quiet is a temperament, not a symptom, and this is not "
         "an attempt to change it."),
        ("Is it only for young people?",
         "No. It is used at any age, most often when someone is returning to "
         "work or study after a period away, or after an episode of illness."),
        ("Is it done in a group?",
         "It can be, and group practice has advantages. What is available "
         "depends on the clinic's arrangements at the time, which the "
         "consultation will tell you."),
    ],
)

THERAPY_DETAIL["relapse"] = dict(
    title="Relapse Prevention in Guntur | Dr. M. Tirumala Babu",
    meta="Relapse prevention in Guntur — identifying personal triggers and "
         "early warning signs and agreeing a plan for them, in substance use, "
         "bipolar disorder and recurrent depression.",
    keyword="relapse prevention in Guntur",
    intro="Relapse is rarely sudden. In most conditions it is preceded by "
          "signs that are consistent from episode to episode — and usually "
          "visible to the family before the person notices. Relapse prevention "
          "is the work of writing those down and agreeing in advance what "
          "happens when they appear.",
    session="Planning starts once the acute phase has settled, because it "
            "needs clear thinking. The work covers your own early warning "
            "signs, drawn from what actually happened last time rather than "
            "from a textbook list; the situations, people and states that "
            "raise your risk; what specifically will be done at each stage, "
            "and by whom; who to contact and how quickly; and — with your "
            "agreement — what the family's part is, since they often see it "
            "first.",
    suits=[
        "Substance use disorders, after withdrawal is complete",
        "Bipolar disorder, where episodes recur",
        "Recurrent depression",
        "Schizophrenia and psychosis, after an acute episode has settled",
    ],
    limits=[
        "It reduces risk; it does not guarantee that relapse will not happen",
        "It needs the plan to be written down and shared, not just discussed",
        "It works best with family involvement, which requires your consent",
    ],
    faqs=[
        ("Does a relapse mean the treatment failed?",
         "No. Relapse is part of the course of several conditions. It is "
         "treated as information about what the plan did not yet cover, not as "
         "a verdict on the person."),
        ("Why involve my family?",
         "Because they usually notice an early warning sign before you do — a "
         "change in sleep, in spending, in speed of speech. With your consent, "
         "that makes them the earliest useful alarm."),
        ("What does the plan actually look like?",
         "Something short and concrete: your specific early signs, what will "
         "be done at each stage, who to contact and how soon. Something that "
         "can be acted on in a difficult week, not a document."),
    ],
)
