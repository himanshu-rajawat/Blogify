# Blogify

[![Blogify Logo](https://blogify-application.web.app/img/blogify_logo.acfb6c5c.png)](https://blogify-application.web.app)

A blogging platform built using Django and Vue.js, with features such as user authentication using JWT, following and liking other users' posts, saving posts for later reading, and using AWS S3 bucket to store media files. 

## Key Features
- User authentication using JWT
- Ability to follow and like other users' posts
- Option to save posts for later reading
- AWS S3 bucket to store media files
- Single-page application using Vue components and Vue Router
- REST APIs implemented using Django REST framework for CRUD operations

## Requirements
- Python 3.x
- Django 3.x
- Vue.js 2.x

## Setup

### Django Project
1. Clone the repository: `git clone <repo>`
2. Create and start a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: 
    - `python manage.py makemigrations`
    - `python manage.py migrate`
5. Start the Django server: `python manage.py runserver`

### Vue.js Project
1. Clone the repository: `git clone <repo>`
2. Ensure that npm is installed on your system
3. Update URLs for the Django app in the Vue components
4. Start the Vue app: `npm runserve`

## Contributing
Feel free to fork the repository and make a pull request if you want to contribute to this project.
