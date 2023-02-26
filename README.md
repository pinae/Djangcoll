# Djangcoll
Django project for training dataset collection

## Setting up the development server

First clone the repository:

```shell
git clone git@github.com:pinae/Djangcoll.git
```

Then enter the newly created folder:

```shell
cd Djangcoll
```

Set up the virtual environment with `pipenv` and install the dependencies:

```shell
pipenv install
```

After that enter the folder with the django project:

```shell
cd djangcoll
```

Now set up the database:

```shell
pipenv run python manage.py migrate
```

Create a superuser in the newly created installation:

```shell
pipenv run python manage.py createsuperuser
```

After that the setup is complete. You only need to complete the steps to this point once.

While developing you need to start the develpment server and you may need to restart it several times if critical 
Exceptions get thrown. This is normal as you usually have incomplete code during development. Start the development 
server with this command: 

```shell
pipenv run python manage.py runserver
```

The development server answers to requests to http://localhost:8000 (or http://127.0.0.1:8000 if your local 
nameserver config does not define a `localhost`).
