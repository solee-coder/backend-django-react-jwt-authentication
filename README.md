# Django & React Registration and Authentication - Django Backend

&nbsp;

## Installation

### Django Installation

This is the companion Github repository to the YouTube video demonstrating the installation and  testing of the API endpoints.

This repository constitutes the backend code using Python, Django and Django Rest Framework and relies on the dj-rest-auth package, which in turn relies on the django-allauth package.  It currently uses SQLite as the database, please change this according to your needs in the settings.py file. It utilises a Django custom user model, and uses email, rather than user name, as the mandatory registration and log in field. Transactional emails for registration and password management is used, so please ensure you have a suitable email provider that permits such emails. For demonstration purposes, the YouTube video uses the console email backend.

References for core packages:

dj-rest-auth: https://dj-rest-auth.readthedocs.io/en/latest/

django allauth: https://docs.allauth.org/en/latest/

simpleJWT: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html

&nbsp;

### Installation Steps

  
#1 Clone or download the repository. Inspect the pipfile to view the dependencies. The django project name is "backend_site" and the app is called "accounts".

#2 Using pipenv (https://pipenv.pypa.io/en/latest/) install the dependencies with `pipenv install`. The following are the core packages in used.

`pipenv install django==4.2 'dj-rest-auth[with_social]' django-cors-headers djangorestframework djangorestframework-simplejwt django-environ`

#3 A sample .env file is included called sample.env. Please configure this with your environment variables and email provider settings.

#4 Once installed, activate the virtual environment with `pipenv shell`

#5 Examine models.py in the accounts app folder.  Several custom user model fields have been created. Adding, removing and changing these fields will impact the rest of the configuration that you will have to customise, e.g. serializer.py, views.py, admin.py. Please remember to customise the user model before developing other models to avoid complications during database migrations (https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#changing-to-a-custom-user-model-mid-project). 

#6 Run `python manage.py makemigrations`

This will detect if there are any missing packages. Please note that pipenv may not successfully install all the dependencies in use, so please install them manually as needed based on the error messages.

#7 Run `python manage.py migrate`

This will set up the Django models.

#8 Run `python manage.py createsuperuser`

#9 Run `python manage.py runserver`

#10 Log in to the admin console. Add the email address to the superuser created earlier. Proceed to test the APIs.

&nbsp;

### Configuration notes:

**models.py** - configure the custom user model based on AbstractBaseUser class

**managers.py** - configure a custom user manager with email validation based on BaseUserManager class

**admin.py** - configure the Django admin panel for the custom user model

**serializers.py** - configure a custom Registration, User Details serializer. Configure settings.py to use these custom serializers

**adapter.py** - configure the save_user method to include the custom user fields not provided for by allauth. Configure settings.py to use this adapter
