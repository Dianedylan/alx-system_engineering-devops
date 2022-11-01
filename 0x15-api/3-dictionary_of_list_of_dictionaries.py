#!/usr/bin/python3
"""
Task 3:
3-dictionary_of_list_of_dictionaries.py
Exports tasks for every employee ID,
the TODO list progress.
This information is exported in JSON format.
Uses a specific API.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    user_len = len(requests.get(url).json())
    data = {}

    for i in range(1, user_len + 1):
        req = requests.get(url + str(i))
        username = req.json()["username"]
        req = requests.get(url + str(i) + '/todos')
        amount = len(req.json())
        data[i] = []
        for j in range(amount):
            completed = req.json()[j]["completed"]
            title = req.json()[j]["title"]
            data[i].append({
                "task": title,
                "completed": completed,
                "username": username
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
