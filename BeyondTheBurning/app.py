from flask import Flask, render_template, request, redirect, url_for
from content import PAGES, SOURCES, EVIDENCE_LABELS, SURVEY_URL, get_page

app = Flask(__name__)

app.secret_key = 'top-secret'

# Choices for the dropdowns and checkboxes on the exposure report form
LOCATIONS = ["Minneapolis, MN", "St. Paul, MN", "Elsewhere in Minnesota", "Outside Minnesota"]
AGENTS = ["Tear gas", "Pepper spray", "Pepper balls", "Not sure"]
SYMPTOMS = {
    "breathing": "Coughing, wheezing, or trouble breathing",
    "eyes": "Burning eyes or blurry vision",
    "skin": "Skin burning, rash, or blisters",
    "menstrual": "Menstrual changes or cramping",
    "headache": "Headache, nausea, or dizziness",
    "anxiety": "Anxiety, stress, or trouble sleeping",
}

# Reports are only kept in memory (like the class demo), so they reset when the app restarts
reports = []


# Makes these variables available in every template (used by the nav bar in base.html)
@app.context_processor
def site_globals():
    return {"pages": PAGES, "survey_url": SURVEY_URL}


# Page 1: Homepage
@app.route('/')
def index():
    return render_template('home.html', report_count=len(reports))


# Pages 2-7: topic pages (Understanding, Respiratory, Reproductive, Long-Term, Vulnerable, Care)
@app.route('/topic/<slug>')
def topic(slug):
    page = get_page(slug)
    if page is None:
        return render_template('notFound.html'), 404
    return render_template('topic.html', page=page, sources=SOURCES, labels=EVIDENCE_LABELS)


# Page 8: Research library
@app.route('/research')
def research():
    return render_template('research.html', sources=SOURCES)


# Old link style from the ChatGPT outline: /library sends people to /research
@app.route('/library')
def library():
    return redirect(url_for('research'))


# Minneapolis community survey page
@app.route('/minneapolis')
def minneapolis():
    return render_template('minneapolis.html')


# Form page: exposure report (GET shows the form, POST processes it)
@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        location = request.form.get('location', '').strip()
        agent = request.form.get('agent', '').strip()
        days = request.form.get('days', '').strip()
        symptoms = request.form.getlist('symptoms')   # several checkboxes share one name
        details = request.form.get('details', '').strip()
        medical_care = request.form.get('medical_care') == "yes"  # True if checked

        # Validation
        if not name or not email or not location or not agent or not days:
            error = "Please fill in all required fields"
            return render_template('reportForm.html', error=error, form=request.form,
                                   locations=LOCATIONS, agents=AGENTS, symptom_choices=SYMPTOMS)

        if not days.isdigit() or not 1 <= int(days) <= 30:
            error = "Days exposed must be a number from 1 to 30"
            return render_template('reportForm.html', error=error, form=request.form,
                                   locations=LOCATIONS, agents=AGENTS, symptom_choices=SYMPTOMS)

        reports.append({"location": location, "agent": agent, "days": int(days)})

        return render_template(
            'reportSuccess.html',
            name=name,
            email=email,
            location=location,
            agent=agent,
            days=int(days),
            symptoms=[SYMPTOMS[s] for s in symptoms if s in SYMPTOMS],
            symptom_keys=symptoms,
            details=details,
            medical_care=medical_care
        )

    return render_template('reportForm.html', form={}, locations=LOCATIONS, agents=AGENTS,
                           symptom_choices=SYMPTOMS)
