 AI-Powered Resume & Job Description Matcher

This project is a FastAPI-based web application that intelligently matches resumes (CVs) with job descriptions (JDs) using locally hosted LLMs via Ollama. It includes multiple agents for parsing, validation, scheduling, and future shortlisting—all built for streamlined and automated candidate screening.

 **Features**

- 📄 Upload resumes (PDF) and job descriptions (CSV)
- 🤖 CV & JD parsing using custom LLM prompts
- ✅ Validation agent for evaluating fit (skills, experience, suitability)
- 📅 Automated interview scheduling suggestions
- 🧠 Built-in LLM support using **Ollama** (Mistral by default)
- 📊 Results displayed clearly via HTML templates
- ⚙️ Extensible agent-based system (tools, scrapers, APIs, ML, etc.)
- 🛠️ Upcoming: **Shortlisting agent for multiple resumes** with SQLite storage

---

**Installation**

1. Install dependencies:
   pip install -r requirements.txt

2. Start Ollama server locally:
   ollama run mistral
   
4. Run the app:
  uvicorn main:app --reload

---

**File Formats**
Resume: .pdf only
Job Description: .csv with multiple entries

---

**Agents Overview**
Agent	Purpose
CV Parser Agent	Extracts structured details from resumes
JD Parser Agent	Extracts key requirements from the best-fit JD
Validation Agent	Evaluates skill match %, experience fit, and suitability
Schedule Agent	Suggests interview type, date, and interviewer role
(Coming Soon) Shortlisting Agent	Shortlists top candidates from multiple resumes

---

**TODO**
 Add shortlisting agent for multiple resumes
 Integrate SQLite to store parsed results & shortlist metadata
 Add embedding-based similarity search using Ollama
 Add API tools & web scraper tools for advanced analysis

---

**Powered By**
FastAPI
Ollama (Local LLMs)
Python, Jinja2, SQLite (upcoming)

---
**Author**
Built with ❤️ by PAUL LOBO for AI-powered hiring automation.


