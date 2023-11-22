# it_company_task_manager
You can see the database schema [here](https://dbdiagram.io/d/654363957d8bbd6465560b26)
Description
ProjectTask Manager is a custom task management system designed to streamline the product development process within a team of Developers, Designers, Project Managers, and QA specialists. This platform allows team members to create tasks, assign them to specific team members, and track the progress of tasks from creation to completion.

Features
Task Creation: Any team member can create a new task by providing a task name, description, deadline, priority, and task type.

Assign Tasks: Tasks can be assigned to specific team members, allowing for clear accountability and responsibility.

Mark as Done: Team members can mark tasks as done, providing a quick overview of completed and ongoing tasks.

Deadline Tracking: The system tracks deadlines for tasks, helping the team prioritize and meet project timelines.

User Roles: The platform supports different user roles, including Developers, Designers, Project Managers, and QA specialists, each with specific permissions.

You can see the database schema [here](https://dbdiagram.io/d/654363957d8bbd6465560b26)

Getting Started
To get started with TeamTask Manager, follow these steps:

Clone the Repository:

git clone https://github.com/your-username/TeamTask-Manager.git

Install Dependencies:

Copy code:

pip install -r requirements.txt

Database Setup:

python manage.py migrate

python manage.py createsuperuser

Run the Development Server:

python manage.py runserver