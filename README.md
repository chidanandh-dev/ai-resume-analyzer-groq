# 🚀 AI Resume Analyzer (Groq LLM Powered)

An AI-powered Resume Analysis System built using **Groq LLM (LLaMA models)**, Streamlit, and Python.

This application analyzes resumes semantically (not just keyword matching) and provides:

- 📊 ATS Score (0–100)
- 💪 Resume Strength Score
- 🛠 Skill Detection
- 🎯 Suitable Job Roles
- 📌 Task Recommendations
- 🚀 Career Improvement Suggestions
- 📄 Downloadable AI PDF Report

---

## 🧠 Powered By

- Groq LLM API
- LLaMA Models
- Python
- Streamlit
- NLP
- ReportLab
- dotenv (.env security)

---

## 📂 Project Structure

```
cv-task-analyzer/
│
├── app.py
├── utils.py
├── llm_analyzer.py
├── report_generator.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer-groq.git
cd ai-resume-analyzer-groq
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create .env File

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ Do NOT push your .env file to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User uploads resume (PDF or DOCX)
2. Text is extracted using pdfplumber/docx2txt
3. Resume text is sent to Groq LLM
4. LLM returns structured JSON output
5. Application displays:
   - ATS score
   - Resume score
   - Skills
   - Job roles
   - Task recommendations
6. PDF report is generated using ReportLab

---

## 🔐 Security

- API keys are stored securely using `.env`
- `.env` is excluded via `.gitignore`

---

## 🎯 Key Learning Outcomes

- LLM integration using Groq API
- Prompt engineering for structured outputs
- JSON parsing & validation
- AI application deployment
- PDF automation
- Streamlit UI development

---

## 📌 Future Improvements

- Job Description Matching
- Resume Chatbot
- Multi-model support
- Deployment on cloud
- User authentication system

---

## 👨‍💻 Author

**Chidanandh N A**  
AI Trainer | Data Science | Machine Learning | GenAI  

---

## 📜 License

MIT License
