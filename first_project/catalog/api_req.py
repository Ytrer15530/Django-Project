import requests

URL = "http://127.0.0.1:8000/api/goods/?format=json"
JWT = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxODY3Mjk4LCJpYXQiOjE3MDE0MzUyOTgsImp0aSI6ImQ5NTE1ZGNlNDIyZDQ3ODA5YWMxYTE3Yzg2NGEwYjBiIiwidXNlcl9pZCI6MX0.0pvK8lcHUN37PJKgrW_HBgalg187E0a2xDlTyeTWiyI'


def get_category():
    req = requests.get(URL, headers={'Authorization': f'Bearer {JWT}'})
    print(req.json())
    if req.status_code == 200:
        for item in req.json():
            print(item)


json = [{
    "id": 100,
    "name": "bimba"
},
{
    "id": 102,
    "name": "bimba2"
}]

for item in json:
    print(item['name'])

list_name = [item['name'] for item in json]

Parametr.objects.bulk_create(list_name)