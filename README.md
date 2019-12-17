# Ak-Blog

Simple Flask blog application made during Flask
[Learning](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

## Technologies/Tools used & needed.
* **[Python](https://www.python.org/downloads/)** - A programming language.
* **[Flask](flask.pocoo.org/)** - A microframework for Python.
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[SQLITE](https://www.sqlite.org/index.html)** - Small, fast, self-contained, high-reliability, full-featured, SQL DB.

* **[Vagrant](https://www.vagrantup.com/)** - Development Environments Made Easy.

## Table of contents
* [Installation and Usage](#installation-and-usage)

## Installation and usage
**NB** 
* Run the following commands on your terminal.

1. #### **Clone or download repo.**
    ```
    $ git clone https://github.com/Xerrex/ak-Blog.git
    ```
2. #### **Create virtual environment**
    ```
    $ virtualenv -p python3 venv
    ```
    
3. #### **Environment variables.**

    ##### Copy .env file
    ```
    (venv)$ cp .env.examples .env
    ```
    * Edit the following lines on **.env** file.<br>
        Replace **[]** with your actual value.
        ```
        source ./venv/bin/activate
        export FLASK_APP="run.py"
        export SECRET_KEY="[your secret phrase]"
        export DATABASE_URL=""
        export MS_TRANSLATOR_KEY="[paste-your-key-here]
        export ADMINS="[["<paste-admin-email2>","<paste-admin-email2>"]]"
        export MAIL_SERVER=smtp.googlemail.com
        export MAIL_PORT=587
        export MAIL_USE_TLS=1
        export MAIL_USERNAME=<your-gmail-username>
        export MAIL_PASSWORD=<your-gmail-password>
        ```
        
        **To change Enviroment add**
        ```
        export FLASK_DEBUG=1 
        ```

    * Activate virtual environment & export variables.
        ```
        $ source .env
        ```
    * Install Dependancies.
        ```
        (venv)$ pip install -r requirements.txt
        ```  
5. #### **Apply Database migrations**
    ```
    (venv)$ flask db upgrade
    ```
6. #### **Run the app**
   ```
   (venv)$ flask run
   ```


## Additional Information
App contains additional languages to help with language translations

* **flask translate init LANG** to add a new language. LANG is the new language
* **flask translate update** to update all language repositories.
* **flask translate compile** to compile all language repositories.
* **vagrant up** to create a virtual machine.