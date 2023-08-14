import requests
import json

url = "http://5.63.153.31:5051/v1/fora/%D0%9E%D0%B1%D1%89%D0%B8%D0%B9/topics"

payload = json.dumps({
  "forum": {
    "id": "Общий",
    "unreadTopicsCount": 0
  },
  "title": "Тесттовый пост",
  "description": "Пост, чтобы не путаться"
})
headers = {
  'Content-Type': 'application/json',
  'x-dm-auth-token': 'IQJh+zgzF5CmR3N9d4ChVexZ78bwzmg+BbueB/cg6oUhqd6Z0w4tR+pxRNB2Z/QU02306SrO+WLDfpN8eAYJT6FSWGa8EeBwuS1EFvyh/uzSlamU9v4p0De0hl9fLTQx/RbWmjnUdRc='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)