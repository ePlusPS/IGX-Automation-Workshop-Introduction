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
    print(f'Request Response {json_response["status"]}')
    print(json_response["joke"])


if __name__ == "__main__":
    telljoke()
