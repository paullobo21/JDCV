from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.utils.extract_text import extract_text_from_file
from app.agents.agent_executor import execute_agents

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.post("/match/", response_class=HTMLResponse)
async def match_files(request: Request, cv: UploadFile = File(...), jd: UploadFile = File(...)):
    # Extract raw text from uploaded files
    cv_text = await extract_text_from_file(cv)
    jd_text = await extract_text_from_file(jd)

    # Run the full agent pipeline
    result = execute_agents(cv_text, jd_text)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "cv_text": cv_text,
        "jd_text": jd_text,
        "parsed_cv": result["parsed_cv"],
        "parsed_jd": result["parsed_jd"],
        "validation_summary": result["validation_summary"],
        "interview_schedule": result["interview_schedule"]
    })
