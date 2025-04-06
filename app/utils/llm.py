import asyncio
import httpx


async def compare_with_llm(resume_text: str, jd_text: str):
    prompt = f"""
    You are a resume screening assistant.
    Compare the following RESUME and JOB DESCRIPTION.
    - Give a match score out of 100
    - Highlight relevant skills
    - Suggest improvements

    --- RESUME ---
    {resume_text}

    --- JOB DESCRIPTION ---
    {jd_text}
    """

    # Send to Ollama (Gemma or LLaMA3)
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma:latest", "prompt": prompt, "stream": False}
        )
        data = response.json()
        return {"response": data.get("response")}
