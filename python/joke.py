#!/usr/bin/env python
import requests

def telljoke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        'Accept': "application/json",
        'User-Agent': "postman",
        }
    response = requests.request("GET", url, headers=headers)
    json_response = response.json()
    print(json_response["joke"])
    print(json_response["id"])

if __name__ == "__main__":
    telljoke()
