def get_form_value(form, key, default="[Not provided]"):
    """Safely get a field from request.form with a default."""
    return form.get(key, "").strip() or default

def build_data_for_aat(form):
    return {
        "Subclass": get_form_value(form, "subclass"),
        "state_office_address": get_form_value(form, "state_office_address"),
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
        "english_language": get_form_value(form, "english_language"),
        "confirmation_of_enrolment": get_form_value(form, "confirmation_of_enrolment"),
        "financial_capacity": get_form_value(form, "financial_capacity"),
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
def build_data_for_art(form):
    return {
        "applicant_name": get_form_value(form, "applicant_name"),
        "dob_art": get_form_value(form, "dob_art"),
        "address": get_form_value(form, "address"),
        "visa_applied_for": get_form_value(form, "visa_applied_for"),
        "application_date": get_form_value(form, "application_date"),
        "application_id_art": get_form_value(form, "application_id_art"),
        "transaction_reference": get_form_value(form, "transaction_reference"),
        "file_number": get_form_value(form, "file_number"),
        "refusal_date": get_form_value(form, "refusal_date"),
        "circumstances_home_country": get_form_value(form, "circumstances_home_country"),
        "circumstances_australia": get_form_value(form, "circumstances_australia"),
        "course_value": get_form_value(form, "course_value"),
        "immigration_history": get_form_value(form, "immigration_history"),
        "financial_capacity": get_form_value(form, "financial_capacity"),
        "family_ties_home": get_form_value(form, "family_ties_home"),
        "representative_name_art": get_form_value(form, "representative_name_art"),
    }

def build_data_for_tourist_visa(form):
    return {
        "embassy_location": get_form_value(form, "embassy_location"),
        "subclass_tv": get_form_value(form, "subclass_tv"),
        "applicants_list": get_form_value(form, "applicants_list"),  
        "applicants_short": get_form_value(form, "applicants_short"),
        "travel_start_date": get_form_value(form, "travel_start_date"),
        "travel_end_date": get_form_value(form, "travel_end_date"),
        "family_relation": get_form_value(form, "family_relation"),  
        "family_member_name": get_form_value(form, "family_member_name"),
        "family_member_status": get_form_value(form, "family_member_status"),
        "family_member_location": get_form_value(form, "family_member_location"),
        "special_occasions": get_form_value(form, "special_occasions"),
        "planned_cities": get_form_value(form, "planned_cities"),
        "personal_background": get_form_value(form, "personal_background"),
        "travel_plan": get_form_value(form, "travel_plan"),
        "financial_capacity": get_form_value(form, "financial_capacity"), 
        "home_country": get_form_value(form, "home_country"),
        "home_country_ties": get_form_value(form, "home_country_ties"),
        "supporting_documents": get_form_value(form, "supporting_documents"),  
        "primary_applicant_name": get_form_value(form, "primary_applicant_name")
    }

# def build_data_for_gte(form):
#     return{
#         "full_name": get_form_value(form, "full_name"),
#         "dob_gte": get_form_value(form, "dob_gte"),
#         "birth_place": get_form_value(form, "birth_place"),
#         "course_name": get_form_value(form, "course_name"),
#         "education_provider": get_form_value(form, "education_provider"),
#         "education_background": get_form_value(form, "education_background"),
#         "professional_experience": get_form_value(form, "professional_experience"),
#         "career_aspirations": get_form_value(form, "career_aspirations"),
#         "international_exposure": get_form_value(form, "international_exposure"),
#         "study_objective": get_form_value(form, "study_objective"),
#         "why_australia": get_form_value(form, "why_australia"),
#         "education_provider": get_form_value(form, "education_provider"),
#         "why_institution": get_form_value(form, "why_institution"),
#         "expected_outcomes": get_form_value(form, "expected_outcomes"),
#         "financial_capacity": get_form_value(form, "financial_capacity"),
#         "family_ties": get_form_value(form, "family_ties"),
#         "professional_commitments": get_form_value(form, "professional_commitments"),
#         "community_engagement": get_form_value(form, "community_engagement"),
#         "home_country_gte": get_form_value(form, "home_country_gte")
#     }