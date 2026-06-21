# My To-Do List Website

My To-Do List Website is a simple full-stack task management application built using Python Flask, HTML, and CSS. The application allows users to add tasks, delete tasks, and maintain a history log of all actions performed. The project demonstrates frontend-backend integration using Flask routes and dynamic HTML rendering.

---

## Project Objective

The purpose of this project is to develop a simple and user-friendly task management application using Flask. The project demonstrates how a frontend interface can communicate with a Python backend to perform task operations and display dynamic content.

---

## Why This Project Is Important

Task management applications are widely used in personal and professional environments to improve productivity and organization. This project provides a practical example of how web applications handle user input, process data on the server, and display updated information dynamically.

Building this project helped in understanding the complete workflow of a web application, including frontend design, backend processing, data management, and user interaction. It also serves as a foundation for developing larger productivity and management systems.

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

## Key Concepts Used

* Flask Routing
* Form Handling
* GET and POST Requests
* Dynamic HTML Rendering
* Jinja2 Templates
* Python Data Structures
* CRUD Operations
* Frontend and Backend Integration

---

## System Architecture

The application follows a simple client-server architecture:

1. The user enters a task through the web interface.
2. The form sends data to the Flask backend.
3. Flask processes the request and updates the task list.
4. Updated data is rendered dynamically using Jinja2 templates.
5. The browser displays the latest task and history information.

---

## Data Management

The application currently stores data using Python lists during runtime.

### Tasks List

Stores all active tasks entered by the user.

### History List

Stores records of task additions and deletions, allowing users to view past actions performed within the application.

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

## Benefits of the Project

* Improves task organization.
* Demonstrates full-stack development fundamentals.
* Provides practical experience with Flask.
* Introduces dynamic web application development.
* Serves as a foundation for more advanced productivity applications.

---

## Challenges Addressed

* Managing communication between frontend and backend.
* Handling user input through web forms.
* Updating content dynamically after each operation.
* Maintaining task history records.
* Creating a responsive and visually appealing interface.

---

## Future Database Integration

Currently, task data is stored temporarily in memory. Future versions can integrate SQLite or other databases to provide permanent storage and improved scalability.

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

---

## Project Significance

This project serves as an introduction to full-stack web development. It combines frontend technologies with backend programming and demonstrates how web applications process, store, and display user-generated data.
