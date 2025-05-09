# all the code - related to reading the data
# train and test
# read the data from the data sources

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTranformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', "train.csv")
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  #When we call DataIngestion class the three paths above will be saved in the ingestion_config varaible

    def initiate_data_ingestion(self):   #ew will write the code to read the data from the sources
        logging.info("Entered the data ingestion method or compnents")
        try:
            df=pd.read_csv("notebook\data\students.csv")
            logging.info('Read the dataset as a dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)                
            logging.info("Train Test Split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Data Ingestion completed")
            return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                )
                

        except Exception as e:
            raise CustomException(e, sys)
            
if __name__=="__main__":
    obj= DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTranformation()
    train_arr, test_arr,_= data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
