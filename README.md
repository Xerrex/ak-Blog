# Ak-Blog

Simple Flask blog application which allows users to follow other users and view their posts. The app also has language translations to cater for a wide range of users.

* **[Acknowledgment](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)**

## Technologies/Tools used & needed.
* **[Python](https://www.python.org/downloads/)** - A programming language.
* **[Flask](flask.pocoo.org/)** - A microframework for Python.
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[SQLITE](https://www.sqlite.org/index.html)** - Small, fast, self-contained, high-reliability, full-featured, SQL DB.

* **[Vagrant](https://www.vagrantup.com/)** - Development Environments Made Easy.
* **[Docker](https://www.docker.com/) / [Docker-compose](https://docs.docker.com/compose/)** - set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.

## Table of contents

* [Installation or Deployment](#installation-or-Depolyment)
  * [Local Machine](#local-machine)
  * [Docker](#docker)
* [Usage](#usage)
* [Additional Information](#additional-Information)

## Installation or Deployment

### Local machine

* **NB**

  * Run the following commands on your terminal.
  * This commands are per a linux based OS.

* **Clone or download repo**

    ```bash

    git clone https://github.com/Xerrex/ak-Blog.git
    ```

* **Create virtual environment**

    ```bash

    virtualenv -p python3 venv
    ```

* **Environment variables.**

  * Copy .env file

    ```bash

    cp .env.examples .env
    ```

  * Edit the following lines on **.env** file.

    * Replace **your-** with your actual value.
      * export SECRET_KEY="your-secret-key"
      * export DATABASE_URL=""
      * export MS_TRANSLATOR_KEY="paste-your-key-here"
      * export ADMINS=["admin-email2","admin-email2"]
      * export MAIL_SERVER=smtp.googlemail.com
      * export MAIL_PORT=587
      * export MAIL_USE_TLS=1
      * export MAIL_USERNAME=your-gmail-username
      * export MAIL_PASSWORD=your-gmail-password
      * export REDIS_URL="your-ip-address:your-port"

    * To change Enviroment add
      * export FLASK_DEBUG=1

    * Activate virtual environment & export variables.
      * **source .env**

    * Install Dependancies now with virtual environment active.
      * pip install -r requirements.txt

* **Apply Database migrations**
  * flask db upgrade

* **Run the app**
  * flask run

### Docker

* **NB**
  * Pull individual docker images first for easier building, otherwise its not necessary

* **Create environment variable files for mysql and app files**
  * touch .envapp .envsql

* **Add/edit the following in the files**
  * **.envsql**

    ```python
    MYSQL_RANDOM_ROOT_PASSWORD=yes
    MYSQL_DATABASE=akblog
    MYSQL_USER=akblog
    MYSQL_PASSWORD="your-db-pass"
    ```

  * **.envapp**

    ```python
    FLASK_CONFIG=development #optional
    SECRET_KEY="your-secret-key"
    DATABASE_URL=mysql+pymysql://akblog:your-db-pass@dbserver/akblog
    MS_TRANSLATOR_KEY=your-ms key
    ADMINS="["admin-email-1"]"
    ELASTICSEARCH_URL=http://elasticsearch:9200
    FLASK_DEBUG=1 #optional
    MAIL_SERVER=smtp.googlemail.com
    MAIL_PORT=587
    MAIL_USE_TLS=1
    MAIL_USERNAME=your-gmail-username #optional
    MAIL_PASSWORD=your-gmail-password #optional
    REDIS_URL="redis://redis:6379/0"
    ```

    * remove optional lines if not using.
    * **your-db-pass** is same as the one defined in **.envsql**

* **Build/Run images**
  * **Build**
    * build images with the command:

      ```bash
      docker-compose build
      ```
  
  * **Run**
    * run the built images with:

      ```bash
      docker-compose up
      ```

## Usage

* **Access the app by going to the address with your browser**

  * [http://0.0.0.0:5000](http://0.0.0.0:5000)
  * [http://127.0.0.1:5000](http://127.0.0.1:5000)

* **To view database changes**
  * Uncomment the adminer part of the docker-compose.yml file

  ```yml
  # adminer:
  #     image: adminer:latest
  #     container_name: adminer
  #     restart: always
  #     ports:
  #         - 8080:8080
  ```

  * head over to this address with your browser.

    * [http://0.0.0.0:8080](http://0.0.0.0:8080)
    * [http://127.0.0.1:8080](htpp://127.0.0.1:8080)

  * Use the same login credentials as defined in **.envsql**

## Additional Information

App contains additional commands to help with language translations

* **flask translate init LANG** to add a new language. LANG is the new language
* **flask translate update** to update all language repositories.
* **flask translate compile** to compile all language repositories.
* **vagrant up** to create a virtual machine.
