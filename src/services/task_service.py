"""
TaskService class for managing tasks in memory.

This module defines the TaskService class which manages tasks in memory using
a Python list and provides methods for CRUD operations.
"""

from models.task import Task
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class TaskService:
    """
    Service class for managing tasks in memory.
    """

    def __init__(self):
        """
        Initialize the TaskService with an empty task list and ID counter.
        """
        self.tasks = []
        self.next_id = 1

    def get_next_id(self):
        """
        Get the next available ID for a new task.

        Returns:
            int: The next available task ID
        """
        next_id = self.next_id
        self.next_id += 1
        return next_id

    def add_task(self, title, description=""):
        """
        Add a new task to the task list.

        Args:
            title (str): The title of the task
            description (str): The description of the task (optional)

        Returns:
            Task: The newly created task
        """
        task_id = self.get_next_id()
        task = Task(task_id, title, description, completed=False)
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        """
        Get all tasks in the task list.

        Returns:
            list: A list of all Task objects
        """
        return self.tasks

    def get_task_by_id(self, task_id):
        """
        Get a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Task: The task with the specified ID, or None if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, title=None, description=None):
        """
        Update an existing task's title and/or description.

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): The new title for the task
            description (str, optional): The new description for the task

        Returns:
            bool: True if the task was updated, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                if not title.strip():
                    raise ValueError(
                        "Title must be provided when updating a task")
                task.title = title.strip()
            if description is not None:
                task.description = description.strip() if description else ""
            return True
        return False

    def delete_task(self, task_id):
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def toggle_task_status(self, task_id):
        """
        Toggle the completion status of a task.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            bool: True if the task status was toggled, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = not task.completed
            return True
        return False
