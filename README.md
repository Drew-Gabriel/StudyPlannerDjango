Study Planner Django Web App

Description

Study Planner is a Django web application that helps students create and review study tasks. The application allows users to enter a subject, task title, and planned study time. The information is saved in a database and displayed dynamically on the website.

This project demonstrates how Python and Django can be used to create an interactive web application.

Technologies

- Python
- Django
- HTML
- CSS
- SQLite
- Git and GitHub

Requirements Demonstrated

This project demonstrates the following Web Apps requirements:

- At least two dynamically generated HTML pages
- Interactive user input
- A web application running on the local Django development server
- Database integration
- A third dynamically generated web page

Pages

Home

URL: "/"

The Home page displays the Study Planner and a summary of the saved study tasks. It shows the total number of tasks and total study minutes.

Add Task

URL: "/add/"

The Add Task page allows the user to enter a subject, task title, and study time. Django processes the submitted form and saves valid information to the database.

Task List

URL: "/tasks/"

The Task List page retrieves saved study tasks from the database and displays them dynamically.

How It Works

The user enters information on the Add Task page. Django receives the submitted form and validates the information. If the information is valid, the study task is saved in the SQLite database.

The Task List page retrieves the saved tasks from the database and displays them.

The Home page also calculates and displays a summary of the saved tasks.

Database

The application uses a SQLite database with a Django model called "StudyTask".

Each study task stores:

- Subject
- Title
- Study time in minutes
- Date and time created

How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Create a virtual environment.
4. Activate the virtual environment.
5. Install the dependencies:

"pip install -r requirements.txt"

6. Apply the database migrations:

"python manage.py migrate"

7. Start the Django development server:

"python manage.py runserver"

8. Open the application in a browser at:

"http://127.0.0.1:8000/"

Video

Video link:(https://youtu.be/XHTutXjbD4s?si=nrlGwjdqYitwqvYo)

The video will demonstrate the application running, show the main features, and provide a walkthrough of the Django code.

What I Learned

I learned how Django connects URLs, Python views, HTML templates, forms, and a database to create an interactive web application.

I also learned how to accept user input, validate form information, save information to a database, and display saved information dynamically.

One challenge was setting up the Python and Django environment. Breaking the work into smaller steps and testing each part helped me solve the problems.

Author

Taiye Gabriel Ade-Benson

GitHub

Repository: "StudyPlannerDjango"