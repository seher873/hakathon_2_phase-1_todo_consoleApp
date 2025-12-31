"""
Command-line interface for the todo app.

This module provides the main CLI menu system and user interaction functionality.
"""

import sys
import os

# Add parent directory to sys.path to allow imports from other modules
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from lib import utils
from services.task_service import TaskService


class TodoCLI:
    """
    Command-line interface for the todo application.
    """

    def __init__(self):
        """
        Initialize the CLI with a TaskService instance.
        """
        self.task_service = TaskService()

    def display_menu(self):
        """
        Display the main menu options to the user.
        """
        print("\n" + "="*40)
        print("TODO APP - Main Menu")
        print("="*40)
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as complete/incomplete")
        print("0. Exit")
        print("="*40)

    def add_task(self):
        """
        Handle adding a new task via CLI.
        """
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        # Validate title
        if not utils.validate_task_title(title):
            utils.display_error("Title is required. Task not added.")
            return

        description = input("Enter task description (optional): ").strip()
        try:
            task = self.task_service.add_task(title, description)
            utils.display_success(
                f"Task '{task.title}' added successfully with ID {task.id}")
        except ValueError as e:
            utils.display_error(str(e))

    def view_tasks(self):
        """
        Handle viewing all tasks via CLI.
        """
        print("\n--- All Tasks ---")
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            print(f"{status} {task.id}. {task.title}")
            if task.description:
                print(f"   {task.description}")
            print()

    def update_task(self):
        """
        Handle updating a task via CLI.
        """
        print("\n--- Update Task ---")
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks available to update.")
            return

        self.view_tasks()

        try:
            task_id = utils.get_valid_task_id_input(self.task_service)
            if task_id is None:
                print("Update operation cancelled.")
                return

            task = self.task_service.get_task_by_id(task_id)
            if not task:
                utils.display_error(f"Task with ID {task_id} not found.")
                return

            print(f"Current task: {task.title}")
            if task.description:
                print(f"Current description: {task.description}")

            new_title = input(
                f"Enter new title (or press Enter to keep '{task.title}'): ").strip()
            new_description = input(
                f"Enter new description (or press Enter to keep current): ").strip()

            # Use current values if user didn't provide new ones
            title = new_title if new_title else task.title
            description = new_description if new_description else task.description

            # Validate title if it's being updated
            if new_title and not utils.validate_task_title(title):
                utils.display_error("Title is required. Task not updated.")
                return

            updated = self.task_service.update_task(
                task_id, title, description)
            if updated:
                utils.display_success(
                    f"Task with ID {task_id} updated successfully")
            else:
                utils.display_error(f"Failed to update task with ID {task_id}")

        except ValueError as e:
            utils.display_error(str(e))

    def delete_task(self):
        """
        Handle deleting a task via CLI.
        """
        print("\n--- Delete Task ---")
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks available to delete.")
            return

        self.view_tasks()

        try:
            task_id = utils.get_valid_task_id_input(self.task_service)
            if task_id is None:
                print("Delete operation cancelled.")
                return

            task = self.task_service.get_task_by_id(task_id)
            if not task:
                utils.display_error(f"Task with ID {task_id} not found.")
                return

            print(f"You are about to delete: {task.title}")
            if task.description:
                print(f"Description: {task.description}")

            if utils.get_confirmation("Are you sure you want to delete this task?"):
                deleted = self.task_service.delete_task(task_id)
                if deleted:
                    utils.display_success(
                        f"Task with ID {task_id} deleted successfully")
                else:
                    utils.display_error(
                        f"Failed to delete task with ID {task_id}")
            else:
                print("Delete operation cancelled.")

        except ValueError as e:
            utils.display_error(str(e))

    def mark_task_status(self):
        """
        Handle marking a task as complete/incomplete via CLI.
        """
        print("\n--- Mark Task Status ---")
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks available to mark.")
            return

        self.view_tasks()

        try:
            task_id = utils.get_valid_task_id_input(self.task_service)
            if task_id is None:
                print("Mark operation cancelled.")
                return

            task = self.task_service.get_task_by_id(task_id)
            if not task:
                utils.display_error(f"Task with ID {task_id} not found.")
                return

            # Toggle the status
            new_status = not task.completed
            toggled = self.task_service.toggle_task_status(task_id)

            if toggled:
                status_str = "complete" if new_status else "incomplete"
                utils.display_success(
                    f"Task with ID {task_id} marked as {status_str}")
            else:
                utils.display_error(
                    f"Failed to toggle status for task with ID {task_id}")

        except ValueError as e:
            utils.display_error(str(e))

    def run(self):
        """
        Run the main application loop.
        """
        print("Welcome to the Todo App!")

        while True:
            self.display_menu()

            try:
                choice = input("Select an option (0-5): ").strip()

                if choice == '1':
                    self.add_task()
                elif choice == '2':
                    self.view_tasks()
                elif choice == '3':
                    self.update_task()
                elif choice == '4':
                    self.delete_task()
                elif choice == '5':
                    self.mark_task_status()
                elif choice == '0':
                    print("Thank you for using the Todo App. Goodbye!")
                    break
                else:
                    print("Invalid option. Please select a number between 0 and 5.")

            except KeyboardInterrupt:
                print("\n\nApplication interrupted. Goodbye!")
                break
            except Exception as e:
                utils.display_error(f"An unexpected error occurred: {str(e)}")


def main():
    """
    Main function to run the todo app CLI.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()
