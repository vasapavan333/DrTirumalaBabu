"""Telugu for the navigation, headings and the safety-critical lines.

Scope, and why it stops where it does
-------------------------------------
Most patients in Guntur read Telugu more comfortably than English. What is
translated here is the layer that helps someone find their way around and get
help: the menu, every section heading, the footer, the emergency numbers and
the appointment wording.

The clinical body copy is deliberately **not** translated. Machine-translating
"do not stop drinking suddenly — this can cause seizures" is a real-world
risk, and none of the English has been reviewed by the doctor yet either.
Those paragraphs need a Telugu speaker who is also comfortable with the
clinical content — ideally Dr. Tirumala Babu himself.

Adding a translation later
--------------------------
Every string below renders as a `<span class="te" lang="te">` under its
English original, the same treatment the condition cards already use. To
extend the translation, add keys here and reference them from
tools/build_pages.py; nothing else has to change.

Wording is taken from the clinic's own posters wherever they cover a term,
because that phrasing is what patients in Guntur already recognise.
"""

# --------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------

NAV = {
    "Home": "ముఖ్య పేజీ",
    "About": "డాక్టర్ గురించి",
    "About Doctor": "డాక్టర్ గురించి",
    "Services": "సేవలు",
    "Conditions": "సమస్యలు",
    "Therapies": "చికిత్సా విధానాలు",
    "Contact": "సంప్రదించండి",
    "How It Works": "ఎలా జరుగుతుంది",
}

BOOK = "అపాయింట్‌మెంట్ బుక్ చేయండి"
INSTAGRAM = "ఇన్‌స్టాగ్రామ్‌లో ఫాలో అవ్వండి"

ALL_OF = {
    "services": "అన్ని సేవలు",
    "conditions": "అన్ని సమస్యలు",
    "therapies": "అన్ని చికిత్సలు",
}

# --------------------------------------------------------------------------
# Footer
# --------------------------------------------------------------------------

FOOTER = {
    "Explore": "పేజీలు",
    "Contact": "సంప్రదించండి",
    "Urgent help": "అత్యవసర సహాయం",
}

# --------------------------------------------------------------------------
# Section headings, keyed by the English heading the build emits.
# A heading with no entry here simply renders without a Telugu line.
# --------------------------------------------------------------------------

HEADINGS = {
    # condition pages
    "Signs and symptoms": "లక్షణాలు",
    "Causes and risk factors": "కారణాలు",
    "When to consult a psychiatrist": "ఎప్పుడు వైద్యుడిని కలవాలి",
    "Treatment and management": "చికిత్స",
    "Approaches that may form part of treatment": "మందులు కాకుండా ఇతర చికిత్సలు",
    "Non-pharmacological approaches": "మందులు కాకుండా ఇతర చికిత్సలు",
    # therapy pages
    "What it is": "ఇది ఏమిటి",
    "What a session involves": "సెషన్‌లో ఏమి జరుగుతుంది",
    "Who it tends to suit": "ఎవరికి సరిపోతుంది",
    "What it does not do": "ఇది చేయనిది",
    "Conditions this is used in": "ఏ సమస్యలకు ఉపయోగిస్తారు",
    "Therapies offered here": "ఇక్కడ అందించే చికిత్సలు",
    "Approaches that may be recommended or referred": "సిఫార్సు లేదా రెఫరల్ ద్వారా",
    "Non-pharmacological therapies": "మందులు కాకుండా ఇతర చికిత్సలు",
    # index pages
    "Conditions we assess and treat": "మేము చికిత్స చేసే సమస్యలు",
    "Reading a list is not a diagnosis": "జాబితా చదవడం నిర్ధారణ కాదు",
    # shared
    "Frequently asked questions": "తరచుగా అడిగే ప్రశ్నలు",
    # the hand-written pages
    "Your mental health deserves care and understanding": "మీ మానసిక ఆరోగ్యం ముఖ్యం",
    "Meet Dr. Tirumala Babu": "డాక్టర్ గురించి",
    "Psychiatric care for your mental well-being": "మానసిక ఆరోగ్య సంరక్షణ",
    "Services offered at the clinic": "క్లినిక్‌లో అందించే సేవలు",
    "What a consultation looks like": "సంప్రదింపు ఎలా జరుగుతుంది",
    "Visit the clinic": "క్లినిక్‌కు రండి",
    "Take the first step toward better mental health": "మొదటి అడుగు వేయండి",
    "Send an appointment enquiry": "అపాయింట్‌మెంట్ కోసం సందేశం",
}

# Category headings on conditions.html, keyed by category id.
CATEGORY = {
    "mental-health": "మానసిక సమస్యలు",
    "neuro-cognitive": "నాడీ &amp; జ్ఞాపకశక్తి సమస్యలు",
    "de-addiction": "వ్యసన విముక్తి",
    "psychosomatic": "శృంగార &amp; శారీరక-మానసిక ఆరోగ్యం",
}

# Eyebrows — the small uppercase label above a heading.
EYEBROW = {
    "Appointments": "అపాయింట్‌మెంట్లు",
    "Symptoms": "లక్షణాలు",
    "Treatment": "చికిత్స",
    "Causes": "కారణాలు",
    "Therapies": "చికిత్సా విధానాలు",
    "Conditions": "సమస్యలు",
    "Services": "సేవలు",
    "Questions": "ప్రశ్నలు",
}

# --------------------------------------------------------------------------
# The safety-critical line. The phone numbers carry the meaning here, so they
# are repeated as links rather than written into the sentence — a number a
# reader cannot tap is no use in an emergency.
# --------------------------------------------------------------------------

EMERGENCY = (
    "తక్షణ ప్రమాదం ఉంటే అపాయింట్‌మెంట్ కోసం వేచి ఉండకండి. "
    "అత్యవసర సేవలకు {emergency}, అంబులెన్స్ కోసం {ambulance}. "
    "ఉచిత మానసిక ఆరోగ్య సహాయం కోసం టెలీ-మానస్ {telemanas}."
)

# The line under the appointment band.
APPOINTMENT = (
    "సోమవారం నుండి శనివారం, సాయంత్రం 6:00 – రాత్రి 9:00. "
    "అపాయింట్‌మెంట్ కోసం క్లినిక్‌కు కాల్ చేయండి."
)
