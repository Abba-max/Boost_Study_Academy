# Boost_Study_Academy
An online platform for tutoring by Instructors in the Engineering domain

# Boost Study Academy

Boost Study Academy is a Django-based web project designed for studying, demonstrating, or deploying academic or educational applications. This README guides you through setup, execution, and development practices.

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (recommended)
- Git

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/Abba-max/Boost_Study_Academy.git
cd Boost_Study_Academy
```

### 2. Set Up a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```
*If `requirements.txt` does not exist, run:*
```sh
pip install django
```

### 4. Apply Database Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional, for admin site)

```sh
python manage.py createsuperuser
```

### 6. Run the Development Server

```sh
python manage.py runserver
```
Then visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

- `manage.py` – Django's command-line utility.
- `Boost_Study_Academy/` – Main project settings.
- `[app_name]/` – Your Django apps.
- `requirements.txt` – Python dependencies.
- `README.md` – This file.

## Running Tests

```sh
python manage.py test
```

## Contributing

Fork the repository, make your changes in a separate branch, and submit a pull request.

## License

This project is licensed under the MIT License.

---

**Happy coding with Django!**