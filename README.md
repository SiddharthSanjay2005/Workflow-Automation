# 🚀 Intelligent Workflow Automation System


## 📌 Overview:-
This project is an **AI-inspired workflow automation system** that processes leads, makes decisions based on rules, and triggers actions like email, SMS, and CRM updates.
It simulates real-world systems like **CRM automation tools (HubSpot, Zapier)**.


## 🎯 Problem Statement:-
Design an AI-powered system to automate workflows across platforms with dynamic decision-making.


## ✅ Features Implemented:-

### 🔹 Workflow Orchestration Engine:-
* Central engine to process leads
* Executes actions based on decisions

### 🔹 Dynamic Decision Logic:-
* Lead scoring system
* Rule-based classification:
  * HIGH_PRIORITY
  * FOLLOWUP
  * LOW_PRIORITY

### 🔹 Multi-System Integration:-
* CRM (internal system)
* Email service (mock)
* SMS service (mock)

### 🔹 Retry Mechanism:-
* Handles failures (e.g., email service)
* Automatically retries operations

### 🔹 Workflow Logging:-
* Tracks all actions performed
* Stores logs in database

### 🔹 Web Dashboard:-
* Add leads via UI
* View leads in table
* View workflow logs


## 📥 Input:-

Leads contain:
* Name
* Phone
* Status (new/contacted)
* Interest Level (1–10)


## ⚙️ System Architecture:-

Frontend (Dashboard UI)
↓
Flask API
↓
Orchestrator Engine
↓
-

| Rules Engine (Decision Logic) |
| Email Service                |
| SMS Service                  |
| CRM Service                  |
--------------------------------

↓
SQLite Database



## 🔄 Workflow Execution Flow:-
1. User submits lead
2. Lead stored in database
3. Score calculated
4. Decision made:
   * HIGH_PRIORITY → Email + SMS + CRM update
   * FOLLOWUP → Email + CRM update
   * LOW_PRIORITY → No action
5. Actions logged


## 🧠 Scoring Logic:-
Score = (interest_level × 10) + 20 (if status = new)


## 🖥️ API Endpoints:-

| Method | Endpoint  | Description          |
| ------ | --------- | -------------------- |
| POST   | /add-lead | Add and process lead |
| GET    | /leads    | Get all leads        |
| GET    | /logs     | Get workflow logs    |


## ▶️ How to Run:-

### 1. Clone project:-
git clone https://github.com/your-username/workflow-automation.git

### 2. Navigate:-
cd workflow-automation

### 3. Create virtual environment:-
py -m venv venv
venv\Scripts\activate

### 4. Install dependencies:-
python -m pip install -r requirements.txt

### 5. Run server:-
python app.py

### 6. Open dashboard:-
http://127.0.0.1:5000/


## 🧪 Sample Input:-

Name: Siddharth
<br>
Phone: 9876543210
<br>
Status: new
<br>
Interest Level: 9


## 📊 Output Example:-

* Email + SMS triggered
* CRM updated
* Logs stored in database


## 📂 Project Structure:-

Workflow-Automation/
├── app.py
<br>
├── database.py
<br>
├── engine/
<br>
├── models/
<br>
├── services/
<br>
├── routes/
<br>
├── templates/
<br>
├── static/


## 🔥 Future Possible Improvements:-

* React dashboard
* Machine Learning lead scoring
* Authentication system
* Deployment (AWS / Render)


## 🏁 Conclusion:-
This project demonstrates:

* Backend system design
* Workflow automation
* API integration
* Real-world architecture


## 👨‍💻 Author:-
Siddharth Sanjay
