#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python script that, using a REST API
"""
import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    if response.status_code != 200:
        print("No tasks found for this employee")
        return
    if not todos:
        print("No tasks found for this employee")
        return
    user_id = todos[0]['userId']
    username = todos[0]['username']
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        completed_tasks_count = 0
        for task in todos:
            completed_status = "True" if task['completed'] else "False"
            task_title = task['title']
            writer.writerow([user_id, username, completed_status, task_title])
            if task['completed']:
                completed_tasks_count += 1
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
