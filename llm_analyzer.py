import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text):

    prompt = f"""
You are an expert AI Resume Analyzer.

Analyze this resume and return ONLY valid JSON.

Resume:
{resume_text}

Return in this JSON format:

{{
    "ats_score": number between 0-100,
    "resume_score": number between 0-100,
    "skills": ["skill1", "skill2"],
    "job_roles": ["role1", "role2"],
    "tasks": ["task1", "task2"],
    "recommendations": "detailed career advice"
}}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        content = response.choices[0].message.content

        # Remove possible markdown formatting
        content = content.replace("```json", "").replace("```", "").strip()

        return json.loads(content)

    except Exception as e:
        return f"❌ LLM Error or JSON Parsing Failed: {str(e)}"
