# Another-Stupid-Blog
Another stupid blog app that nobody will really care about. I made it to learn the basics of creating full-stack applications with Flask

Done in a Python3 Dev Environment.

# Setup

Clone down the repo

In your terminal:

## Create Virtual Environment 

On Mac or Linux: 

```bash
$ cd /path/to/another-stupid-blog
$ python3 -m venv venv
```

On Windows:

```bash
$ cd /path/to/another-stupid-blog
$ py -3 -m venv venv
```

## Activate Virtual Environment

On Mac or Linux:

```bash
$ . venv/bin/activate
```

On Windows:

```bash
$ venv\Scripts\activate
```

## Install Flask 

```bash
$ pip install Flask
```

## Run Applicaton

On mac or Linux:

```bash
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

On Windows CMD:

```bash
$ set FLASK_APP=flaskr
$ set FLASK_ENV=development
$ flask run
```

On Windows Powershell:

```bash
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
$ flask run
```

Once running, you can access the application at http://127.0.0.1:5000 

Go sign up and write stuff that no one will care about.

As of now you have to register a user and then it will take you to the login page where you enter in that username and password.