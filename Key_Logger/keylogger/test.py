from requests import request

url = "localhost:5000/api"


headers = {
  'Content-Type': 'application/json'
}

response = request("POST", url, headers=headers, data={"blabla": "la", "fd": "fdd"})

print(response.text)
