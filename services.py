from application_factory import create_application
from bottle import request
from dynamodb import DynamoDB
from response import Response

import datetime
import json
import requests

application = create_application()
database = DynamoDB()


@application.get('/company/<cnpj>')
def get_by_cnpj(cnpj: str):
    try:
        partition_key = {
            'cnpj': cnpj
        }
        result = database.get_item(partition_key)['Item']
        data = {
            'data': result['content']
        }
        return Response(200).body(data).build()
    except Exception as e:
        error = {
            'error': str(e)
        }
        return Response(500).raise_request(error).build()


@application.get('/')
def health_check():
    try:
        data = {
            'data': {
                'application_name': 'Zup AWS Serverless',
                'version': '1.0.0'
            }
        }
        return Response(200).body(data).build()
    except Exception as e:
        error = {
            'error': str(e)
        }
        return Response(500).raise_request(error).build()


@application.post('/company')
def save():
    try:
        content = request.json
        cnpj = content['cnpj']
        result = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').json()
        data = dict({
            'cnpj': cnpj,
            'content': result,
            'creation_date': str(datetime.datetime.now)
        })
        database.put_item(data)
        return Response(201).body(data).build()
    except Exception as e:
        error = {
            'error': str(e)
        }
        return Response(500).raise_request(error).build()
