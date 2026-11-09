import os
from datetime import datetime

import streamlit as st
from groq import Groq
from pypdf import PdfReader
from docx import Document
from io import BytesIO

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🧭",
    layout="wide",
)

st.title("🧭 AI Learning Roadmap Generator")
st.write(
    "Generate a personalized, step-by-step learning roadmap based on your "
    "chosen field, current skill level, available time, and optionally your CV."
)

MAX_CV_SIZE_MB = 10


def get_api_key():
    """Read the Groq API key from Streamlit Secrets or an environment variable."""
    try:
        key = st.secrets.get("GROQ_API_KEY", "")
        if key:
            return key
    except Exception:
        pass
    return os.getenv("GROQ_API_KEY", "")

if st.button("🚀 Generate Roadmap", type="primary"):
    with st.spinner("Generating your learning roadmap..."):
        roadmap = generate_roadmap(
            field,
            skill_level,
            duration,
            weekly_hours,
            goal,
            cv_text
        )

    st.markdown("## Your Learning Roadmap")
    st.markdown(roadmap)

    st.download_button(
        label="📥 Download Roadmap",
        data=roadmap,
        file_name="learning_roadmap.md",
        mime="text/markdown"
    )

def generate_roadmap(field, level, duration, hours_per_week, goal, cv_text=""):
    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "Groq API key not found. Configure GROQ_API_KEY in your "
            "environment variables or Streamlit Secrets."
        )

    client = Groq(api_key=api_key)
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    system_prompt = """
You are an experienced learning-path designer, career-learning advisor,
and supportive teacher.

Create realistic, structured learning roadmaps for the user's chosen field.

Adapt the roadmap according to:
- Current skill level
- Available learning duration
- Weekly study hours
- Existing skills from the uploaded CV

If a CV is provided:
1. Identify existing technical skills.
2. Identify relevant educational background.
3. Identify practical experience.
4. Identify knowledge gaps.
5. Recommend topics that need improvement.

Do not repeat foundational topics unnecessarily.

Create realistic learning plans.
Do not promise guaranteed employment or mastery.

Use clear language, headings, and practical exercises.
Do not invent learning resources or URLs.
"""
