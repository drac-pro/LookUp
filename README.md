# LookUP
![Logo](https://raw.githubusercontent.com/drac-pro/LookUp/main/dynamic/static/images/L.png)

## Introduction

Welcome to `LookUP`, a comprehensive Business Directory Web Application. LookUP is designed to empower business owners to register and manage their businesses efficiently while providing a platform for users to discover and connect with a wide array of services and businesses.

This is a portfolio project at the end of fundation phase of ALX SE.

## The Team

1. Darius Seivinyuy Tohtin

2. Awugo Agabi Therese-Claire

3. Emmanuel Francis

## Application Overview

**LookUP allows users to:**

- **Register as Business Users:** Sign up to manage and showcase your business.
- **Manage Business Profiles:** Add, update, and maintain detailed business information
- **Service Listings:** Businesses can provide detailed descriptions of their services
- **Account Management:** Manage personal and business profiles, including profile pictures.
- **View Business Listings:** Browse through all registered businesses and access detailed business profiles.

## Key Features
- User Registration and Login: Secure sign-up and login functionality for business users.
- Business Profile Management: Add and update business details like name, description, and address.
- Service Listings: Showcase the services your business offers.
- Personal Account Management: Update personal information and profile pictures.
- Comprehensive Business Listings: Users can browse and access detailed business profiles.

## Users of LookUP

1. Business Owners:

	* Sign Up and Login: Register and log in to manage business details.
	* Business Profile Management: Add and maintain detailed business information including name, description, address, and services.
	* Account Management: Update personal information and manage profile pictures.

2. General Users:

	* Search for Businesses: Search for a businesses based on service offered and location
	* Browse Businesses: View a comprehensive list of all registered businesses.
	* Business Details: Access detailed profiles for each business including services offered.

## Running LookUP Locally

To run LookUp on your local environment, clone the repo and run this command in the root directory of the project.

***Command:*** 
``` 
LOOKUP_MYSQL_USER=lookup_dev LOOKUP_MYSQL_PWD=lookup_dev_pwd123 LOOKUP_MYSQL_HOST=localhost LOOKUP_MYSQL_DB=lookup_dev_db python3 run.py
```
***Both first we need to setup some few things***

### Required Pakages and Dependencies


__python and MySQLdb__:

```
sudo apt update
sudo apt install python3

sudo apt-get install pkg-config
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
```


__Other python pakages run:__

```
sudo pip3 install -r requirements.txt
```
[requirements](./requirements.txt)

On the root directory of the project


__Database - MySQL:__
To set up the database for the back end run this commands

```
sudo apt install mysql-server
sudo service mysql start
```

*After that run this to Create a user and database for LookUP*

```
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
```
[sql script](./setup_mysql_dev.sql)

You can run [This now](#running-lookup-locally)  
  

## Key Components

| Component | Description |
|-----------|-------------|
| [base_model.py](./models/base_model.py) | A base class from which all other objects in our web app inherits from |
| [db_storage.py](./models/engine/db_storage.py) | Creates a connection to the database and links the objects define in [models](./models) to the database |
| [routes.py](./dynamic/routes.py) | contains our web aplication route and business logic |
| [forms.py](./dynamic/forms.py) | Flask forms which are used by templates to collect, add, edit Business User info |
| [layout.html](./dynamic/templates/layout.html) | The base template of all other template also contains important bootstrap links |
| [run.py](./run.py) | Runs the entire application see [ Running LookUP Locally](#running-lookup-locally) |

## Helpful Resources 

Here are some resources to help you understand the technologies used in LookUP:
- Flask Documentation: [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- SQLAlchemy Documentation: [SQLAlchemy](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- bootstrap Documentation: [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- [Video](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)  


## License

[MIT License](./LICENSE)
