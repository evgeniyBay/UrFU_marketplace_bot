import requests

url = 'http://localhost:5000/clear'
response = requests.delete(url)

if response.status_code == 200:
    print('Database cleared successfully')
else:
    print('Failed to clear database')