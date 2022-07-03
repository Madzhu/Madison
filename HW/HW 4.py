import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)  # Объект библиотеки
json_data = response.content.decode()  # строка
print(json_data)

with open('../data.json', 'w') as file:
    json.dump(json_data, file)
    # json.dumps()

# with open('src/dist/new_file.json', 'r') as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()


url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)
# response.status_code  # 200
# response.content  # [...]
print(response.content.decode())
print(type(response.content.decode()))
json_data1 = json.loads(response.content.decode())
print(json_data1[7])
print(type(json_data1[7]))

for i in json_data1:
    print(i["title"])
    with open(f'hello/data_{i["id"]}_new_new.json', 'w') as file:
        json.dump(json_data, file)
