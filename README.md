# bookstore
An online web application bookstore that will allow user to purchase the books, search for books, and more features.

# Teammates: 
**Jermel Stuart, Marjorie Suarez, Michael Trachtenberg, HouyHour Ung, Fabio Velasquez, Bryan Virgil**

# Live demo of the section which I developed:
https://www.youtube.com/watch?v=K8vAbcowUH4

## Getting Started For Windows:
### 1. Download/install python 3.6+

### 2. Create/activate virtual environment CMD. Within project root directory run the commands: 
Windows:
* py -m venv .\venv  
* .\venv\Scripts\activate  
* (deactivate closes venv)

MacOS:
*creating the virtual environment: python3 -m venv env
*activate the virtual environment: source env/bin/activate (make sure that you are in the correct directory)
*exiting the virtual environment: Ctrl + C into the terminal


### 3. To install dependencies, inside active venv run:  
* pip install -r requirements.txt  

### 4. Runserver in venv:   
* python manage.py runserver  
* (CTRL+C closes server)  

To check that the page is working, visit http://localhost:8000/  

## Connecting database
Requirements: Have postgreSQL and pgAdmin4 installed and there should be a default server. 

### 1. Create a new server
* Right click on the default server and select 'create new server'
* Name the server 'CENProject'
* Right click on 'CENProject' and create a new database
* Name the database 'bookstoredb'

### 2. Restore database
* Download the 'bookstoredb' file from the shared google drive
* Right click on 'bookstoredb' and select 'restore'
* In the format row select 'custom or tar'
* Under file, find the location of the file and select the file.
* NOTE: Confirm that on bottom right, the format selected is 'All Files'
* Under Role name select 'postgres'
