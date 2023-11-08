# Business Project

This project involves a web application that runs on Docker, implemented using Python and Django. It contains functionalities related to business management. Below are the steps for running the application and executing the test cases.

## Testing and Deployment Pipeline

Our GitHub Actions pipeline is configured to first execute the test cases and, upon successful completion, automate the deployment process to an EC2 instance. This ensures that any issues are identified and resolved before the software is deployed, enhancing the reliability of the deployment pipeline.

**Note:** Ensure that all these host, username, key, and port dependencies are configured securely in the GitHub repository secrets.
## Prerequisites

- Python 3.9
- Docker

## A) Running the Application

Ensure that Python and Docker are installed on your system. After that, navigate to the '/business-tasks' directory and execute the following command:

- sudo docker-compose up
  
### Access the Application

You can access the application by visiting the following link in your web browser:

[http://localhost:8000/myapp](http://localhost:8000/myapp)

Make sure the application is running before accessing the link.

The application will run on port 8000, and the endpoint is '/myapp'. Access the index page to interact with the application.

## B) Running Test Cases

To execute the test cases, use the following commands in the terminal:


- pip install -r requirements.txt 
- export DJANGO_SETTINGS_MODULE=businessproject.settings 
- pytest --cov=. --cov-report=html 


The test results will be displayed, including the coverage report.

## C) Direct Run

For a direct run of the application without Docker, use the following commands:

- pip install -r requirements.txt
- python3 manage.py runserver

## Videos

Two instructional videos are attached that provide further guidance on setting up and running the application.

Please refer to the videos for more detailed instructions on using the application.



