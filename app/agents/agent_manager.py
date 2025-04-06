from app.agents.cv_parser_agent import run_cv_parser
from app.agents.jd_parser_agent import run_jd_parser
from app.agents.validation_agent import run_validation
from app.agents.schedule_agent import run_schedule

async def process_with_agents(cv_text: str, jd_text: str) -> dict:
    # Step 1: Parse CV
    parsed_cv = await run_cv_parser(cv_text)

    # Step 2: Parse JD
    parsed_jd = await run_jd_parser(jd_text)

    # Step 3: Validate compatibility
    validation_feedback = await run_validation(parsed_cv, parsed_jd)

    # Step 4: Schedule interview if suitable
    interview_plan = await run_schedule(parsed_cv, parsed_jd)

    return {
        "parsed_cv": parsed_cv,
        "parsed_jd": parsed_jd,
        "validation_feedback": validation_feedback,
        "interview_plan": interview_plan
    }
