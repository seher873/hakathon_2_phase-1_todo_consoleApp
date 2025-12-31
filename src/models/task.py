"""
Task model definition for the todo app.

This module defines the Task class with id, title, description, and completion status fields.
It includes validation to ensure title is provided when creating a task.
"""


class Task:
    """
    Represents a todo item with ID, title, description, and completion status.
    """

    def __init__(self, task_id, title, description="", completed=False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task (auto-incrementing integer starting from 1)
            title (str): Brief description of the task (required)
            description (str): Detailed information about the task (optional, default is empty string)
            completed (bool): Boolean indicating whether the task is complete (default: False)

        Raises:
            ValueError: If title is not provided
        """
        if not title or not title.strip():
            raise ValueError("Title must be provided when creating a task")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed

    def __str__(self):
        """
        String representation of the Task.

        Returns:
            str: Formatted string representation of the task
        """
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.id}. {self.title}\n   {self.description}"

    def to_dict(self):
        """
        Convert the Task instance to a dictionary.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Task instance from a dictionary.

        Args:
            data (dict): Dictionary containing task data

        Returns:
            Task: Task instance created from the dictionary
        """
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )
