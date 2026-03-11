🛡️ JobGuard AI
Machine Learning Powered Job Scam Detection
JobGuard AI is a sophisticated cybersecurity tool designed to detect and neutralize fraudulent job listings. By leveraging Random Forest Classification and Heuristic Analysis, the system identifies deceptive patterns in job metadata to protect candidates from phishing and financial scams.

📌 Table of Contents
➡ Overview

➡ The Problem

➡ Technical Approach

➡ Key Features

➡ Performance Metrics

➡ Installation & Usage

➡ Author

🔍 Overview
With the rise of remote work, job-related scams have increased significantly. JobGuard AI provides a secure terminal where users can audit job descriptions before applying. The engine analyzes linguistic cues and metadata to provide a real-time risk assessment.

❓ The Problem
Fraudulent job postings are often used to harvest sensitive personal data or solicit illegal payments. These scams use specific "urgency" and "high-pay" triggers that are difficult for humans to quantify manually but are easily detectable through machine learning.

🛠️ Technical Approach
Algorithm: Random Forest Classifier (chosen for its high precision in binary classification).

Feature Extraction: TF-IDF (Term Frequency-Inverse Document Frequency) to vectorize and weigh the importance of specific words in job postings.

Backend: Flask-based REST API for seamless model inference.

Visualization: Interactive Radar Charts using Chart.js to visualize risk vectors like Urgency and Anonymity.

✨ Key Features
🚀 Real-time Diagnostics: Paste a job description and get an instant security verdict.

📈 AI Confidence Score: Displays the mathematical probability of a listing being a scam.

🗺️ Risk Mapping: Visualizes specific threat vectors through a dynamic Radar Chart.

📄 Security Reports: Generates downloadable diagnostic summaries for users.
---

## 📸 Visual Demo & Screenshots

To provide a clear understanding of the system's interface and analytical capabilities, here are the key views of **JobGuard AI**:
🖥️ Prediction Terminal (Main Dashboard),📊 Real-time Risk Analysis & Intelligence
"<img src=""dashbord1.png"" width=""400px"" alt=""Dashboard 1""/>","<img src=""result1.png"" width=""400px"" alt=""Result 1""/>"
View 1: Input Description Area,View 1: Initial Risk Assessment
,
"<img src=""dashbord2.png"" width=""400px"" alt=""Dashboard 2""/>","<img src=""result2.png"" width=""400px"" alt=""Result 2""/>"
View 2: Security Diagnostics Trigger,View 2: Radar Chart & Security Report


📊 Performance Metrics
The model has been rigorously tested and achieved the following:

Accuracy: 98.5%

Patterns Learned: 438 distinct fraudulent behavior markers.

Method: Heuristic and Static Metadata Analysis.

🚀 Installation & Usage
Clone the repository:

Bash
git clone https://github.com/syedatayyabasource/JobGuard-AI.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
python app.py
👩‍💻 Author
Tayyaba Zahra Software Engineer | Cybersecurity Researcher 
🔗 LinkedIn: syeda-tayyaba-14b01436b

🔗 GitHub: syedatayyabasource