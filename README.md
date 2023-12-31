
Task Flow System is a custom task management system designed to streamline the product development process within a team of Developers, Designers, Project Managers, and QA specialists. This platform allows team members to create tasks, assign them to specific team members, and track the progress of tasks from creation to completion.

Features
Task Creation: Any team member can create a new task by providing a task name, description, deadline, priority, and task type.

Assign Tasks: Tasks can be assigned to specific team members, allowing for clear accountability and responsibility.

Mark as Done: Team members can mark tasks as done, providing a quick overview of completed and ongoing tasks.

Deadline Tracking: The system tracks deadlines for tasks, helping the team prioritize and meet project timelines.

User Roles: The platform supports different user roles, including Developers, Designers, Project Managers, and QA specialists, each with specific permissions.

You can see the database schema [here](https://dbdiagram.io/d/654363957d8bbd6465560b26)

[Task Flow System deployed to Render](https://task-flow-3q5o.onrender.com)

Getting Started
- To get started with TeamTask Manager, follow these steps:
 Fork the repo (GitHub repository)
1. Clone the forked repo
    ```
    git clone the-link-from-your-forked-repo
    ```
    - You can get the link by clicking the `Clone or download` button in your repo 
2. Open the project folder in your IDE 
3. Open a terminal in the project folder 
4. Create virtual environment
    and install requirements in it, but if not:
    ```
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt
    ```
5. Database Setup:
  - `python manage.py makemigrations`
  - `python manage.py migrate`


You can use the following command to load prepared data from fixture to test:
`python manage.py loaddata task_manager_db_data.json`


After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `user1`
  - Password: `1qazcde3`

Runserver:
`python manage.py runsever`