import os
from flask import Flask, render_template, request, send_file
from docx import Document
from openai import OpenAI
from datetime import datetime
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# --- OpenAI client ---
# Prefer environment variable; fallback to literal only for local testing.
#OPENAI_API_KEY = os.getenv("")
client = OpenAI(api_key="")


cloudinary.config( 
    cloud_name = "dmze3pcjh", 
    api_key = "966861392574793", 
    api_secret = "al310I4Vz48f2URu2J1mTJab1Ko", 
    secure=True
)

# --- AAT SYSTEM TEMPLATE ---
AAT_TEMPLATE = """
You are a professional migration agent drafting an Administrative Appeals Tribunal (AAT) submission letter
for a refused Student Visa (Subclass 500). Use a formal, respectful tone and keep structure tight.

Follow this structure exactly, filling in with applicant data where provided:

Administrative Appeals Tribunal
Migration & Refugee Division
[State Office Address]

In reply quote:
Client Name: {client_name}
Date of Birth: {dob}
Application ID: {application_id}
File Number: {file_number}
Visa Subclass: Student Visa (Subclass 500)
Date of Refusal: {date_of_refusal}
Representative: {representative}
MARN: {marn}

RE: Submission in Support of Student Visa Review Application
Refusal Under Clauses 500.212, 500.213, 500.214, and 500.217 of Schedule 2 to the Migration Regulations 1994

Dear Tribunal Member,

I respectfully submit this statement on behalf of the applicant in support of their application for merits review before the Tribunal.
The applicant seeks review of a decision to refuse their Student visa (subclass 500) and maintains they meet all relevant criteria.

1. CLAUSE 500.212 – GENUINE STUDENT CRITERION
a) Circumstances in Home Country:
{home_country}

b) Circumstances in Australia:
{australia}

c) Value of the Course to Future:
{value_course}

d) Previous Study and Gaps:
{previous_study}

e) Immigration History:
{immigration_history}

f) Other Relevant Matters:
{other_matters}

2. CLAUSE 500.213 – ENGLISH LANGUAGE REQUIREMENT
Provide a concise, professional justification that the applicant meets English requirements under LIN 24/022
(e.g., valid test results with scores, packaged ELICOS where relevant, or an applicable exemption). Avoid placeholders.

3. CLAUSE 500.214 – CONFIRMATION OF ENROLMENT
Confirm the applicant has a valid current COE for a CRICOS-registered course (principal or packaged).
Clarify any previous deficiencies have been corrected with updated documentation.

4. CLAUSE 500.217 – FINANCIAL CAPACITY
Summarise evidence of tuition payments, savings, sponsor income, and any affidavits/statutory declarations,
linking them to the Department’s financial capacity framework.

Conclusion
Provide a professional concluding statement requesting that the Tribunal:
1) set aside the refusal decision; and
2) remit the matter to the Department with the finding that the visa criteria are satisfied.

Yours sincerely,

{representative}
Registered Migration Agent
MARN: {marn}
"""

# --- GSS SYSTEM TEMPLATE ---
GSS_TEMPLATE = """
You are a professional migration agent drafting a Genuine Student Statement (GSS) to support a Student Visa (Subclass 500) application.
Use a clear, persuasive, and truthful tone. Avoid placeholders; write full sentences.

Genuine Student Statement (GSS)

Client Name: {client_name_v1}
Date of Birth: {dob_v1}
Nationality: {nationality}
Passport Number: {passport_number}
Proposed Course: {course_name}
Education Provider: {education_provider}
Intended Start Date: {start_date}

1) BACKGROUND AND EDUCATION HISTORY
- Previous studies and timeline, including institutions and outcomes: {previous_study}
- Academic achievements, awards, notable projects or results: {academic_achievements}

2) REASONS FOR CHOOSING AUSTRALIA
- Why Australia offers the right academic, cultural, or industry environment for this course: {why_australia}
- Why not the home country or alternative destinations (costs, quality, outcomes): {why_not_home}
- Why this specific institution (curriculum, facilities, support, outcomes, location): {why_institution}

3) CAREER ASPIRATIONS AND FUTURE PLANS
- Explain how this course aligns with short/long-term career plans, roles, industries, and expected progression: {career_plans}

4) FINANCIAL CAPACITY
- Provide a succinct description of funding sources (savings, family support, loans, scholarships) and ability to cover tuition, living, and travel costs: {funding_sources}

5) FAMILY AND PERSONAL TIES
- Family ties and obligations in the home country and how they incentivize return: {family_ties}
- Additional incentives to return home after studies (career, business plans, assets, community): {return_home}

Conclusion
Provide a professional closing paragraph reinforcing genuine student intent, compliance with visa conditions, and intended return.

Yours sincerely,

{representative_v1}
Registered Migration Agent
MARN: {marn_v1}
"""

def get_form_value(form, key, default="[Not provided]"):
    """Safely get a field from request.form with a default."""
    return form.get(key, "").strip() or default

def build_data_for_aat(form):
    return {
        "client_name": get_form_value(form, "client_name"),
        "dob": get_form_value(form, "dob"),
        "application_id": get_form_value(form, "application_id"),
        "file_number": get_form_value(form, "file_number"),
        "date_of_refusal": get_form_value(form, "date_of_refusal"),
        "representative": get_form_value(form, "representative"),
        "marn": get_form_value(form, "marn"),
        "home_country": get_form_value(form, "home_country"),
        "australia": get_form_value(form, "australia"),
        "value_course": get_form_value(form, "value_course"),
        "previous_study": get_form_value(form, "previous_study"),
        "immigration_history": get_form_value(form, "immigration_history"),
        "other_matters": get_form_value(form, "other_matters"),
    }

def build_data_for_gss(form):
    return {
        "client_name_v1": get_form_value(form, "client_name_v1"),
        "dob_v1": get_form_value(form, "dob_v1"),
        "nationality": get_form_value(form, "nationality"),
        "passport_number": get_form_value(form, "passport_number"),
        "course_name": get_form_value(form, "course_name"),
        "education_provider": get_form_value(form, "education_provider"),
        "start_date": get_form_value(form, "start_date"),
        "previous_study": get_form_value(form, "previous_study"),
        "academic_achievements": get_form_value(form, "academic_achievements"),
        "why_australia": get_form_value(form, "why_australia"),
        "why_not_home": get_form_value(form, "why_not_home"),
        "why_institution": get_form_value(form, "why_institution"),
        "career_plans": get_form_value(form, "career_plans"),
        "funding_sources": get_form_value(form, "funding_sources"),
        "family_ties": get_form_value(form, "family_ties"),
        "return_home": get_form_value(form, "return_home"),
        "representative_v1": get_form_value(form, "representative_v1"),
        "marn_v1": get_form_value(form, "marn_v1"),
    }

def ask_gpt(system_prompt, user_content):
    """Call OpenAI Chat Completions API and return the text."""
    resp = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
    )
    return resp.choices[0].message.content

def save_docx(text, filename_prefix):
    """Save text to a .docx file with timestamp."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"{filename_prefix}_{ts}.docx"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], fname)

    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(output_path)
    return output_path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            template_type = request.form.get("template_type", "").strip().upper()
            if template_type not in ("AAT", "GSS"):
                return "Invalid template type selected. Choose AAT or GSS."

            if template_type == "AAT":
                data = build_data_for_aat(request.form)
                # Build prompt content by formatting the AAT template with data
                prompt_filled = AAT_TEMPLATE.format(**data)
                system_prompt = "You are an expert migration agent drafting formal AAT letters."
                letter_text = ask_gpt(system_prompt, prompt_filled)
                output_path = save_docx(letter_text, "AAT_submission")

            else:  # GSS
                data = build_data_for_gss(request.form)
                prompt_filled = GSS_TEMPLATE.format(**data)
                print(prompt_filled)  # Debugging line to check filled prompt
                system_prompt = "You are an expert migration agent writing Genuine Student Statements (GSS) for Subclass 500."
                letter_text = ask_gpt(system_prompt, prompt_filled)
                output_path = save_docx(letter_text, "GSS_statement")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            public_id = f"doc_{timestamp}"
            upload_result = cloudinary.uploader.upload(output_path,
                                           public_id=public_id, resource_type="raw")
            
            download_link, _ = cloudinary_url(
                upload_result["public_id"],
                resource_type="raw",
                flags="attachment"
            )
            print(download_link)
            # return send_file(output_path, as_attachment=True)
            return download_link

        except Exception as e:
            return f"Error: {str(e)}"

    # Render your dynamic frontend (make sure your templates/index.html matches the new fields)
    return render_template("index.html")

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
