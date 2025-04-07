from app.agents.cv_parser_agent import run_cv_parser
from app.agents.jd_parser_agent import run_jd_parser
from app.agents.validation_agent import run_validation
from app.agents.schedule_agent import run_schedule

def execute_agents(cv_text: str, jd_text: str):
    # Step 1: Parse CV
    parsed_cv = run_cv_parser(cv_text)

    # Step 2: Parse JD
    parsed_jd = run_jd_parser(jd_text, cv_text)

    # Step 3: Validate match
    validation_summary = run_validation(parsed_cv, parsed_jd)

    # Step 4: Suggest schedule (if match is good)
    interview_schedule = run_schedule(validation_summary)

    return {
        "parsed_cv": parsed_cv,
        "parsed_jd": parsed_jd,
        "validation_summary": validation_summary,
        "interview_schedule": interview_schedule
    }
