

# 💸 Expense Management System

This is a full-stack Expense Management System with a **Streamlit frontend** and **FastAPI backend**, integrated with a **MySQL database**. It allows users to track, manage, and visualize expenses with features like budget tracking, PDF export, and password-protected access.


---

## 📁 Project Structure

```markdown
project-expense-tracking/
├── backend/
│ ├── db_helper.py # MySQL database operations
│ ├── logging_setup.py # Log configuration
│ └── server.py # FastAPI server with API routes
│
├── frontend/
│ ├── add_update_ui.py # Add/update expense UI
│ ├── analytics_by_category.py # Analytics by category
│ ├── analytics_by_month.py # Analytics by month
│ ├── budget_tracker.py # Monthly budget tracker UI
│ ├── utils.py # PDF export utility
│ └── app.py # Main Streamlit entry point
│
├── tests/
│ ├── backend/
│ │ └── test_db_helper.py # Tests for DB functions
│ ├── frontend/
│ └── conftest.py # Test config
│
├── README.md
└── requirements.txt
````
---

## 🚀 Features

- 📅 Add or update expenses by date
- 📊 Visualize analytics by **Category** or **Month**
- 🎯 Monthly budget tracker with a dynamic progress bar
- 🔐 Password-protected app access
- 📄 Download analytics reports as **PDF**
- 🧪 Unit tests for database logic

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/DatawithDipankar/expense-management-system.git
cd expense-management-system
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗃️ MySQL Database Setup

> ⚠️ Make sure you have MySQL installed and running

### A. Create database and table

You can do this via terminal or MySQL Workbench:

```sql
CREATE DATABASE expense_manager;

USE expense_manager;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    amount FLOAT NOT NULL,
    category VARCHAR(255),
    notes TEXT
);
```

### B. Configure connection

Edit the connection in `backend/db_helper.py`:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="expense_manager"
)
```

---

## 🔐 Password Protection

This app is protected by a login screen.

### Set the password in `.env`:

```
APP_PASSWORD=mysecret123
```

You’ll be prompted to enter this when you open the Streamlit app.

---

## ▶️ Run the Application

### 1. Start FastAPI backend:

```bash
backend/ uvicorn server:app --reload
```

### 2. Run Streamlit frontend:

```bash
frontend/ streamlit run app.py
```

---

## 📄 Exporting Reports

After analytics are generated, click **Download PDF** to export your category/monthly spending as a formatted report.

---

## 📌 To-Do (Ideas to Extend)

* User authentication system (multi-user)
* Cloud database or SQLite fallback
* Export to Excel or JSON
* Add dark/light mode toggle

---

## 🙌 Contributing

Contributions and suggestions are welcome! Feel free to fork the repo, create a branch, and submit a pull request.

---

## 📬 Contact

For questions or collaboration opportunities, reach out via LinkedIn: [linkedin.com](https://www.linkedin.com/in/dipankar-mane-b9663b257?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BmEmSatCuRf%2BoV6n8VTN%2FLA%3D%3D)

```
