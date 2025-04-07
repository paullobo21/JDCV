jd_parser_prompt = """
You are an expert in job description analysis. The input may contain multiple job descriptions.

Given the candidate's resume and job descriptions below, identify and extract the **most suitable job description** based on skill match, experience level, and overall fit.

Candidate Resume:
{cv_text}

Job Descriptions:
{jd_text}

From the best-fit job description, extract:
- Job Title
- Required Skills
- Responsibilities
- Education Requirements
- Experience Level

Make sure your response is structured and concise.
"""
