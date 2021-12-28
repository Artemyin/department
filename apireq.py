import requests
import json
from datetime import date, datetime
from pprint import pprint

def post_to_department():
    url = "http://127.0.0.1:5000/api/v1/departments/" 

    param_dict = {'name': 'AAAsss'}
    
    data = json.dumps(param_dict)
    print(data)
    response = requests.post(url, json=param_dict)
    pprint(response)
    pprint(response.headers)
    pprint(response.status_code)
    pprint(response.json())

def get_to_department():
    url = "http://127.0.0.1:5000/api/v1/departments/12" 
    response = requests.get(url)
    pprint(response)
    pprint(response.headers)
    pprint(response.status_code)
    pprint(response.json())

def post_to_employee():
    url = "http://127.0.0.1:5000/api/v1/employees/" 

    param_dict = {'name': 'Merriam Webster',
        'birthdate': '1986-06-22', 
        'salary': 100,
        #'department': 4,
        }
    
    print(param_dict.get('birthdate'))
    print(datetime.strptime(param_dict.get('birthdate'), '%Y-%m-%d'))

    data = json.dumps(param_dict)
    print(data)
    response = requests.post(url, json=param_dict)
    pprint(response)
    pprint(response.headers)
    pprint(response.status_code)
    pprint(response.json())


#get_to_department()

post_to_employee()

