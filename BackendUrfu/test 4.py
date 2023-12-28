import requests

url = 'http://localhost:5000/clear'
response = requests.delete(url + "/2")

if response.status_code == 200:
    print('Удаление товара')
else:
    print('Увы')