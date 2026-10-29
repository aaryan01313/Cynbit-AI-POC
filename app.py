import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
import PyPDF2

#API 
load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))
st.set_page_config(page_title="Cynbit Admissions Agent", page_icon="🏢", layout="centered")

hide_uploader_size = """
    <style>
    div[data-testid="stFileUploadDropzone"] small {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_uploader_size, unsafe_allow_html=True)

st.title("BitElevate Admissions Scorer")
st.markdown("Internal tool for Cynbit HR to automatically screen and route candidate profiles.")

uploaded_file = st.file_uploader("Upload Candidate Resume", type="pdf")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

if uploaded_file is not None:
    if uploaded_file.size > 10485760:
        st.error("File size is too huge please upload a short one.")
    else:
        st.success(f"File '{uploaded_file.name}' ready for analysis.")
        
        if st.button("Run AI Screening"):
            with st.spinner("Analyzing the resume..."):
                
                resume_text = extract_text_from_pdf(uploaded_file)
                
                prompt = f"""
                You are an internal AI Admissions Evaluator for Cynbit Technologies.
                We run a training program called "BitElevate" with tracks in:
                - Software Engineering (Full-stack, Cloud)
                - Digital Marketing & SEO
                
                Analyze the following candidate resume text and provide a concise JSON-like summary:
                1. Candidate Level (Beginner/Intermediate/Advanced)
                2. Recommended BitElevate Track
                3. Brief reasoning (2 sentences max)
                4. Match Score (out of 100 based on their tech skills fitting our tracks)
                
                Format the output neatly in Markdown.
                
                Resume Text:
                {resume_text}
                """
                
                try:
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt,
                    )
                    
                    st.markdown("### Screening Results")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"API Error: {e}")