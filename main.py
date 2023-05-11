from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

# Loading the Machine Learning Model
model = load("./SalaryModel.pkl")

# Définir une classe modèle pour l'entrée de l'API
class ExperienceInput(BaseModel):
    experience: float

# Créer une instance de l'application FastAPI
app = FastAPI()

# Définir une route POST pour l'API
@app.post("/predict")
def predict_salary(input_data: ExperienceInput):
    experience = input_data.experience
    result = model.predict([[experience]])
    salary = round(result[0], 2)
    return {"estimated_salary": salary}

@app.get("/")
def hello():
    return {"message": "Hello, I am an API!"}

# Exécuter l'application avec uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
