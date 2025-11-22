# 🎯 Event Registration System

A full-stack web application built using **Python (Django)** that allows users to register for events and stores the data in a database. Admins can view all registrations through a secure admin dashboard.

---

## 🚀 Tech Stack

| Technology | Usage |
|-----------|-------|
| Python | Backend logic |
| Django | Web Framework |
| SQLite | Local Database |
| HTML, CSS | Frontend UI |
| Django Templates | Rendering Pages |

---

## ✨ Features

✔ User Event Registration Form  
✔ Stores data in database  
✔ Admin dashboard to manage registrations  
✔ Success confirmation page  
✔ View all registrations  
✔ Secure user data handling  
✔ Fully responsive UI *(styling update coming soon)*

---


## 📂 Project Structure

Event-Registration-System/
│── event_project/ # Main Django project
│── event_app/ # Application with models + views
│── templates/ # HTML pages
│── db.sqlite3 # Database
│── manage.py # Django entry point


---

## ⚙️ Setup Instructions

Clone the repository:

```bash
git clone https://github.com/AbhishekRay79/Event-Registration-System.git
cd Event-Registration-System

Create & activate virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows

Install dependencies:

pip install django

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Run the server:

python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

Admin panel → http://127.0.0.1:8000/admin

🔑 Admin Access

You can create your own:

python manage.py createsuperuser

🎯 Future Enhancements

🔹 Bootstrap UI for modern design

🔹 Email confirmation to users

🔹 Multiple event categories

🔹 Edit/Delete registrations (Full CRUD)



🙌 Developer

Abhishek Ray
📍 B.Tech (CSE)



