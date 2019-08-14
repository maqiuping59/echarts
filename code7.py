import requests

response = requests.get('https://www.baidu.com/')
print(response.text)
print(response.content)
print(response.apparent_encoding)
print(response.cookies)
print(response.links)
print(response.status_code)
print(response.headers)