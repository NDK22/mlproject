## Student Performance Indicato End to End Machine Learning Project


This is a web application that predicts a student's math score based on various inputs such as gender, ethnicity, parental education level, lunch type, test preparation course, and scores in reading and writing. The application is built using Flask, a lightweight web framework for Python.


Prerequisites

- Python 3.8
- pip (Python package installer)
- AWS for Continuous Deployment and hosting

Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies

pip install -r requirements.txt

Alternatively, you can install the project using the setup script:

pip install .

Usage

Run the Application

python app.py

The application will start on [app](http://studentmathperformance-env-1.eba-pbmrfk2x.us-east-2.elasticbeanstalk.com/). Open this URL in your web browser to access the application.

Using the Application

1. Fill in the form with the required details:
    - Gender
    - Race or Ethnicity
    - Parental Level of Education
    - Lunch Type
    - Test Preparation Course
    - Writing Score
    - Reading Score

2. Click on the "Predict your Maths Score" button.

3. The predicted math score will be displayed on the screen.

Snapshot of the project:

![image](https://github.com/NDK22/mlproject/assets/121696401/78085c15-3be5-4190-82df-b34a04d357f9)

