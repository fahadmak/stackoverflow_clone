[![Build Status](https://travis-ci.org/fahadmak/stackoverflow_clone.svg?branch=develop)](https://travis-ci.org/fahadmak/stackoverflow_clone)
[![Coverage Status](https://coveralls.io/repos/github/fahadmak/stackoverflow_clone/badge.svg?branch=develop)](https://coveralls.io/github/fahadmak/stackoverflow_clone?branch=develop)
# Stackoverflow Clone
Stack Overflow is a question and answer website for hobbyists, amateur and professional programmers. 

## Getting Started

```
Clone project from github
    $ git clone https://github.com/fahadmak/stackoverflow_clone.git
```

### Prerequisites

What you need to install the stackoverflow and how to install them

```
1. Install Python 3.7 or greater

2. Install virtualenv 
    $ pip install vitualenv
    
```

### Installing

```
1. Using the terminal navigate to project directory, and create a virtual enviroment
    $ virtualenv venv

2. Activate the virtual environment using this command
   Mac Os/Linux
    $ source venv/bin/activate
   
   Windows
    venv\Scripts\activate
    
3. Install project dependency from the requirements.txt file
    $ pip install -r requirements.txt
    
4. Run migrations
    $ python manage.py makemigrations
    $ python manage.py migrate
    
5. Create super user to access the system
    $ python manage.py createsupersuser (Follow prompt to enter Username, Email, Password and Confirm Password)
    
6. run development server to access the system
    $ python manage.py runserver
```

Output

```
Enter url in browser
    $ http://127.0.0.1:8000/
```


## Running the tests

```
To run test run the following command:
    $ python manage.py test
```

## Developed Using

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
