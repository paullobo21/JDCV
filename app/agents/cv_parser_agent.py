from app.llm.ollama_llm import call_ollama
from app.prompts.cv_parser_prompt import cv_parser_prompt

def run_cv_parser(cv_text: str):
    prompt = cv_parser_prompt.format(cv_text=cv_text)
    return call_ollama(prompt)
