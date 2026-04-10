<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/1f111580-5259-416c-a4c8-f6eb55d09b85" /># 🔐 Agentic Privacy Analyzer

An **Agentic AI-based web application** that analyzes a user's digital footprint and provides **privacy risk assessment and actionable security recommendations**.

---

## 1️⃣ Business Problem

In today's digital ecosystem, users frequently reuse emails and passwords across multiple platforms.  
This leads to:

- Data breaches and credential leaks  
- Lack of awareness about digital exposure  
- No clear guidance on how to improve security  

👉 Most users **do not know whether their data is exposed or how to respond**.

---------------------------------------------------------------------------------------------------------------------------

## 2️⃣ Possible Solution

A system that can:

- Detect exposure of user data  
- Analyze the severity of risk  
- Provide actionable recommendations  

This can be achieved using **Agentic AI**, where multiple intelligent agents collaborate to solve the problem.

---------------------------------------------------------------------------------------------------------------------------

## 3️⃣ Implemented Solution

This project implements a **multi-agent system**:

### Agents:

- 🔍 **Data Finder Agent**
  - Detects whether an email is exposed

- 📊 **Risk Analyzer Agent**
  - Assigns a risk score (LOW / MEDIUM / HIGH)

- 🛡 **Privacy Advisor Agent**
  - Provides security recommendations

### Flow:

User Input → Data Finder → Risk Analyzer → Advisor → Output

👉 The system is **deterministic** (same input → same output) ensuring reliability.

---------------------------------------------------------------------------------------------------------------------------

## 4️⃣ Tech Stack Used

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Architecture | Agent-based modular system |
| Visualization | Streamlit UI |
| Version Control | Git + GitHub |

---------------------------------------------------------------------------------------------------------------------------

## 5️⃣ Architecture Diagram
+-------------------+
| User Input |
| (Email Input) |
+---------+---------+
|
v
+------------------------+
| Data Finder Agent |
| (Check Exposure) |
+---------+--------------+
|
v
+------------------------+
| Risk Analyzer Agent |
| (Risk Calculation) |
+---------+--------------+
|
v
+------------------------+
| Privacy Advisor Agent |
| (Recommendations) |
+---------+--------------+
|
v
+------------------------+
| Final Output |
| (UI + Logs + Report) |
+------------------------+



---------------------------------------------------------------------------------------------------------------------------

## 6️⃣ How to Run Locally

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/agentic-privacy-analyzer.git
cd agentic-privacy-analyzer

Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run Application
streamlit run app.py


---------------------------------------------------------------------------------------------------------------------------


Screenshots--

--https://drive.google.com/drive/folders/1l2naRvZeN6UXO2PvmtLX8O--YnbeJOg5?usp=sharing

---------------------------------------------------------------------------------------------------------------------------

7️⃣ References and Resources Used
Streamlit Documentation → https://docs.streamlit.io
Python Official Docs → https://docs.python.org
GitHub Documentation → https://docs.github.com

------------------------------------------------------------------------------------------------------------------------

Problems Faced & Solutions
Problem	Solution
Inconsistent results (random output) -->	Replaced with deterministic logic
Git push errors (rejected) -->	Used git pull --allow-unrelated-histories
File not visible locally --> Restored project using GitHub clone
Streamlit UI issues	--> Simplified layout and improved structure
JSON download not opening	--> Changed format to .txt

🛡 Guardrails Implemented
Email format validation
Ethical usage warning
Deterministic output (no randomness)


---------------------------------------------------------------------------------------------------------------------------

🎯 Use Case

This system helps:

Individuals understand their digital exposure
Improve cybersecurity awareness
Demonstrate Agentic AI collaboration

---------------------------------------------------------------------------------------------------------------------------

🚀 Future Enhancements
Real API integration (HaveIBeenPwned)
Authentication system
Database storage
Dashboard analytics

---------------------------------------------------------------------------------------------------------------------------

⚠️ Disclaimer

This project is for educational purposes only.
Only analyze data you own or have permission to check.

👨‍💻 Author
Vishnu G
