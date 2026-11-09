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


def extract_cv_text(uploaded_file):
    """Extract readable text from a PDF, DOCX, or TXT CV."""
    if uploaded_file is None:
        return ""

    file_bytes = uploaded_file.getvalue()
    extension = uploaded_file.name.rsplit(".", 1)[-1].lower()

    if extension == "pdf":
        reader = PdfReader(BytesIO(file_bytes))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        return "\n".join(pages).strip()

    if extension == "docx":
        document = Document(BytesIO(file_bytes))
        parts = [paragraph.text for paragraph in document.paragraphs]

        # Also extract text from tables, which are common in CV templates.
        for table in document.tables:
            for row in table.rows:
                parts.append(" | ".join(cell.text for cell in row.cells))

        return "\n".join(part for part in parts if part.strip()).strip()

    if extension == "txt":
        return file_bytes.decode("utf-8", errors="replace").strip()

    raise ValueError("Unsupported CV format. Please upload PDF, DOCX, or TXT.")


def generate_roadmap(field, level, duration, hours_per_week, goal, cv_text=""):
    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "Groq API key not found. Configure GROQ_API_KEY in your "
            "environment variables or Streamlit Secrets."
        )

    client = Groq(api_key=api_key)
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    system_prompt = 
