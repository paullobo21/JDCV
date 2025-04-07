schedule_prompt = """
Given the candidate’s validation summary, determine whether to proceed with scheduling an interview.

Validation Summary:
{validation_summary}

If yes, suggest:
- Interview Type (Technical/HR/etc.)
- Preferred Date and Time (suggest one)
- Interviewer's Role

Format your response in a short, structured paragraph.
"""
