## Student Performance Indicator End to End Machine Learning Project


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

MLprpject/
|
|── .ebextensio/
|    |── python.config                      # config file for AWS Deployment in Elastic Bean and CodePipeline for Continuous Deployment
|── artifacts/
|    ├── data.csv                           # Metadata csv
|    ├── train.csv                          # Training data csv
|    ├── test.csv                           # Testing data csv
|    ├── model.pkl                          # Saved Best Model
|    ├── preprocessor.pkl                   # Saved Preprocessing file for new data
|── notebook/
|   |── EDA Student Performance.ipyb        # Jupyter file to do exploratory data analysis of the data being used to create the model
|   |── Model Training.ipyb                 # Jupyter file to structure how we will be training the data using various machine learning algorithm
├── application.py                          # Main application script
├── requirements.txt                        # Project dependencies
├── setup.py                                # Setup script for packaging
├── templates/
│   └── home.html                           # HTML template for the form and result display
├── src/
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py             # Prediction pipeline script
│   │   
|   |── components/
|   |   |── data_ingestion.py               # Data Ingestion script
|   |   |── data_transformation.py          # Data Transformation script
|   |   |── model_trainer.py                # Model Training Script
|   |── exeption.py                         # Script for Custom Exception handling for error messages
|   |── logger.py                           # Script for logging
|   |── utils.py                            # Scripts to have functions used in various other scripts
└── README.txt                              # Project README file

Machine learning Algorithms used:
|── CatBoostRegressor
|── AdaBoostRegressor
|── GradientBoostingRegressor
|── RandomForestRegressor
|── LinearRegression
|── DecisionTreeRegressor
|── XGBRegressor

The model's performance was evaluated using r2 score.
The model was hyperparameters tuned. 
The best model model was selected using GridSearchCV


Snapshot of the project:


![image](https://github.com/NDK22/mlproject/assets/121696401/78085c15-3be5-4190-82df-b34a04d357f9)

