import streamlit as st
from utils import extract_text
from llm_analyzer import analyze_resume
from report_generator import generate_pdf

st.set_page_config(page_title="AI Resume Task Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer (LLM Powered)")
st.write("Upload your CV and get AI-powered career insights.")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    resume_text = extract_text(uploaded_file)

    if resume_text.strip() == "":
        st.error("Could not extract text from resume.")
    else:
        st.subheader("📄 Extracted Resume Text")
        st.text_area("Resume Content", resume_text, height=200)

        if st.button("Analyze Resume"):
            with st.spinner("Analyzing with AI..."):
                result = analyze_resume(resume_text)

            if isinstance(result, dict):

                st.subheader("📊 ATS Score")
                st.progress(result["ats_score"] / 100)
                st.write(f"**ATS Score:** {result['ats_score']}/100")

                st.subheader("💪 Resume Strength Score")
                st.progress(result["resume_score"] / 100)
                st.write(f"**Resume Strength Score:** {result['resume_score']}/100")

                st.subheader("🛠 Detected Skills")
                st.write(result["skills"])

                st.subheader("🎯 Suitable Job Roles")
                st.write(result["job_roles"])

                st.subheader("📌 Tasks Candidate Can Perform")
                st.write(result["tasks"])

                st.subheader("🚀 Career Recommendations")
                st.write(result["recommendations"])

                pdf_file = generate_pdf(result)

                with open(pdf_file, "rb") as f:
                    st.download_button(
                        label="📥 Download Full AI Report (PDF)",
                        data=f,
                        file_name="AI_Resume_Report.pdf",
                        mime="application/pdf"
                    )

            else:
                st.error(result)
