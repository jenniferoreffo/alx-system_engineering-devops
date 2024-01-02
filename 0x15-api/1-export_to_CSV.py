#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python script that, using a REST API
"""
import requests
import sys
import csv
def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    done_tasks = []
    todos = response.json()
    if response.status_code != 200:
        response = requests.get(url)
        return
    user_id = todos[0]['userId'] if todos else 'Unknown'
    username = todos[0]['username'] if todos else 'Unknown'

    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos:
            completed_status = "True" if task['completed'] else "False"
            task_title = task['title']
            writer.writerow([user_id, username, completed_status, task_title])
    print(f"Exported data to {filename}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
