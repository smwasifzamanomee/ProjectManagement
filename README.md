# Project Management Tool

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone git@github.com:smwasifzamanomee/ProjectManagement.git
   cd ProjectManagement

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   #pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
# ProjectManagement
