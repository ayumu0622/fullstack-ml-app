from fastapi import FastAPI
from pydantic import BaseModel
from machine_learning.titanic import PredictOnAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
     CORSMiddleware,
     allow_origins = ['http://localhost:3000'],
     allow_methods = ["*"],
     allow_headers = ["*"]
)

@app.get('/helloworld')
def get_hello_message():
    return {"message": "Hello World!!"}

@app.get('/api/{message}')
def get_any_message(message: str):
    return {"message": message}

class SchemaOfTitanicFeaturesRequest(BaseModel):
     Sex: str
     Pclass: str
     Age: int
     Parch: int
     SibSp: int

class SchemaOfSurvivalProbabilityResponse(BaseModel):
     survival_probability: float

@app.post('/api/titanic', response_model=SchemaOfSurvivalProbabilityResponse)
def derive_score(request_body: SchemaOfTitanicFeaturesRequest):
     features_dict = request_body.__dict__
     survival_probability =  PredictOnAPI.derive_survival_probability(**features_dict)
     return {'survival_probability': survival_probability}


   

