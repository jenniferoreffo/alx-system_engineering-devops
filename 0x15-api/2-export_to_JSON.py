#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python script that, using a REST API
"""
import csv
import json
import requests
import sys

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    if response.status_code != 200:
        print("Failed to fetch data")
        return
    if not todos:
        print("No tasks found for this employee")
        return
    user_id = todos[0]['userId']
    username = todos[0]['username']
    tasks = []
    completed_tasks_count = 0
    for task in todos:
        task_dict = {
                            "task": task['title'],
                            "completed": task['completed'],
                            "username": username}
        tasks.append(task_dict)
        if task['completed']:
            completed_tasks_count += 1

    json_data = {user_id: tasks}
    filename = f"{user_id}.json"

    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)

    total_tasks = len(todos)
    print(f"Employee {username} is done with tasks ({completed_tasks_count}/{total_tasks}):")
    print(f"{username}: {completed_tasks_count}/{total_tasks}")
    print(f"Exported data to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

