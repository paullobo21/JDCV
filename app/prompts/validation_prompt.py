validation_prompt = """
Based on the parsed resume and job description below, evaluate the candidate's fit for the job.

Parsed Resume:
{cv_info}

Parsed Job Description:
{jd_info}

Include:
- Skill Match %
- Experience Relevance
- Overall Suitability (High/Medium/Low)

Be concise and structured.
"""
