import os
import shutil
from paperbase import config

def newPaperBase(name):
    base_path = os.path.join("DB_USER", "projects", config.UID, "data", name)
    if os.path.exists(base_path):
        print(f"Error: The paperbase '{name}' already exists.")
        return

    try:
        os.makedirs(base_path)
        print(f"Paperbase '{name}' created successfully.")
    except Exception as e:
        print(f"Error creating paperbase: {e}")


def insertData(paperbase, key, value):
    if not config.UID:
        print("Project ID not connected. Use config.connect(project_id) first.")
        return

    base_path = os.path.join("DB_USER", "projects", config.UID, "data", paperbase)

    if not os.path.exists(base_path):
        print(f"Error: Paperbase '{paperbase}' does not exist.")
        return

    safe_key = key.replace('/', '_').replace('\\', '_')

    try:
        with open(os.path.join(base_path, safe_key), 'w') as file:
            file.write(value)
    except Exception as e:
        print(f"Error writing data: {e}")


def retrieveData(paperbase, key):
    if not config.UID:
        print("Project ID not connected. Use config.connect(project_id) first.")
        return

    base_path = os.path.join("DB_USER", "projects", config.UID, "data", paperbase)
    if not os.path.exists(base_path):
        print(f"Error: Paperbase '{paperbase}' does not exist.")
        return

    safe_key = key.replace('/', '_').replace('\\', '_')
    file_path = os.path.join(base_path, safe_key)

    if not os.path.exists(file_path):
        print(f"Error: Data key '{key}' does not exist in paperbase '{paperbase}'.")
        return

    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    except Exception as e:
        print(f"Error reading data key: {e}")


def editData(paperbase, key, new_value):
    if not config.UID:
        print("Project ID not connected. Use config.connect(project_id) first.")
        return

    base_path = os.path.join("DB_USER", "projects", config.UID, "data", paperbase)
    if not os.path.exists(base_path):
        print(f"Error: Paperbase '{paperbase}' does not exist.")
        return

    safe_key = key.replace('/', '_').replace('\\', '_')
    file_path = os.path.join(base_path, safe_key)

    if not os.path.exists(file_path):
        print(f"Error: Data key '{key}' does not exist in paperbase '{paperbase}'.")
        return

    try:
        with open(file_path, 'w') as file:
            file.write(new_value)
    except Exception as e:
        print(f"Error editing data key: {e}")


def deletePaperBase(name):
    base_path = os.path.join("DB_USER", "projects", config.UID, "data", name)

    if not os.path.exists(base_path):
        print(f"Error: The paperbase '{name}' does not exist.")
        return

    try:
        shutil.rmtree(base_path)
        print(f"Paperbase '{name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting paperbase: {e}")


def deleteData(paperbase, key):
    if not config.UID:
        print("Project ID not connected. Use config.connect(project_id) first.")
        return

    base_path = os.path.join("DB_USER", "projects", config.UID, "data", paperbase)

    if not os.path.exists(base_path):
        print(f"Error: Paperbase '{paperbase}' does not exist.")
        return

    safe_key = key.replace('/', '_').replace('\\', '_')
    file_path = os.path.join(base_path, safe_key)

    if not os.path.exists(file_path):
        print(f"Error: Data key '{key}' does not exist in paperbase '{paperbase}'.")
        return

    try:
        os.remove(file_path)
        print(f"Data key '{key}' deleted successfully from paperbase '{paperbase}'.")
    except Exception as e:
        print(f"Error deleting data key: {e}")