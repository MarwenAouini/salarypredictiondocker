# Salary Prediction App On Docker

* run python model/Model.py to create .pkl
* Now everything should be ready to run locally. Go in the root of the project, and run uvicorn api.main:app --host 0.0.0.0 --port 8000
* You can access it via this link http://localhost:8000/docs after starting the API locally.

# docker (local)

* docker-compose up --build 

# git (CI/CD)
* click on setup a workflow yourself. A YAML file will be automatically created inside a workflowsfolder which will be created in a .github folder at the root of the repo.
* In our case, we will set the workflow to be triggered on push requests only on the main branch.
* The job that will be triggered will be run on a remote server that GitHub Actions will connect to through the SSH Remote Commands. In other situations, this job may run on Github runners, i.e. instances provided by Github (SSH Remote Commands is a custom GitHub Action that you can find from the marketplace. It’s free to use, you’ll just have to call it after the uses section).
* The SSH Remote Commands Github Action will be called with the following arguments
    + host: the hostname of the server (i.e. its public IP)
    + username: the ssh username
    + key: the content of ssh private key
# AWS 


