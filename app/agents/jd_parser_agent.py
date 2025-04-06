from app.llm.ollama_llm import call_ollama
from app.prompts.jd_parser_prompt import jd_parser_prompt

def run_jd_parser(jd_text: str, cv_text: str):
    prompt = jd_parser_prompt + f"\n\nCandidate Resume:\n{cv_text}\n\nJob Descriptions:\n{jd_text}"
    return call_ollama(prompt)
