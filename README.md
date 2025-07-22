# 🎓 Student Management System (Python + MySQL)

This is a simple command-line application for managing students and class records using Python and MySQL.

---

## 📁 Project Structure

```bash
GithubSql/
│
├── app.py             # Main CLI application
├── Connection.py      # Database connection (uses dotenv for security)
├── DbManager.py       # All DB functions (add, delete, update, select)
├── Student.py         # Student entity model
├── Class.py           # Class entity model
├── .env               # Hidden file for DB credentials (not uploaded to GitHub)
└── README.md          # This file

💡 Features:
- 🧾 List all students in a class

- ➕ Add new student

- 📝 Edit existing student

- ❌ Delete student by ID

- 📚 Display all classes

💻 Technologies Used
Python 3.x

MySQL

mysql-connector-python

python-dotenv

🔐 Environment Setup
Create a .env file in the root folder:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=studentdb

⚠️ Note: .env is excluded from GitHub via .gitignore for security.

⚙️ Installation & Run

# Clone the repo
git clone https://github.com/yourusername/yourrepo.git

# Go into project folder
cd yourrepo

# Install required packages
pip install mysql-connector-python python-dotenv

# Run the application
python app.py

🧠 Example Usage (Terminal UI)

******

1 - Student List  
2 - Add Student  
3 - Edit Student  
4 - Delete Student  
5 - Close (E/C)

Your Choice: 

🧾 Sample .env (For Testing)

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=erenpolat
DB_NAME=studentdb

👤 Author
Developed by Eren Polat

GitHub: github.com/erenpolat

📌 Notes
Supports only CLI (console) interface.

All SQL tables must be created beforehand (student, class etc.).

Ensure foreign key constraints are set correctly in MySQL.

📸 Screenshots
(You can add screenshots from terminal or code editor here using drag-drop in GitHub README editor)

