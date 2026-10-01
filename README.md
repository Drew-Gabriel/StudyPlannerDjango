# Study Planner Django Web App

## Description
Study Planner is a Django web application that helps a student create and review study tasks. The application demonstrates server-side dynamic web pages, user input, Django views, templates, URL routing, forms, and a SQLite database.

## Technologies
- Python
- Django
- HTML
- CSS
- SQLite

## Requirements Demonstrated
- At least two dynamically generated HTML pages
- Interactive user input
- Local Django development server
- Database integration
- Third dynamically generated page

## How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment.
4. Install dependencies with `pip install -r requirements.txt`.
5. Run `python manage.py migrate`.
6. Start the server with `python manage.py runserver`.
7. Open `http://127.0.0.1:8000/` in a browser.

## Pages
- Home: `/`
- Add Task: `/add/`
- Task List: `/tasks/`

## How It Works
The user enters a task and subject on the Add Task page. Django receives the submitted form, validates the information, and saves it to the SQLite database. The Task List page retrieves the saved records and dynamically displays them.

## Video
Video link: [Add your 4–5 minute video link here]

## What I Learned
I learned how a Django URL routes a browser request to a Python view, how a view sends data to an HTML template, how forms accept user input, and how Django models connect a web application to a database.

## Author
Taiye Gabriel Ade-Benson
