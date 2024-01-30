# Django from the scratch

## Machine Setup

1.  Install Python in the system from the site [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  Install git from the site [https://git-scm.com/downloads](https://git-scm.com/downloads)

3.  Install VS Code from the site [https://code.visualstudio.com/download](https://code.visualstudio.com/download)



## Getting access to Git code from local machine

### Using SSH keys

1.  In the terminal paste the below text, replacing the email used in the example with your GitHub email address
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    This command will create a new SSH key using the email as a label

2.  You will then be prompted to "Enter a file in which to save the key.".

    You can specify a file location or press “Enter” to accept the default file location.

3.  Add the new SSH key to the ssh-agent
    ```bash
    ssh-add -K /Users/you/.ssh/id_rsa
    ```

4.  Add this ssh key into the Github/Gitlab


## For a new project

### Project setup


1.  Install django into the machine using the following command
    ```bash
    pip install django
    ```

2.  Create a new Django project
    ```bash
    django-admin startproject project
    ```
    Note we can keep any name in place of 'project'

    

3.  Navigate to the project directory
    ```bash
    cd project
    ```

4.  Create a virtual environment
    For Windows,
    ```bash
    python3 venv venv
    ```

    For Linux,
    ```bash
    virtualenv venv
    ```

5.  Activate the virtual enviroment
    For Windows,
    ```bash
    . venv\scripts\activate
    ```

    For Linux,
    ```bash
    source venv/bin/activate
    ```

### Installation

1.  Install django

    ```bash
    pip install django
    ```

2.  Install Django Rest Framework
    ```bash
    pip install djangorestframework
    ```

3.  Start a Django app
    ```bash
    django-admin startapp user
    ```

4.  Install mysqlclient
    ```bash
    pip install mysqlclient
    ```
    If we get error while installation of mysqlclient we should paste the following code in the init.py file

    ```bash
       import pymysql
       pymysql.install_as_MySQLdb()
    ```


### Migrations

1.  Make migrations
    ```bash
    python manage.py makemigrations
    ```

2.  Migrate
    ```bash
    python manage.py migrate
    ```

### Run the project

    Run the project
    ```bash
    python manage.py runserver
    ```

## For this existing project

1.  Clone the repository
    ```bash
    [Django Github Repository](https://github.com/UtkJaiswal/Django-CRUD-Form)
    ```

2.  Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the project
    ```bash
    python manage.py runserver
    ```

4.  The server is running at [http://localhost:8000](http://localhost:8000)

