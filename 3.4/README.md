# Deployment Workflow With Prefect

## Deployment Process

<img src="../images/Activity-create-run-deployment.png"><img>

### Step 1:

```sh
prefect project init
```

#### prefect.yaml

```YAML
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

```sh
prefect deploy --help

prefect deploy 3.4/orchestrate.py:main_flow -n "nyc-taxi-green-duration-ml-training" -p zooncamp-work-pool

prefect worker start --pool 'zooncamp-work-pool'


```
