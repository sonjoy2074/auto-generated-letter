import os
from flask import Flask, render_template, request, send_file
from docx import Document
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from utils.templates import AAT_TEMPLATE, GSS_TEMPLATE, ART_TEMPLATE, TOURIST_VISA_TEMPLATE, GTE_TEMPLATE
from utils.helper import build_data_for_aat, build_data_for_gss, build_data_for_art, build_data_for_tourist_visa, build_data_for_gte
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

load_dotenv()
# --- OpenAI client ---
# Prefer environment variable; fallback to literal only for local testing.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

cloudinary.config( 
    cloud_name = "dmze3pcjh", 
    api_key = "966861392574793", 
    api_secret = "al310I4Vz48f2URu2J1mTJab1Ko", 
    secure=True
)

def ask_gpt(system_prompt, user_content):
    """Call OpenAI Chat Completions API and return the text."""
    resp = client.chat.completions.create(
        model="gpt-5-nano-2025-08-07",
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
            if template_type not in ("AAT", "GSS", "GTE", "ART", "TOURIST_VISA"):
                return "Invalid template type selected. Choose from AAT, GSS, GTE, ART, or TOURIST_VISA."

            if template_type == "AAT":
                data = build_data_for_aat(request.form)
                # Build prompt content by formatting the AAT template with data
                prompt_filled = AAT_TEMPLATE.format(**data)
                system_prompt = (
                    "You are an Australian registered migration agent drafting a legal submission "
                    "for the Administrative Appeals Tribunal (AAT). "
                    "Use precise legal terminology, reference relevant sections of the Migration Act 1958, "
                    "Migration Regulations 1994, and Ministerial Directions (e.g., No. 108). "
                    "Ensure the tone is formal, persuasive, and compliant with Tribunal expectations."
                )
                letter_text = ask_gpt(system_prompt, prompt_filled)
                output_path = save_docx(letter_text, "AAT_submission")
            # elif template_type == "GTE":
            #     data = build_data_for_gte(request.form)
            #     prompt_filled = GTE_TEMPLATE.format(**data)
            #     system_prompt = (
            #         "You are an Australian registered migration agent drafting a Genuine Temporary Entrant (GTE) statement "
            #         "for a Student Visa (Subclass 500) application. "
            #         "Use precise legal and regulatory references, including clause 500.212 of Schedule 2 to the Migration Regulations 1994, "
            #         "section 65 of the Migration Act 1958, and Ministerial Direction No. 108. "
            #         "Ensure the tone is formal, truthful, and persuasive, clearly addressing all GTE factors: "
            #         "home country circumstances, potential circumstances in Australia, the value of the course, "
            #         "immigration history, and other relevant matters."
            #     )
            #     letter_text = ask_gpt(system_prompt, prompt_filled)
            #     output_path = save_docx(letter_text, "GTE_submission")
            elif template_type == "GSS":
                data = build_data_for_gss(request.form)
                print(type(data))  # Debugging line to check data structure
                prompt_filled = GSS_TEMPLATE.format(**data)
                print(prompt_filled)  # Debugging line to check filled prompt
                system_prompt = (
                    "You are an Australian registered migration agent drafting a Genuine Student Statement (GSS) "
                    "to support a Student Visa (Subclass 500) application. "
                    "Frame the statement in line with the Genuine Temporary Entrant (GTE) requirement under clause 500.212 "
                    "of Schedule 2 to the Migration Regulations 1994 and Ministerial Direction No. 108. "
                    "Ensure the tone is clear, persuasive, and compliant with Department of Home Affairs expectations, "
                    "while highlighting academic progression, financial capacity, and incentives to return home."
                )
                letter_text = ask_gpt(system_prompt, prompt_filled)
                output_path = save_docx(letter_text, "GSS_statement")
            elif template_type == "ART":
                data = build_data_for_art(request.form)
                prompt_filled = ART_TEMPLATE.format(**data)
                system_prompt = (
                    "You are an Australian registered migration agent preparing a Tribunal review submission (ART) "
                    "for the Administrative Appeals Tribunal (Migration & Refugee Division). "
                    "Use a highly formal, legally persuasive tone and reference the Migration Act 1958, "
                    "Migration Regulations 1994 (particularly clause 500.212), "
                    "Ministerial Direction No. 108, and relevant Federal Court precedents. "
                    "Ensure the submission demonstrates procedural fairness, correct application of law, "
                    "and argues why the refusal should be set aside and substituted with a grant."
                )

                letter_text = ask_gpt(system_prompt, prompt_filled)
                output_path = save_docx(letter_text, "ART_submission")
            elif template_type == "TOURIST_VISA":
                data = build_data_for_tourist_visa(request.form)
                prompt_filled = TOURIST_VISA_TEMPLATE.format(**data)
                system_prompt = (
                    "You are an Australian registered migration agent drafting a Tourist Visa"
                    "application support letter. "
                    "Ensure the letter addresses the Genuine Temporary Entrant requirement under clause 600.211 "
                    "of Schedule 2 to the Migration Regulations 1994, "
                    "and compliance with visa conditions under section 41 of the Migration Act 1958. "
                    "Use a respectful, formal tone while demonstrating strong ties to the home country, "
                    "financial capacity, and the temporary nature of the visit."
                )
                letter_text = ask_gpt(system_prompt, prompt_filled)
                output_path = save_docx(letter_text, "Tourist_Visa_submission")
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
