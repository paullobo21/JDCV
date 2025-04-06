from app.agents.agent_executor import execute_agents

def get_match_result(cv_text: str, jd_text: str):
    result = execute_agents(cv_text, jd_text)
    return result
