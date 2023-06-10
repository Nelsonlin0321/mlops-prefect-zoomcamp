# MLOps Zoomcamp 2023 Week 3

![Prefect logo](./images/logo.svg)

---

This repo contains Python code to accompany the videos that show how to use Prefect for MLOps. We will create workflows that you can orchestrate and observe..

# Setup

## Clone the repo

Clone the repo locally.

## Install packages

In a conda environment with Python 3.10.12 or similar, install all package dependencies with 

```bash
pip install -r requirements.txt
```
## Start the Prefect server locally

Create another window and activate your conda environment. Start the Prefect API server locally with 

```bash
prefect server start
```



## Optional: use Prefect Cloud for added capabilties
Signup and use for free at https://app.prefect.cloud


##  Prefect Workflow Deployment


### Step 1:
```
prefect preject init
```


### Step 2:prefect.yaml
Define the CICD pipeline and github setting
```yaml
# File for configuring project / deployment build, push and pull steps

# Generic metadata about this project
name: mlops-prefect-zoomcamp
prefect-version: 2.10.11

# build section allows you to manage and build docker images
build: null

# push section allows you to manage if and how this project is uploaded to remote locations
push: null

# pull section allows you to provide instructions for cloning this project in remote locations
pull:
- prefect.projects.steps.git_clone_project:
    repository: git@github.com:Nelsonlin0321/mlops-prefect-zoomcamp.git
    branch: main
    access_token: null
```

### Step 3: deployment.yaml

Define what workflow to deploy with setting in this project

```yaml
deployments:
- name: green-taxi-duration-training-with-local-data
  version: 1
  tags: []
  description: "The training pipeline of green taxi duration with local data"
  schedule: {}
  flow_name: null
  entrypoint: 3.4/orchestrate.py:green_taxi_duration_training_with_local_data
  parameters: {}
  work_pool: 
    name: zooncamp-work-pool
    work_queue_name: default
    job_variables: {}

- name: green-taxi-duration-training-with-s3-data
  version: 1
  tags: []
  description: "The training pipeline of green taxi duration with s3 data"
  schedule: {}
  flow_name: null
  entrypoint: 3.5/orchestrate_s3.py:green_taxi_duration_training_with_s3_data
  parameters: {}
  work_pool: 
    name: zooncamp-work-pool
    work_queue_name: default
    job_variables: {}

```

### Step 4:  Start worker that polls your work poll

#### By CLI
```sh
prefect worker start -p zooncamp-work-pool -t process
```

### Step 5: Deploy workflow by specify python file
```sh
prefect deploy 3.4/orchestrate.py:green_taxi_duration_training_with_local_data -n green-taxi-duration-training-with-local-data -p zooncamp-work-pool
```

```sh
prefect deploy 3.5/orchestrate_s3.py:green_taxi_duration_training_with_s3_data -n green-taxi-duration-training-with-s3-data -p zooncamp-work-pool
```

#### By YAML 
```sh
prefect deploy --all
```

### Step 5: Run Workflow

```sh
prefect deployment run green-taxi-duration-training-with-s3-data/green-taxi-duration-training-with-s3-data
```

![Prefect logo](images/Activity-create-run-deployment.png)

