## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Future Development](#future-development)

## Description

This Chatroom mini app is a Django-based web application, focusing on using Web Sockets to allow asynchronous requests alongside the synchronous HTTP requests used in prior projects.

The App focused on asynchronous Django using Web Socket , and so the UI was kept visually simple.

**Tech Stack: Python / Aysnchronous requests with Django Channels /  ORM with Django, JS DOM manipulation / tailwindcss**

## Installation

1. Clone the repository:

   ```bash
   gh repo clone wells1989/djangoChat-mini-project

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Apply database migrations:

   ```bash
   python manage.py migrate 

4. Run the development Server:

   ```bash
   python manage.py runserver 

Access the app at http://localhost:8000 in your web browser.

## Usage
- The homepage shows the list of Chatrooms available ...
![Screenshot (523)](https://github.com/wells1989/Full-stack-blog/assets/122035759/41e4c4e1-0c0e-4ac3-8ff3-6ded6c3aba4c)

- And in each Chatroom the messages can be added at the bottom, using Web Sockets to allow multiple simultaneous requests. The room page also used DOM manipulation to add new messages as well as adding key features such as auto-scroll on sending a new message.
![Screenshot (522)](https://github.com/wells1989/Full-stack-blog/assets/122035759/49d7317e-e8ca-4fd5-ad56-a4216f2ba64a)

### Future-development:
- As the focus of the project was on asynchronous Django programming, other features (logging in and registering / editing and deleting the messages) was not included in this first version.
- If this project was to be fully deployed, other features (likes on each message by altering the message model, creating new rooms via Django forms, adding message room favourites to Django's built-in User model to display in the front end.)
