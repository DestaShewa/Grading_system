# 🎓 GradePro — Student Grading Management System

A simple and professional **Student Grading Management System** built with **Python, Flask, SQLite, HTML, and CSS**.

The project allows administrators to manage student records, enter subject marks, automatically calculate grades, search and filter students, and view individual academic results through a clean and responsive web interface.

> 🚧 **Project Status:** Development milestone completed.
> The current version focuses on core functionality, CRUD operations, database integration, and professional UI/UX. Security, authentication, PostgreSQL, automated testing, APIs, and deployment are planned for future versions.

---

## 📸 Overview

GradePro provides a centralized interface for managing student academic information.

### Main features

* 📊 Dashboard with student statistics
* 👨‍🎓 Student management
* ➕ Add students
* ✏️ Edit student information
* 🗑️ Delete students
* 🔎 Search students by ID or name
* 🎯 Filter students by pass/fail status
* 🧮 Automatic total calculation
* 📈 Automatic average calculation
* 🏆 Automatic grade calculation
* ✅ Pass/fail calculation
* 📄 Individual student result page
* 💬 User feedback messages
* 📱 Responsive UI for smaller screens
* 🧩 Flask Blueprint-based routing
* 💾 SQLite database persistence

---

# 🛠️ Technologies

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core programming language |
| Flask      | Web framework             |
| SQLite     | Database                  |
| HTML5      | Page structure            |
| CSS3       | Styling and responsive UI |
| Jinja2     | Server-side templates     |
| Git        | Version control           |
| GitHub     | Source code hosting       |

---

# 🏗️ Project Architecture

The project currently follows a simple modular Flask architecture:

```text
grading_system/
│
├── app.py
├── database.py
├── grading.py
├── grading.db
│
├── routes/
│   ├── __init__.py
│   └── students.py
│
├── services/
│   ├── __init__.py
│   └── student_service.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   │
│   └── students/
│       ├── list.html
│       ├── add.html
│       ├── edit.html
│       └── result.html
│
└── static/
    └── css/
        └── style.css
```

---

# 📂 Main Components

## `app.py`

The main Flask application.

Responsibilities:

* Creates the Flask application
* Initializes the database
* Registers the students Blueprint
* Provides the dashboard route

---

## `database.py`

Handles SQLite database operations.

Responsibilities:

* Creating the database connection
* Configuring SQLite rows
* Creating the `students` table

---

## `grading.py`

Contains the grading/business calculation logic.

It calculates:

```text
Total
   ↓
Average
   ↓
Grade
   ↓
Pass / Fail
```

### Current grading scale

|  Average | Grade |
| -------: | :---: |
|   90–100 |   A   |
|    80–89 |   B   |
|    70–79 |   C   |
|    60–69 |   D   |
| Below 60 |   F   |

### Passing rule

```text
Average >= 50 → PASS

Average < 50 → FAIL
```

---

## `routes/students.py`

Contains student-related web routes using a Flask Blueprint.

Current endpoints include:

```text
/students
/students/add
/students/<id>
/students/edit/<id>
/students/delete/<id>
```

---

## `templates/`

Contains the application's HTML templates using Jinja2.

The templates include:

* Dashboard
* Student list
* Add student form
* Edit student form
* Student result page
* Shared base layout

---

## `static/css/style.css`

Contains the application's visual design.

The current UI includes:

* Sidebar navigation
* Top navigation
* Dashboard cards
* Responsive tables
* Forms
* Buttons
* Status badges
* Result cards
* Empty states
* Flash messages
* Mobile responsive layout

---

# ⚙️ How the Application Works

The basic workflow is:

```text
                 ┌──────────────┐
                 │   Dashboard  │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   Students   │
                 └──────┬───────┘
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
          Add        Edit       Delete
             │          │
             └─────┬────┘
                   ▼
             Enter Marks
                   │
                   ▼
          ┌─────────────────┐
          │ Calculate Result│
          └────────┬────────┘
                   │
            ┌──────┼──────┐
            ▼      ▼      ▼
          Total Average Grade
                         │
                         ▼
                    PASS / FAIL
                         │
                         ▼
                  Student Result
```

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/grading-system.git
```

Move into the project:

```bash
cd grading-system
```

---

## 2. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
```

Windows:

```bash
python -m venv venv
```

---

## 3. Activate the virtual environment

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install flask
```

---

# ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

You should see something similar to:

```text
 * Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🧪 Example

Create a student:

```text
Student ID: STU-001
Name: Abebe Kebede

Mathematics: 85
English: 78
Science: 92
```

The system automatically calculates:

```text
Total:    255
Average:  85
Grade:    B
Status:   PASS
```

---

# 🔎 Student Search

Students can be searched using:

```text
Student ID
```

or:

```text
Student Name
```

The list can also be filtered by:

```text
All Students
Passed
Failed
```

---

# 🎯 Current Features

### Dashboard

The dashboard provides:

* Total number of students
* Overall average
* Number of passed students
* Number of failed students
* Recently added students

### Student Management

Administrators can:

```text
Create
  ↓
Read
  ↓
Update
  ↓
Delete
```

student records.

### Automatic Grading

The application automatically calculates:

```text
Total = Math + English + Science

Average = Total / 3
```

Then assigns the appropriate grade and status.

---

# 🔐 Current Security Status

This is currently a **learning/development project** and should not be deployed publicly as-is.

The current version does not yet include:

* User authentication
* Role-based authorization
* CSRF protection
* Production secret management
* Production database configuration
* Rate limiting
* Comprehensive automated testing
* Production server configuration
* HTTPS configuration

These are planned improvements.

---

# 🛣️ Roadmap

The project will evolve gradually from a simple Flask application into a more production-oriented system.

## Phase 1 — Core Application ✅

* [x] Flask application
* [x] SQLite database
* [x] Student CRUD
* [x] Automatic grading
* [x] Search
* [x] Filtering
* [x] Student result page
* [x] Dashboard statistics
* [x] Flask Blueprint
* [x] Responsive UI
* [x] Professional UI/UX

---

## Phase 2 — Code Quality

* [ ] Complete service layer
* [ ] Better validation
* [ ] Custom exceptions
* [ ] Centralized error handling
* [ ] Application configuration
* [ ] Environment variables
* [ ] Logging
* [ ] Improve project structure

---

## Phase 3 — Production Database

Replace SQLite with PostgreSQL.

Planned:

* [ ] PostgreSQL
* [ ] Database migrations
* [ ] Database indexes
* [ ] Better constraints
* [ ] Connection management

---

## Phase 4 — Authentication & Security

* [ ] Admin login
* [ ] Password hashing
* [ ] Authentication
* [ ] Authorization
* [ ] Role-based access
* [ ] CSRF protection
* [ ] Secure sessions
* [ ] Input sanitization
* [ ] Security headers

---

## Phase 5 — REST API

Build an API for other applications.

```text
Web Application
       │
       ▼
     Flask
       │
       ├────────── Web UI
       │
       └────────── REST API
                       │
              ┌────────┴────────┐
              ▼                 ▼
           Flutter           Other Apps
```

Planned:

* [ ] REST API
* [ ] JSON responses
* [ ] API validation
* [ ] API authentication
* [ ] Pagination
* [ ] API documentation

---

## Phase 6 — Testing

* [ ] Unit tests
* [ ] Integration tests
* [ ] Route tests
* [ ] Database tests
* [ ] Validation tests
* [ ] Automated test workflow

---

## Phase 7 — Deployment & DevOps

* [ ] Docker
* [ ] Docker Compose
* [ ] PostgreSQL container
* [ ] Gunicorn
* [ ] Nginx
* [ ] Environment configuration
* [ ] CI/CD
* [ ] Cloud deployment
* [ ] Monitoring
* [ ] Production logging

---

# 📚 What I Learned From This Project

This project was built incrementally to practice real software engineering concepts.

Key concepts practiced:

```text
Python
  ↓
Functions
  ↓
Modules
  ↓
Flask
  ↓
Routing
  ↓
Templates
  ↓
Forms
  ↓
CRUD
  ↓
SQLite
  ↓
SQL
  ↓
Blueprints
  ↓
Separation of concerns
  ↓
UI/UX
  ↓
Responsive design
```

The project also helped demonstrate the difference between:

```text
"It works"
```

and:

```text
"It is organized, maintainable,
usable, secure and deployable."
```

The current milestone focuses primarily on **functionality + maintainability + UI/UX**.

---

# 🎓 Project Purpose

This project was created as part of my journey toward becoming a:

**Software Engineer → System Engineer → AI Agent Systems Engineer**

Rather than only studying programming concepts theoretically, I am using progressively more complex projects to practice:

* Backend development
* Database design
* Software architecture
* API development
* Security
* DevOps
* System design
* AI system integration

---

Possible future features include:

* Teacher management
* Class management
* Subject management
* Attendance
* Student performance analytics
* Parent accounts
* Teacher accounts
* Mobile application
* Notifications
* AI-powered student performance analysis
* AI tutoring assistant
* AI-generated learning recommendations

---

# 🤝 Contributing

This project is primarily a personal learning and portfolio project.

Suggestions, improvements, and constructive feedback are welcome.

---

# 📄 License

This project is currently intended for educational and portfolio purposes.

Add a formal open-source license if you decide to distribute the project publicly.

---

# 👨‍💻 Author

**Desta Shewa**

Computer Science Graduate | Software Engineering | Backend Development | AI Systems

---

⭐ If you find this project useful, consider giving the repository a star.

