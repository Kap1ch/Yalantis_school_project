# Instructions for creating and launching a project

+ In an empty directory, execute the command:

`git clone https://github.com/Kap1ch/Yalantis_school_project.git`

+ Сreate a new virtual environment and run it.

   > Windows:
   
   `python3 -m venv venv`

   `.\venv\Scripts\activate.bat`
   
   > Linux:
   
   `python3 -m venv venv`

   `source venv/bin/activate`
   
+ Go to directory Yalantis_school_project:

`cd Yalantis_school_project`

+ Install all dependencies:

`pip install -r requirements.txt `

+ Apply migration:

`python manage.py migrate`

+ Create superuser:

`python manage.py createsuperuser`

+ run server:

`python manage.py runserver `

#### **Run tests**

`python manage.py test`






