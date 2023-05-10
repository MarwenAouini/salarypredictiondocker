# Utiliser une image Python de base
FROM python:3.11

# Copier les fichiers de l'API dans le conteneur
COPY ./requirements.txt /app/requirements.txt
# Installer les dépendances
RUN pip install -U -r /app/requirements.txt
#RUN pip install fastapi uvicorn spacy pandas joblib scikit-learn

# Copier les fichiers de l'API dans le conteneur
COPY ./SalaryModel.pkl /app/SalaryModel.pkl
COPY ./api /app/api

# Définir le répertoire de travail
WORKDIR /app


# Exposer le port 8000
EXPOSE 8000

# Lancer l'application avec uvicorn
ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]

