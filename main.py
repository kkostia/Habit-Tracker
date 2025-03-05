import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "kostia0807"
USERNAME = "kostia"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Steps Graph",
    "unit": "Steps",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text )
today = datetime.now()
graph_posting = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8602",
}

# posting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
# response = requests.post(url=posting_endpoint, json=graph_posting, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4500"
}
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)