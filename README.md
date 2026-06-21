# My To-Do List Website

My To-Do List Website is a simple full-stack task management application built using Python Flask, HTML, and CSS. The application allows users to add tasks, delete tasks, and maintain a history log of all actions performed. The project demonstrates frontend-backend integration using Flask routes and dynamic HTML rendering.

---

## Core Features Overview

### Task Management

* Add new tasks using an input field.
* Display all active tasks in a dedicated Tasks section.
* Delete tasks using a Delete button.
* Automatically update the task list without manual page refresh.

### History Tracking

* Records every task addition.
* Records every task deletion.
* Displays action history in a separate History section.

### Flask Backend

* Handles form submissions.
* Manages task storage using Python lists.
* Processes task deletion requests.
* Renders dynamic content using Jinja2 templates.

### User Interface

* Responsive layout using HTML and CSS.
* Moon-themed background design.
* Clean task and history sections.
* Styled buttons and glass-effect input field.

---

## Project Directory Structure

```text
todo-list/
│
├── app.py                 # Flask backend application
├── index.html             # Main frontend page
├── style.css              # Styling and layout
├── moon.jpeg              # Background image
└── README.md              # Project documentation
```

---

## Technologies Used

### Frontend

* HTML5
* CSS3

### Backend

* Python
* Flask

---

## Application Workflow

```text
User
 ↓
HTML Form
 ↓
Flask Route (/add)
 ↓
Python Task List
 ↓
Display Updated Tasks

Delete Button
 ↓
Flask Route (/delete/<index>)
 ↓
Remove Task
 ↓
Update History
 ↓
Render Updated Page
```

---

## Local Setup Guide

### Prerequisites

* Python 3.10 or higher
* Flask installed

### Install Flask

```bash
pip install flask
```

### Run Application

```bash
python app.py
```

---

## View the Project

After running the application, open your web browser and navigate to:

```text
http://127.0.0.1:5000
```

You will be able to:

* Add new tasks
* Delete existing tasks
* View task history
* Interact with the application through the web interface

---

## Future Improvements

* Store tasks in SQLite database.
* Add task completion status.
* Add due dates and priorities.
* User authentication and login.
* Dark/Light theme switcher.

---

## Learning Outcomes

This project demonstrates:

* Python Flask backend development
* Form handling in Flask
* Dynamic page rendering using Jinja2
* HTML and CSS frontend design
* CRUD-style task operations
* Basic full-stack web development concepts
