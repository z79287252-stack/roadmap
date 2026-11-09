
AI Learning Roadmap Generator
An AI-powered Streamlit application that creates a step-by-step learning roadmap for any subject or domain.

Users provide:

Learning field or domain
Current skill level: Beginner, Intermediate, or Advanced
Available learning duration
Weekly study hours
Optional learning goal
The app uses the Groq API to generate a practical roadmap with learning phases, weekly planning, projects, checkpoints, and learning resources.

Tech Stack
Python 3.10+
Streamlit
Groq Python SDK
Groq chat completion model: llama-3.3-70b-versatile
Project Structure
learning-roadmap-generator/
├── app.py
├── requirements.txt
└── README.md
1. Clone the repository
After creating a new repository on GitHub, clone it:

git clone https://github.com/YOUR-USERNAME/learning-roadmap-generator.git
cd learning-roadmap-generator
Copy the three project files into this folder.

2. Create a virtual environment
Windows:

python -m venv venv
venv\Scripts\activate
macOS / Linux:

python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure your Groq API key
Create an API key in the Groq Console.

For local development, set an environment variable in your terminal.

PowerShell:

$env:GROQ_API_KEY="your_actual_groq_api_key"
Command Prompt:

set GROQ_API_KEY=your_actual_groq_api_key
macOS / Linux:

export GROQ_API_KEY="your_actual_groq_api_key"
Do not paste your API key into app.py, commit it to GitHub, or share it publicly.

5. Run the application
streamlit run app.py
Streamlit will show a local address in your terminal, usually http://localhost:8501.

6. Push the project to GitHub
Run these commands from the project folder:

git init
git add app.py requirements.txt README.md
git commit -m "Build AI learning roadmap generator"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/learning-roadmap-generator.git
git push -u origin main
Replace YOUR-USERNAME with your GitHub username. If you cloned an existing repository in step 1, you usually only need git add, git commit, and git push.

7. Deploy on Streamlit Community Cloud
Push the project to GitHub.
Open Streamlit Community Cloud and sign in with GitHub.
Choose Create app and select your repository, branch, and app.py.
Open the app's Advanced settings / Secrets section.
Add your key in TOML format:
GROQ_API_KEY = "your_actual_groq_api_key"
Deploy the app.
Never add the real key to this README or to a committed file.

How it works
Streamlit collects the learner's preferences.
The app reads the Groq API key from Streamlit Secrets or an environment variable.
The Groq SDK sends the learning requirements to the selected chat model.
The generated Markdown roadmap appears in the app.
The learner can download the roadmap as a .md file.
Notes
AI-generated roadmaps can contain errors. Check important course details, certification requirements, and resource links.
The selected model must be available to your Groq account. If Groq changes model availability, update the model value in app.py to a currently supported chat model.
Keep your API key private.
