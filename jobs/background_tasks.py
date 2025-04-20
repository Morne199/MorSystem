# jobs/background_tasks.py

import time

def process_task_in_background(task_name: str):
    print(f"Starting background task: {task_name}")
    time.sleep(5)  # Simulate heavy work
    print(f"Task {task_name} processed ✅")
    
def send_email_notification(task_title: str):
    print(f"📧 Sending email: New task created - {task_title}")