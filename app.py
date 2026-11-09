
import os
from datetime import datetime

import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🧭",
    layout="wide",
)

st.title("🧭 AI Learning Roadmap Generator")
st.write(
    "Create a practical, step-by-step learning plan based on your subject, "
    "current skill level, and available time."
)

# Read the API key from Streamlit Secrets (deployment) or environment variables (local).
def get_api_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return os.getenv("GROQ_API_KEY")


def generate_roadmap(field, level, duration, hours_per_week, goal):
    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "Groq API key not found. Add GROQ_API_KEY to your .env/environment "
            "or Streamlit Secrets."
        )

    client = Groq(api_key=api_key)

    system_prompt = """
You are an experienced learning-path designer and supportive teacher.
Create realistic, well-organized learning roadmaps for the user's stated subject.
Adapt the depth and terminology to the learner's current skill level and time.
Do not pretend the learner can master a large field in an unrealistically short time.
If the timeline is too short, explain what can reasonably be achieved.
Use clear Markdown headings, tables where useful, and beginner-friendly language.
Include practical exercises and projects, not only theory.
Recommend reputable, freely accessible learning resources by name and official URL
when you know them confidently. Never invent URLs. If unsure, give resource names
without a URL.
"""

    user_prompt = f"""
Create a personalized learning roadmap with these details:

Field / domain: {field}
Current skill level: {level}
Available learning duration: {duration}
Study time: {hours_per_week} hours per week
Main goal: {goal or "Build strong practical knowledge"}

Structure the response in this order:

1. Roadmap overview and realistic expected outcome
2. Prerequisites
3. Learning phases in chronological order
   - Duration
   - Topics
   - Simple explanations
   - Practice tasks
   - Completion checkpoints
4. Weekly study schedule
5. Practical projects
6. Recommended tools and software
7. Learning resources
8. Progress assessment and next steps

Make the timeline fit the user's available duration.
Clearly label optional topics.
Avoid vague advice. Name the actual topics.
"""
