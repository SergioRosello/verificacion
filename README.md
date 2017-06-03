# Verification
## Description
Project to simulate real-life development of a web app.
Including unit tests, mock tests, BDD tests and continuous integration and deployment.  
Developed in Ubuntu 16.04.
## Technologies used
* Python 2.7
* VirtualENV
* MongoDB
* Lettuce
* Selenium web driver
* Jenkins
* HTML5
* Bootstrap
* Git

## About the app
The app is a web scrapper with a front-end that allows the user to introduce a URL. The app then proceeds to parse the content of the URL and creates an ordered list with the word that appears the most and the times it appears. Followed by the remaining words in decreasing order. These results are also uploaded to the database. Every section of the app has been tested with it's respective test. Including continuous integration and development process.
## Setup
```
    virtualenv ENV
    source ENV/bin/activate
    pip install requirements.txt
```
If MongoDB is not installed in your machine, you have to install it first.  
You can use this command:
```
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
    echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
    sudo apt-get update
    sudo apt-get install -y mongodb-org
```


## Deploying the app
```
    python code/application.py
```
##TODO:
* coverage on all of the scripts
* Give user feedback when database is down

## Tests
### Unit Tests
In the root directory:
```
    nosetests tests/tests_text_analyzer.py
```
### Mock tests
In the root directory (If MongoDB is installed in your machine):
```
    nosetests tests/tests_db_connection.py
```
### BDD tests
In the root directory, run application.py

```
    python code/application.py
```
While application.py is running:

```
    lettuce tests/features
```

## Runing coverages
### text_analyzer
```
    coverage run -m tests.tests_text_analyzer
```
After the script has finished, you can use the command below to find out the coverage percentage and areas where the code hasn't been covered.
```
    coverage html code/text_analyzer.py 
```
### url_scrapper
```
    coverage run -m tests.test_url_scrapper
```
After the script has finished, you can use the command below to find out the coverage percentage and areas where the code hasn't been covered.
```
    coverage html code/url_scrapper.py
```
### db_connection
```
    nosetests --with-coverage tests/tests_db_connection.py --cover-package=code.db_connection --cover-html
```
After the script has finished, you can use the command below to find out the coverage percentage and areas where the code hasn't been covered.
```
    chromium-browser cover/index.html
```