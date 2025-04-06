from app.llm.ollama_llm import call_ollama
from app.prompts.schedule_prompt import schedule_prompt

def run_schedule(validation_summary: str):
    prompt = schedule_prompt.format(validation_summary=validation_summary)
    return call_ollama(prompt)
