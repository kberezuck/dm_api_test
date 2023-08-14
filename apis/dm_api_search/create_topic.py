import json

import requests

url = "http://5.63.153.31:5051/v1/fora/%D0%9E%D0%B1%D1%89%D0%B8%D0%B9/topics"

payload = json.dumps({
    "forum": {
        "id": "Общий",
        "unreadTopicsCount": 0
    },
    "title": "Тестовый пост22",
    "description": "Пост, чтобы не путаться"
})
headers = {
    'Content-Type': 'application/json',
    'x-dm-auth-token': 'IQJh+zgzF5DQxxtBXZrLCIGEzSPgq0jUgHuB2j1pHb5QM+cBOgL1zLAAt3o6/AlKYHwQdePe3dib1tvC5dmDKANjY1eCM9/p10nICIR25LhkNQQ5R48y0uZlR01PiWN6E/760eWhf50='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
