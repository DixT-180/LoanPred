import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os
class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            print(features,"xxxx")
            print(type(features),'shape',features.shape)
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self, 
        Age:int,
                 
                 
        Gender: str,

        Experience:int,

        Income:float,
        Family:int,
        CCAvg:float, 
        Education:str,
        Mortgage:int,
        HomeOwnership:str):

        self.Age=Age
        self.Gender = Gender
        self.Experience = Experience
        self.Income = Income
        self.Family = Family
        self.CCAvg = CCAvg
        self.Education = Education
        self.Mortgage=Mortgage
        self.HomeOwnership = HomeOwnership


      
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age":[self.Age],

              
                "Gender": [self.Gender],
                "Experience":[self.Experience],
                "Income":[self.Income],
                "Family":[self.Family],
                "CCAvg":[self.CCAvg],
                "Education":[self.Education],
                "Mortgage":[self.Mortgage],
                "HomeOwnership":[self.HomeOwnership],


              
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

