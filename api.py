import requests

def fetch_github_info():
    url = "https://api.github.com"

    response = requests.get(url)

    print("Status Code", response.status_code)
    print("Headers:", response.headers)
    print("Response Data:")

if __name__=="__main__":
    fetch_github_info()

    #RESTful


import requests
import json

def get_user_details(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print("User Name:", user_data["login"])
        print("Public Repos:", user_data["public_repos"])
    else:
        print("Failed to fetch data")

get_user_details("utkarsh428")
