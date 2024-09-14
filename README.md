# Task manager app
Web application with a database connection using Flask as a framework.
# _Index_
- [Description](#description)
- [Features](#goal)
- [Project Features](#features)
  - [Functionality](#func)  
  - [Database](#bbdd)    
- [Tech stack](#stack)
- [Installation and Setup](#install)

## _Description_ <a name="description"></a>
This project is a simple web application to manage tasks, developed as a learning exercise for building apps connected to a database. The task manager allows users to perform basic operations on a list of tasks, such as creating, editing, marking as completed, and deleting tasks. 

<img width="952" alt="2024-09-14_15h31_35" src="https://github.com/user-attachments/assets/c1832461-d5b9-44a7-8a9a-31e74fbd752d">
<img width="954" alt="2024-09-14_15h33_56" src="https://github.com/user-attachments/assets/c51a281d-bd7b-4693-89d7-24a825337112">

## _Goal_ <a name="goal"></a>
The goal of the this projectis to apply concepts learned about web app development, database management, and the use of frameworks and libraries like Flask, SQLAlchemy, Bootstrap, and others.
## _Project Features_<a name="features"></a> 
### Functionality <a name="func"></a>
The application provides the following functionality:
- Create tasks, with the following fields:
  - Task description
  - Task category
  - Task deadline
- Mark tasks as completed
- Edit existing tasks
- Delete tasks
### Database <a name="bbdd"></a>
The application uses SQLite to store tasks. The database includes the following table:
- Table tarea (task):
  - id_tarea: unique ID of the task
  - contenido: task description
  - categoria: task category
  - fecha_limite: task deadline
  - hecha: Task status (completed or not)
## _Tech stack_<a name="stack"></a>
- Programming Language:
  - Python 3
- Development Framework:
  - Flask: Lightweight and powerful web framework.
- Database:
  - SQLite:  Relational database used to store tasks.
- ORM :
  - SQLAlchemy:used to interact with the database.
- Frontend:
  - HTML5, CSS3, JavaScript, jQuery, Jinja2
  - Bootstrap: A design framework for layout and styling.
  - Google Fonts: Used to enhance typography.
  - uiGradients: Tool for creating gradient backgrounds.
- Dependency Management:
  - blinker==1.6.2
  - click==8.1.3
  - colorama==0.4.6
  - dominate==2.8.0
  - Flask==2.3.3
  - Flask-Bootstrap==3.3.7.1
  - Flask-FontAwesome==0.1.5
  - Flask-WTF==1.2.1
  - greenlet==2.0.2
  - itsdangerous==2.1.2
  - Jinja2==3.1.2
  - MarkupSafe==2.1.3
  - SQLAlchemy==2.0.32
  - typing_extensions==4.6.3
  - visitor==0.1.3
  - Werkzeug==3.0.4
  - WTForms==3.0.1
- Development Tools:
  - Jetbrains Pycharm Community
- Virtual Environment (for development):
  - virtualenv: Creates Python virtual environments.

## _Installation and Setup_<a name="install"></a>
__1.__ Clone the repository  

__2.__ Create and activate a virtual environment:  
`` python -m venv venv   ``
- On Linux/Mac:  
`` 
source venv/bin/activate  ``

- On Windows (cmd):  
`` 
venv\Scripts\activate   ``

__3.__ Install dependencies:  

`` pip install -r requirements.txt  ``
   
__4.__ Run the application:
Set the FLASK_APP environment variable and run the application:  
- On Linux/Mac:  
`` 
export FLASK_APP=main.py
flask run  ``

- On Windows (cmd):  
`` 
set FLASK_APP=main.py
flask run   ``

__5.__ Access the application at http://127.0.0.1:5000/ in your browser.
