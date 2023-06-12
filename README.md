# agencymanagement
Django TP project

## Basic settings
If it's your first time opening this project, you need to do some change before using it.
Use these following command by open a terminal in your post or IDE:

- cd [project directory] # example cd my_project
- cp .env.dev .env # environnement based: dev or stage or pre-prod or prod
- cp core/settings.py.dev core/settings.py # environnement based: DEBUG == True or False
- pip install -r requirements.txt

# Useful command
### Pre-commit command
To check classical code review's issues before commit.
- cd [project directory] # example cd my_project
- pre-commit run --all-files
