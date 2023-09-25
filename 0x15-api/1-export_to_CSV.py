#!/usr/bin/python3
"""
Python script that, using a REST API, retrieves and displays
information about an employee's TODO list progress and exports it to CSV.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <employee_id>".format(sys.argv[0]))

    employee_id = sys.argv[1]

    # Get user info
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_info.json()
    user_id = user_data.get('id')  # Use 'id' instead of 'username'
    username = user_data.get('username')  # Use 'username' instead of 'name'

    # Get user's tasks
    user_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id))
    tasks_data = user_tasks.json()

    # Prepare CSV file name based on USER_ID
    csv_file_name = '{}.csv'.format(user_id)

    # Create and write to the CSV file
    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = [
                "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write CSV header
        writer.writeheader()

        # Write task data to CSV
        for task in tasks_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

    print("Data exported to {}".format(csv_file_name))
