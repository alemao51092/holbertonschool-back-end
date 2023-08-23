#!/usr/bin/python3
"""
Employee Task API

This script retrieves information about a user's completed and incomplete tasks
using the jsonplaceholder.typicode.com API. It writes the obtained data
into a CSV file.
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) != 2:
        exit()

    user_req = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    user = json.loads(user_req.text)
    user_todo_req = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    user_todo = json.loads(user_todo_req.text)

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF=8') as f:

        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in user_todo:
            writer.writerow([user["id"], user["username"], task["completed"],
                             task["title"]])
