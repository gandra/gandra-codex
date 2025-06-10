import os
import requests
from dotenv import load_dotenv

load_dotenv()

AUTH_SERVER = os.getenv('AUTH_SERVER', 'http://localhost:9000')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_token():
    data = {'grant_type': 'client_credentials'}
    return requests.post(f"{AUTH_SERVER}/oauth2/token", data=data, auth=(CLIENT_ID, CLIENT_SECRET)).json()['access_token']

def call_api(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    return requests.get(url, headers=headers).json()

if __name__ == '__main__':
    token = get_token()
    print('Access token:', token)
    cities = call_api(token, 'http://localhost:8082/countries')
    print(cities)
