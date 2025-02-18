import requests

def test_1():
    url = "https://httpbin.org/get"
    response = requests.get(url)
    print(response.status_code)
    return response

def test_2():
    params = {"q": "python language"}
    response = requests.get("https://httpbin.org/get", params=params)
    return response

def test_3():
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    response = requests.post("https://httpbin.org/post", json=data)
    return response

def test_4():
    data = {
        "name": "Nada",
        "age": 21
    }
    response = requests.put("https://httpbin.org/put", json=data)
    return response

def test_5():
    data = {
        "age": 22
    }
    response = requests.patch("https://httpbin.org/patch", json=data)
    return response

def test_6():
    response = requests.delete("https://httpbin.org/delete")
    return response

def test_7():
    response = requests.get("https://httpbin.org/redirect/1", allow_redirects=True)
    return response.headers.get("Location")
