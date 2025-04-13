## Project Structure

Student_Performance_Predictor/

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




## Deployment

This project is deployed using GitHub Actions to Azure App Service. The deployment process is automated through a GitHub Actions workflow.


GitHub — where the code lives ✅


# Steps:

1. **Set up Azure App Service**:
   - Create an App Service on Azure if you already have one.


2. **GitHub Actions Workflow**:
   The app is deployed automatically using the GitHub Actions workflow in `.github/workflows/main_studentperformancepredictor.yml` upon pushing to the `main` branch. The workflow does the following:
   - Installs dependencies.
   - Deploys to Azure App Service.

4. **Push Changes**:
   Push changes to the `main` branch. GitHub Actions will handle the deployment process automatically.

Once deployed, your app will be available at the URL provided by Azure App Service.

