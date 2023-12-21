from io import BytesIO

import requests
import base64
from PIL import Image

product_id = 1
url = 'http://localhost:5000/'

response = requests.get(url + f'product/{product_id}')

if response.status_code == 200:
    product_info = response.json()
    print('Информация о продукте:')
    print(product_info['id'])
    print(product_info['user_id'])
    print(product_info['description'])
    print(product_info['date'])
    print(product_info['price'])
else:
    print('Жаль')

decoded_image_data = base64.b64decode(product_info['photo'])
decoded_image = Image.open(BytesIO(decoded_image_data))
decoded_image.save('decoded_image.jpg')


response = requests.get(url + 'products')
product_info = response.json()
print(len(product_info))