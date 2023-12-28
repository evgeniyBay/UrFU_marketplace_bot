import requests
import base64


image_path = 'фото1.jpg'
with open(image_path, 'rb') as file:
    image_data = file.read()

encoded_image = base64.b64encode(image_data).decode('utf-8')
url = 'http://localhost:5000/'

product_data = {
    'name': 'Тест50',
    'price': 124311,
    'description': 'Потестить',
    'photo': encoded_image,
    'user_id': '13',
    'date': '2022-12-31'
}

response = requests.post(url + 'product', json=product_data)
if response.status_code == 201:
    print('Продукт создан')
else:
    print('Что то не так')

