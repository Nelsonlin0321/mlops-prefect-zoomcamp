# Deployment Workflow With Prefect

## Deployment Workflow

### deployment.yaml

```YAML
deployments:
- name: green-taxi-duration-training-with-local-data
  version: 1
  tags: []
  description: "The training pipeline of green taxi duration with local data"
  schedule: {}
  flow_name: null
  entrypoint: 3.4/orchestrate.py
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
  entrypoint: 3.5/orchestrate_s3.py
  parameters: {}
  work_pool:
    name: zooncamp-work-pool
    work_queue_name: default
    job_variables: {}
```

```sh
prefect deploy --all
```

```
prefect deployment run green_taxi_duration_training_with_s3/green-taxi-duration-training-with-s3-data
```
