# LookUP
![Logo](https://raw.githubusercontent.com/drac-pro/LookUp/main/dynamic/static/images/L.png)

## Introduction

Welcome to `LookUP`, a comprehensive Business Directory Web Application. LookUP is designed to empower business owners to register and manage their businesses efficiently while providing a platform for users to discover and connect with a wide array of services and businesses.

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

To run LookUp on your local environment, clone the repo and run this command in the root directory of the project

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

sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
```

__Other python pakages run:__
`sudo pip3 install -r requirements.txt`


LookUp - Your Essential Services Locator
Welcome to LookUp! LookUp is a mobile application designed to help users find essential services around them, such as hospitals, pharmacies, police stations, and more. Whether you’re a traveler in a new city or a local in need of immediate assistance, LookUp is here to guide you.

