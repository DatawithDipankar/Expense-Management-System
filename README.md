

# 💸 Expense Management System

This is a full-stack Expense Management System with a **Streamlit frontend** and **FastAPI backend**, integrated with a **MySQL database**. It allows users to track, manage, and visualize expenses with features like budget tracking, PDF export, and password-protected access.


---

## 📁 Project Structure

```markdown
expense-management-system/
│
├── backend/             # FastAPI backend and DB helper
├── frontend/            # Streamlit app & UI logic
├── utils.py             # PDF generation utility
├── .env                 # Password (and optionally DB config)
├── requirements.txt     # Python dependencies
└── README.md
````
---

## 🚀 Features

- ✅ Add, update, delete daily expenses
- ✅ Category-wise analytics (bar chart + table)
- ✅ Monthly analytics view
- ✅ Monthly **budget tracker with progress bar**
- ✅ Export analytics report as **PDF**
- ✅ **Password-protected** access (via `.env`)
- ✅ Clean and modular structure

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
uvicorn server.server:app --reload
```

### 2. Run Streamlit frontend:

```bash
streamlit run frontend/app.py
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

For questions or collaboration opportunities, reach out via LinkedIn: [linkedin.com/in/datawithdipankar](https://www.linkedin.com/in/dipankar-mane-b9663b257?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BmEmSatCuRf%2BoV6n8VTN%2FLA%3D%3D)

```

---

Let me know if:
- You want to add screenshots or a demo video
- You want help writing a short LinkedIn post linking to this project
- You’re considering deploying this on a cloud platform (like Streamlit Cloud or Render)
```
