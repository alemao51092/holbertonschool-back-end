#usr/bin/python3
"""Employee Task API

This script retrieves information about a user's completed and incomplete tasks
using the jsonplaceholder.typicode.com API.
"""

import requests
import json
from sys import argv

if __name__ == "__main__":

    if len(argv) != 2:
        exit()

    x = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    userx = json.loads(x.text)
    u = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    useru = json.loads(u.text)
    
    completed = 0
    not_completed = 0
    for task in useru:
        if task["completed"]:
            completed += 1
        else:
            not_completed += 1

    print(f"Employee {userx['name']} is done with task"
        f"({completed}/{not_completed + completed}):")
    for task in useru:
        if task["completed"]:
            print(f'\t {task["title"]}')
