
# DOIT

DOIT is a simple task management application built with Streamlit and MongoDB. It allows users to create, update, delete, and view tasks in a user-friendly interface.
.

![App Screenshot](resources/DOIT-LOGO.png)

## FEATURE 
- Add new tasks
- Update existing tasks
- Mark tasks as completed
- Delete tasks
- View all tasks with completion status

## REQUIREMENTS 
```bash
    Python
    Streamlit 
    PyMongo
    MongoDb
```

## CODE FUNCTIONS

- `main()`: The main function that sets up the Streamlit interface and handles the application flow.
- `add_task()`: Handles the addition of new tasks.
- `update_task()`: Manages the updating of existing tasks, including marking them as completed.
- `delete_task()`: Handles the deletion of tasks.
- `display_tasks()`: Displays the current list of tasks with their completion status.

## GETTING STARTED
Git clone the repository or fork it as you like
```bash
    git clone <http-link>
```
```bash
    cd DO-IT
```
Installation of the required packages/modules 
```bash
    pip install requirements.txt
```
Running the application locally
```bash
    streamlit run do-it.py
```
## BADGES

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

