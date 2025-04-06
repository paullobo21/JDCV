from app.agents.job_description_agent import JobDescriptionSummarizerAgent
from app.agents.cv_parser_agent import CVParserAgent
from app.agents.matching_agent import MatchingAgent
from app.agents.interview_scheduler_agent import InterviewSchedulerAgent

class AgentCoordinator:
    def __init__(self):
        self.jd_agent = JobDescriptionSummarizerAgent()
        self.cv_agent = CVParserAgent()
        self.match_agent = MatchingAgent()
        self.schedule_agent = InterviewSchedulerAgent()

    def run(self, jd_text, cv_text):
        jd_summary = self.jd_agent.summarize(jd_text)
        cv_profile = self.cv_agent.extract_profile(cv_text)
        match_result = self.match_agent.calculate_match(jd_summary, cv_profile)
        schedule_result = self.schedule_agent.schedule(match_result)

        return {
            "jd_summary": jd_summary,
            "cv_profile": cv_profile,
            "match_result": match_result,
            "schedule_result": schedule_result
        }
