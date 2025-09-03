# --- AAT SYSTEM TEMPLATE ---
from multiprocessing.dummy.connection import Client


AAT_TEMPLATE = """
You are a professional migration agent drafting an Administrative Appeals Tribunal (AAT) submission letter
for a refused Student Visa (Subclass 500). Use a formal, respectful tone and keep structure tight.

Follow this structure exactly, filling in with applicant data where provided:

Administrative Appeals Tribunal
Migration & Refugee Division

State Office Address: {state_office_address}

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
GSS_TEMPLATE ="""
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


# --- ART SYSTEM TEMPLATE ---
ART_TEMPLATE = """
Administrative Appeals Tribunal Submission

Applicant: {applicant_name}
Date of Birth: {dob_art}
Address: {address}
Visa Applied For: {visa_applied_for}
Date of Application: {application_date}
Application ID: {application_id_art}
Transaction Reference: {transaction_reference}
File Number: {file_number}
Date of Refusal: {refusal_date}
Tribunal: Administrative Appeals Tribunal – Migration & Refugee Division

I act as the authorised representative for {applicant_name} in their application for review of the Department of Home Affairs’ refusal of their {visa_applied_for}. 
The refusal was issued on {refusal_date} on the basis that the delegate was not satisfied the applicant met the Genuine Temporary Entrant (GTE) requirement under clause 500.212 of Schedule 2 to the Migration Regulations 1994, having regard to Ministerial Direction No. 108.

We respectfully submit that the refusal decision was made in error, and upon a proper application of the law to the facts and evidence, the Tribunal should set aside the decision and substitute a decision to grant the visa.

Legal Framework
• Migration Act 1958 (Cth) – section 65 requires the decision-maker to grant a visa if satisfied that the prescribed criteria are met.
• Migration Regulations 1994 (Cth) – clause 500.212 requires that the applicant is a genuine temporary entrant.
• Ministerial Direction No. 108 – requires delegates to consider the applicant’s circumstances in their home country, circumstances in Australia, the value of the course, immigration history, and any other relevant matters.
• Relevant case law (e.g. Dhillon v Minister for Immigration and Border Protection [2016] FCA 1312; Singh v Minister for Home Affairs [2019] FCAFC 33) establishes that a decision-maker must consider all relevant evidence and provide clear reasoning.

Grounds of Appeal and Submissions

1. Applicant’s Circumstances in Home Country
{circumstances_home_country}

2. Circumstances in Australia
{circumstances_australia}

3. Value of the Course
{course_value}

4. Immigration History
{immigration_history}

5. Financial Capacity
{financial_capacity}

6. Family and Professional Ties to Home Country
{family_ties_home}

Conclusion
When applying the statutory framework correctly, the applicant meets the Genuine Temporary Entrant requirement under clause 500.212. 
The refusal decision failed to give proper weight to substantial evidence of:
• Family and economic ties to their home country.
• The academic and professional necessity of the proposed studies in Australia.
• Their financial capacity to fund their education and living costs.
• Their consistent long-term plan to return home after studies.

For these reasons, we respectfully request that the Tribunal set aside the refusal decision and substitute a decision to grant the {visa_applied_for}.

Yours faithfully,

{representative_name_art}
Authorised Representative
"""

# --- TOURIST VISA SYSTEM TEMPLATE ---
TOURIST_VISA_TEMPLATE = """
To:
Visa Officer
Australian Embassy {embassy_location}

Subject: Application for Tourist Visa (Subclass 600)

Applicants:
{applicants_list}

Dear Visa Officer,

I am writing to formally apply for a Tourist Visa (Subclass 600) for {applicants_short}, to visit Australia from {travel_start_date} to {travel_end_date}.

We intend to visit {family_relation} {family_member_name}, who is currently {family_member_status} in {family_member_location}. Our planned visit coincides with {special_occasions}, providing us with an opportunity to reunite as a family and spend meaningful time together. In addition, we plan to explore the cultural and tourist attractions of {planned_cities}.

Personal Background
{personal_background}

Detailed Travel Plan
{travel_plan}

Financial and Personal Commitments
{financial_capacity}

Personal Circumstances and Ties to {home_country}
{home_country_ties}

Supporting Documentation
To facilitate the processing of our visa applications, we have attached the following supporting documents:
{supporting_documents}

Conclusion
We kindly request your favourable consideration of our Tourist Visa (Subclass 600) applications. Our intention is solely to travel to Australia temporarily to visit family, celebrate special occasions, and explore Australia’s attractions. We are committed to complying with all visa conditions and returning to {home_country} at the end of our trip.

Should you require any additional information or documentation, please do not hesitate to contact me.

Thank you for your time and consideration.

Sincerely,

{primary_applicant_name}
"""



# --- GTE SYSTEM TEMPLATE (FULL FORMAT) ---
GTE_TEMPLATE = """
TO: The Department of Home Affairs
Sydney, Australia

Genuine Temporary Entrant (GTE) Letter for Australian Student Visa Application

I, {full_name}, born on {dob_gte} in {birth_place}, am writing to express my genuine intent to pursue {course_name} at {education_provider} in Australia. 
This letter accompanies my application for an Australian Student Visa, underscoring my commitment to enhancing my skills for future career and personal development, 
and to assert that my intentions align with the Genuine Temporary Entrant requirement.

Educational Background
{education_background}

Professional Background
{professional_experience}

Academic & Career Aspirations
{career_aspirations}

International Exposure and Motivation
{international_exposure}

Primary Objective of Study
{study_objective}

Reasons for Choosing Australia
{why_australia}

Reasons for Choosing {education_provider}
{why_institution}

Expected Outcomes from the Course
{expected_outcomes}

Financial Capacity
{financial_capacity}

Ties to Home Country
{family_ties}
{professional_commitments}
{community_engagement}

Conclusion
I assure you of my genuine intentions to comply with all visa conditions and to leave Australia upon completion of my studies. 
My ultimate goal is to contribute significantly to my field and to {home_country_gte}, leveraging the knowledge and skills acquired through my educational journey in Australia. 

Thank you for considering my application. 

Yours sincerely,  
{full_name}
"""
