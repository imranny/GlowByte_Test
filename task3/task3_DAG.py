import json
import csv
import requests

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Imran',
    'start_date': datetime(2025, 8, 4)
}

def extract_data():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()

def transform_data(**kwargs):
    ti = kwargs['ti']
    users_data = ti.xcom_pull(task_ids='extract')
    
    transformed = []
    for user in users_data:
        transformed.append({
            'id': user['id'],
            'name': user['name'],
            'email': user['email']
        })
    return transformed

def load_data(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='transform')

       
    with open('output/users.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'email'])
        writer.writeheader()
        writer.writerows(data)

with DAG(
    'GlowByte_etl_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_data,
    )

    extract >> transform >> load
