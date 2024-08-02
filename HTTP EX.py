import requests

def test_1():
url = "[https://www.google.com](https://www.google.com/)"
response = requests.get(url)
print(response.status_code)
return response

def test_2():
params ={"q": "python language"}
response = requests.get("https://www.google.com/search",
params=params)
return response
def tes_3():
data = {
"name": "John",
"age": 30,
"city": "New York"
}
response = requests.post("https://www.google.com/search",
json=data)
return response

def test_4():
data = {
"name": "Nada",
"age": 21
}
response = requests.put("https://www.google.com/search",
json=data)
return response

def test_5():
data = {
"age": 22
}
response = requests.patch("https://www.google.com/search",
json=data)
return response

def test_6():
response = requests.delete("https://www.google.com/search")
return response

def test_7():
response = requests.get("https://www.google.com/search"
,allow_redirects=True)
return response.headers.get("Location")
