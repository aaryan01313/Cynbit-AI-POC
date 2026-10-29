# AI Resume Screener & Role Matcher (PoC)

A streamlined Streamlit web application designed to automate the resume screening process for HR teams and technical recruiters. 

Instead of manually evaluating resumes, recruiters can upload a candidate's PDF. The AI agent extracts the text, analyzes the candidate's technical skills, suggests the best-fit job role or training track (e.g., Software Engineering, Data Science, Cloud), and generates a compatibility match score.

## Features
- **PDF Extraction:** Automatically extracts raw text from uploaded candidate resumes.
- **AI Screening:** Uses LLM to evaluate the candidate's proficiency level (Beginner/Intermediate/Advanced).
- **Smart Routing:** Recommends the ideal technical track based on extracted skills.
- **Match Score:** Generates a quantifiable match score out of 100.

## Tech Stack
- Python
- Streamlit (Frontend)
- Google GenAI SDK (gemini-3.8-flash)
- PyPDF2 (Data parsing)

## How to Run Locally
1. Clone this repo: `git clone https://github.com/aaryan01313/Cynbit-AI-POC.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your API key in a `.env` file like this: `API_KEY=your_key_here`
4. Run the app: `streamlit run app.py`
