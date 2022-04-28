# Eterlast App Backend

# The first thing to do is to clone the repository:

```sh
$ git clone --------/------------
```

# Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

# Then install the dependencies:

```sh
(env)$ cd eterlast
(env)$ pip install -r requirements.txt
```

# Once pip has finished downloading the dependencies:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```