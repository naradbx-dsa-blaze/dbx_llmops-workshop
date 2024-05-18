# Databricks notebook source
from mlflow.deployments import get_deploy_client
import json
import time

client = get_deploy_client("databricks")
endpoint = client.get_endpoint(endpoint="dbdemos_fsi_fraud")

def check_state(endpoint):
    data = json.loads(endpoint)
    state = data.get('state', {}).get('ready', '')

    while state != 'READY':
        # Sleep for a while before checking again
        time.sleep(300)
        # Reload the data to get the updated state
        data = json.loads(endpoint)
        state = data.get('state', {}).get('ready', '')

    return 1
  
# Triggering the function
json_data = json.dumps(endpoint)
result = check_state(json_data)
