import os, requests
from client import get_token

token = os.environ.get("ibl_access_token", 'h2ugmj9MjEsBF6Nx6cFOj6jl4L9b4p')
def req(token=token):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'greeting' : 'hello',
    }
    response = requests.post("http://localhost:8000/api/greeting/", headers=headers, data=data)

    print(response.status_code)
    res = response.json()
    print(res)

    if response.status_code == 401:
        tok_req = get_token()
        print(tok_req)
        new_token = tok_req['access_token']
        os.environ['ibl_access_token'] = new_token

        req(token=new_token)
req()