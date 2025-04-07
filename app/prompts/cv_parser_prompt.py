cv_parser_prompt = """
You are an expert in resume analysis. Extract the following from the resume text of the candidate (if unavailable, label NA):
- Candidate Name
- Contact Information
- Skills
- Work Experience
- Education
- Certifications

Resume Text:
{cv_text}

Provide your response in a clear, structured format.
"""
