# Student Performance Indicator End to End Machine Learning Project

This is a web application that predicts a student's math score based on various inputs such as gender, ethnicity, parental education level, lunch type, test preparation course, and scores in reading and writing. The application is built using Flask, a lightweight web framework for Python.

## Prerequisites

- Python 3.8
- pip (Python package installer)
- AWS for Continuous Deployment and hosting

## Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively, you can install the project using the setup script:

```bash
pip install .
```

## Usage

### Run the Application

```bash
python application.py
```

The application will start on [http://localhost:5000](http://localhost:5000). Open this URL in your web browser to access the application.

### Using the Application

1. Fill in the form with the required details:
    - Gender
    - Race or Ethnicity
    - Parental Level of Education
    - Lunch Type
    - Test Preparation Course
    - Writing Score
    - Reading Score

2. Click on the "Predict your Math Score" button.

3. The predicted math score will be displayed on the screen.

## Project Structure

```markdown
MLproject/
├── .ebextensions/
│   └── python.config                # Config file for AWS Deployment in Elastic Beanstalk and CodePipeline for Continuous Deployment
├── artifacts/
│   ├── data.csv                     # Metadata CSV
│   ├── train.csv                    # Training data CSV
│   ├── test.csv                     # Testing data CSV
│   ├── model.pkl                    # Saved Best Model
│   ├── preprocessor.pkl             # Saved Preprocessing file for new data
├── notebook/
│   ├── EDA Student Performance.ipynb # Jupyter file for exploratory data analysis
│   ├── Model Training.ipynb          # Jupyter file for model training
├── application.py                   # Main application script
├── requirements.txt                 # Project dependencies
├── setup.py                         # Setup script for packaging
├── templates/
│   └── home.html                    # HTML template for the form and result display
├── src/
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py      # Prediction pipeline script
│   ├── components/
│   │   ├── data_ingestion.py        # Data Ingestion script
│   │   ├── data_transformation.py   # Data Transformation script
│   │   ├── model_trainer.py         # Model Training Script
│   ├── exception.py                 # Script for Custom Exception handling
│   ├── logger.py                    # Script for logging
│   ├── utils.py                     # Utility functions
└── README.md                        # Project README file
```

## Machine Learning Algorithms Used

- CatBoostRegressor
- AdaBoostRegressor
- GradientBoostingRegressor
- RandomForestRegressor
- LinearRegression
- DecisionTreeRegressor
- XGBRegressor

The model's performance was evaluated using r2 score. The model was hyperparameter tuned, and the best model was selected using GridSearchCV.

## Snapshot of the Project

![Snapshot](https://github.com/NDK22/mlproject/assets/121696401/78085c15-3be5-4190-82df-b34a04d357f9)


