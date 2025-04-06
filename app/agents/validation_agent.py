from app.llm.ollama_llm import call_ollama
from app.prompts.validation_prompt import validation_prompt

def run_validation(cv_info: str, jd_info: str):
    prompt = validation_prompt.format(cv_info=cv_info, jd_info=jd_info)
    return call_ollama(prompt)
