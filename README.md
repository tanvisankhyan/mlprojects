
## Student Performance Predictor


## Project Structure

Student_Performance_Predictor

        │
        ├── .github/
        │   └── workflows/
        │       └── main_studentperformancepredictor.yml
        │
        ├── artifacts/
        │   ├── model.pkl
        │   ├── preprocessor.pkl
        │   ├── train.csv
        │   ├── test.csv
        │
        ├── data/
        │   └── students.csv
        │
        ├── notebook/
        │   ├── 1. EDA STUDENT PERFORMANCE.ipynb
        │   ├── 2. MODEL TRAINING.ipynb
        │
        ├── src/
        │   ├── components/
        │   │   ├── data_ingestion.py
        │   │   ├── data_transformation.py
        │   │   └── model_trainer.py
        │   │
        │   ├── pipeline/
        │   │   ├── train_pipeline.py
        │   │   └── predict_pipeline.py
        │   │
        │   ├── utils.py
        │   ├── logger.py
        │   └── exception.py
        │
        ├── templates/
        │   ├── home.html
        │   └── index.html
        │
        ├── application.py
        ├── requirements.txt
        ├── setup.py
        ├── .gitignore
        └── README.md


## Dataset Information

- gender : sex of students  -> (Male/female)
- race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
- parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)
- lunch : having lunch before test (standard or free/reduced) 
- test preparation course : complete or not complete before test
- math score
- reading score
- writing score

- Categories in 'gender' variable:      ['female' 'male']
- Categories in 'race_ethnicity' variable:   ['group B' 'group C' 'group A' 'group D' 'group E']
- Categories in'parental level of education' variable: ["bachelor's degree" 'some college' "master's degree" "associate's degree" 'high school' 'some high school']
- Categories in 'lunch' variable:      ['standard' 'free/reduced']
- Categories in 'test preparation course' variable:      ['none' 'completed']

- We have 3 numerical features : ['math_score', 'reading_score', 'writing_score']
- We have 5 categorical features : ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']



## Algorithms Used

 - Random Forest (RandomForestRegressor)
 - Decision Tree (DecisionTreeRegressor)
 - Gradient Boosting (GradientBoostingRegressor)
 - Linear Regression (LinearRegression)
 - XGBoost Regressor (XGBRegressor)
 - CatBoost Regressor (CatBoostRegressor with verbose=False)
 - AdaBoost Regressor (AdaBoostRegressor)


## Deployment

This project is deployed using GitHub Actions to Azure App Service. The deployment process is automated through a GitHub Actions workflow.
 - GitHub — where the code lives ✅
   
# Steps:

1. **Set up Azure App Service**:
   - Create an App Service on Azure if you already have one.
2. **GitHub Actions Workflow**:
   The app is deployed automatically using the GitHub Actions workflow in `.github/workflows/main_studentperformancepredictor.yml` upon pushing to the `main` branch. The workflow does the following:
   - Installs dependencies.
   - Deploys to Azure App Service.
4. **Push Changes**:
   Push changes to the `main` branch. GitHub Actions will handle the deployment process automatically.

Once deployed, the app will be available at the Azure App Service URL.

