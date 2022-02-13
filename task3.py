import pytest
import requests
from random import randint
##Attention! The API is unstable and buggy, which may cause tests to fail

def create_data():
    r = randint(10000, 100000)
    rs = str(r)
    data = {
        "id": r,
        "username": rs,
        "firstName": rs,
        "lastName": rs,
        "email": rs,
        "password": rs,
        "phone": rs,
        "userStatus": 0
        }
    return data, rs

def create_user(data):
    res = requests.post("https://petstore.swagger.io/v2/user", json=data)
    assert res.status_code == 200


def test_user_create():
    data = create_data()
    create_user(data[0])
    res = requests.get("https://petstore.swagger.io/v2/user/"+data[1])
    assert res.status_code == 200
    assert res.json() == data[0]


def test_user_update():
    data = create_data()
    create_user(data[0])
    new_data = create_data()
    res = requests.put("https://petstore.swagger.io/v2/user/"+data[1],json = new_data[0])
    assert res.status_code == 200
    res = requests.get("https://petstore.swagger.io/v2/user/"+new_data[1])
    assert res.status_code == 200
    assert res.json() == new_data[0]

def test_user_delete():
    data = create_data()
    create_user(data[0])
    res = requests.delete("https://petstore.swagger.io/v2/user/"+data[1])
    assert res.status_code == 200
    res = requests.get("https://petstore.swagger.io/v2/user/"+data[1])
    assert res.status_code == 404

def test_user_login():
    res = requests.get("https://petstore.swagger.io/v2/user/login?username=1&password=1")
    assert res.status_code == 200

def test_user_logout():
    res = requests.get("https://petstore.swagger.io/v2/user/logout")
    assert res.status_code == 200
    

    
    
