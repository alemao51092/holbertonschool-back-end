#!/usr/bin/python3
"""
Employee Task API

This script retrieves information about all users completed and incomplete
tasks using the jsonplaceholder.typicode.com API. It writes the obtained data
into a JSON file.
"""
import json
import requests

if __name__ == "__main__":

    users_req = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    users = json.loads(users_req.text)
    users_todo_req = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    users_todo = json.loads(users_todo_req.text)

    user_data = {}

    for user in users:
        tasks_of_user = [
            {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            for task in users_todo if user['id'] == task['userId']
        ]
        user_data[user['id']] = tasks_of_user

    with open('todo_all_employees.json', 'w', encoding='UTF=8') as f:
        json.dump(user_data, f)
