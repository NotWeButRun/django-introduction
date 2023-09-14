import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["create", "read_all", "read", "update", "update_or_create", "delete"])
parser.add_argument("--pk", default=1, type=int)

args = parser.parse_args()
mode = args.mode
pk = args.pk

body = {
    "user_name": "テストユーザ",
    "birth_day": "2020-01-01",
    "age": 20,
    "created_at": "2020-01-01 00:00:00",
}

body_modified = {
    "user_name": "修正後ユーザ",
    "birth_day": "1920-01-01",
    "age": 120,
    "created_at": "1920-01-01 00:00:00",
}

body_partial = {
    # "user_name": False,
    # "birth_day": False,
    "age": 20,
    "created_at": "2220-01-01 00:00:00",
}

if mode == "create":
    response = requests.post('http://127.0.0.1:8000/api/userInfo/', body)
    print(response.text)
    
elif mode == "read_all":
    response = requests.get('http://127.0.0.1:8000/api/userInfo/')
    print(response.text)

elif mode == "read":
    response = requests.get(f'http://127.0.0.1:8000/api/userInfo/{pk}/')
    print(response.text)


elif mode == "update":
    response = requests.patch(f'http://127.0.0.1:8000/api/userInfo/{pk}/', body_modified)
    print(response.text)

elif mode == "update_or_create":
    response = requests.put(f'http://127.0.0.1:8000/api/userInfo/{pk}/', body_modified)
    print(response.text)


elif mode == "delete":
    response = requests.delete(f'http://127.0.0.1:8000/api/userInfo/{pk}/')
    print(response.text)

