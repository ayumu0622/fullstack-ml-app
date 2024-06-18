import numpy as np
import pandas as pd
from pathlib import Path
import pickle
import warnings
from sklearn.linear_model import LinearRegression

class GenerateModel:

    base_dir = Path(__file__).resolve().parent

    def __init__(self):
        pass

    @classmethod
    def __read_data(cls) -> pd.DataFrame:
        path_to_data = cls.base_dir / 'data' / 'train.csv'
        return pd.read_csv(path_to_data)

    @staticmethod
    def __extract_required_columns(df: pd.DataFrame):
        required_columns = ['Survived','Sex','Pclass','Age','Parch','SibSp']
        return df[required_columns]
    
    @staticmethod
    def encode_sex(x: str):
        if x in ('Male'):
            return 1
        elif x in ('Female'):
            return 0
        else:
            return np.nan

    @classmethod
    def __preprocess_df(cls, df: pd.DataFrame) -> pd.DataFrame:
        tmp_df = cls.__extract_required_columns(df)
        tmp_df = tmp_df.dropna().reset_index(drop=True)
        tmp_df['Sex'] = tmp_df['Sex'].apply(lambda x: cls.encode_sex(x))
        return tmp_df

    @staticmethod
    def __train_model(df: pd.DataFrame):

        y = df['Survived']
        X = df.drop(['Survived'], axis=1)
        
        model = LinearRegression()
        model.fit(X.values, y.values)

        return model

    @classmethod
    def __save_model(cls, model):
        
        path_to_model = cls.base_dir / 'model' / 'model.pkl'
        with open(path_to_model, "wb") as f:
            pickle.dump(model, f)

    @classmethod
    def generate_model(cls):
        df = cls.__read_data()
        preprocessed_df = cls.__preprocess_df(df)
        lgbm_model = cls.__train_model(preprocessed_df)
        cls.__save_model(lgbm_model)


class PredictOnAPI(GenerateModel):
 
     def __init__(self):
         pass
 
     @classmethod
     def __load_model(cls):
 
         path_to_model = cls.base_dir / 'model' / 'model.pkl'
         if path_to_model.exists() == False:
             print('model does not exist')
             cls.generate_model()

         with open(path_to_model, "rb") as f:
             model = pickle.load(f)
 
         return model

     @staticmethod
     def __encode_pclass(x: str):
         if x == 'Upper class':
             return 1
         elif x == 'Middle class':
             return 2
         elif x == 'Lower class':
             return 3
         else:
             return np.nan
 
     @classmethod
     def derive_survival_probability(
         cls,
         Sex: str,
         Pclass: str,
         Age: int,
         Parch: int,
         SibSp: int
     ) -> float:
 
         
         model = cls.__load_model()
 
         encoded_sex = cls.encode_sex(Sex)
         encoded_pclass = cls.__encode_pclass(Pclass)
 
         features = np.array([[
             encoded_sex, encoded_pclass, Age, Parch, SibSp
         ]])
 
         survival_probability = model.predict(features)
         logit = float(survival_probability[0])
         return logit 
