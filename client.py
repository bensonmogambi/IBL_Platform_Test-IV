import requests
from base64 import b64encode

url = 'http://localhost:8000/o/token/'
data = {
    'grant_type': 'password',
    'username': 'Amoo',
    'password': 'taslim100'
}
client_id = 'XQL9I7Z4ifVszYriuxtjjybBpgA4Rlb3Z9P9lMiw'
client_secret = 'taslim'

credentials = f'{client_id}:{client_secret}'
encoded_credentials = b64encode(credentials.encode('utf-8')).decode('utf-8')
headers = {
    'Authorization': f'Basic {encoded_credentials}'
}

def get_token():
    response = requests.post(url, data=data, headers=headers)
    return response.json()

# res = get_token()
# print(res.json())