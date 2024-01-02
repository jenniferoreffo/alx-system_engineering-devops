#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Python script that, using a REST API
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    if response.status_code != 200:
        print("Failed to fetch data")
        return
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)

    employee_name = todos[0]['username'] if total_tasks > 0 else "Unknown"
    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
    print(f"{employee_name}: {len(completed_tasks)}/{total_tasks}")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
