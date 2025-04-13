## Project Architecture

Student_Performance_Predictor/ │ ├── .github/ │ └── workflows/ │ └── main_studentperformancepredictor.yml # GitHub Actions workflow for deployment │ ├── artifacts/ # Trained model, preprocessor, and datasets │ ├── model.pkl │ ├── preprocessor.pkl │ ├── train.csv │ ├── test.csv │ ├── data/ │ └── students.csv # Raw input data │ ├── notebook/ │ ├── 1. EDA STUDENT PERFORMANCE.ipynb # Exploratory data analysis │ ├── 2. MODEL TRAINING.ipynb # Model development and training │ ├── src/ │ ├── components/ │ │ ├── data_ingestion.py │ │ ├── data_transformation.py │ │ └── model_trainer.py │ │ │ ├── pipeline/ │ │ ├── train_pipeline.py │ │ └── predict_pipeline.py │ │ │ ├── utils.py │ ├── logger.py │ └── exception.py │ ├── templates/ │ ├── home.html │ └── index.html # HTML templates for the UI │ ├── application.py # Flask application entry point ├── requirements.txt # Python dependencies ├── setup.py # Project packaging setup ├── .gitignore └── README.md


## ML project


AWS Deployment
Step 1: create Elastic beanstalk instance. create environment
step2: Create code pipeline to inegrate github repositoryand continue the deployment in the elastic beanstalk.

GitHub — where the code lives ✅

CodePipeline — listens to GitHub and starts the deployment

Elastic Beanstalk — deploys and runs the app

IAM roles — let AWS services securely talk to each other