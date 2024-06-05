# Muay Thai Club Website

Welcome to the Muay Thai Club website! This project is a web application build with Django that provides information about the Muay Thai club, including activities, training sessions, events, and much more. The website allows users to register, login, and interact with the club's content.

Access the site here <a href="https://muay-thai-club-website-a215eeee688f.herokuapp.com/">Muay Thai Club Website</a>

<img src="">

## Features

- User Registration, Login, and Logout using Django-allauth
- Home page with an image carousel and welcome text
- Contact form for questions from users saved in the database
- Saving images using Cloudinary
- Activities with categories created from the admin dashboard
- Admin interface for managing content
- CRUD availability for users

## Technologies Used

**Frontend:**
- HTML
- CSS
- Bootstrap

**Backend:**
- Python
- Django
- Django-allauth for authentication
- Contact form request saved in database
- Static files for deployment on heroku website

**Database:**
- SQLite (default Django database, easily replaceable with PostgreSQL, MySQL, etc.)

## Usage
- **Register a new user:** Navigate to the signup page and fill out the registration form.
- **Login:** Use the login page to access your account.
- **Admin Interface:** Access the admin interface at /admin to manage content. Use the superuser credentials created during installation.

## Local Deployment

1. **Clone the repository:**

```console
git clone https://github.com/yourusername/muay-thai-club-website.git
cd muay-thai-club-website
```

2. **Install the Required Dependencies**

```console
pip install -r requirements.txt
```

3. **Set up the database:**

```console
python manage.py migrate
```

4. **Create a superuser:**

```console
python manage.py createsuperuser
```

5. **Run the development server:**

```console
python manage.py runserver
```

6. **Navigate to the project in your browser:**

```console
http://127.0.0.1:8000/
```

## Credits

**Content**
  - Some of the text for the README.md file were taken from <a href="https://chat.openai.com/">ChatGPT</a>
  - Contact form requests on contact page taken from the CI <a href="https://github.com/Code-Institute-Solutions/blog/tree/main/13_collaboration_form/01_create_the_form/about">Django Blog</a>

**Styling**
  - The styling for the game area was largely taken from the CI <a href="https://p3-battleships.herokuapp.com/">Battleships</a> project.
