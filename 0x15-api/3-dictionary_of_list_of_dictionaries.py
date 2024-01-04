#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python script that, using a REST API exports JSON
"""
import json
import requests
def fetch_all_tasks():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url):
        if response.status_code == 200:
            return response.json()
        else:
            return None
def create_tasks_dict(tasks):
    tasks_dict = {}
    for task in tasks:
        user_id = task['userId'] 
        username = task['username']
        task_data = {"username": username,
                "task": task['title'],
                "completed": task['completed']
        }
        if user_id not in tasks_dict:
            tasks_dict[user_id] = []
            tasks_dict[user_id].append(task_data)
    return tasks_dict
def export_tasks_to_json(tasks_dict):
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(tasks_dict, file, indent=2)
    print(f"Tasks exported to {filename}")

if __name__ == "__main__":
    main()
        
