# Data Model: Todo App

## Task Entity

### Fields
- **id** (int): Auto-incrementing unique identifier starting from 1
- **title** (str): Brief description of the task (required)
- **description** (str): Detailed information about the task (optional)
- **completed** (bool): Boolean indicating whether the task is complete (default: False)

### Validation Rules
- Title must be provided when creating a task
- ID must be unique within the system
- ID must be a positive integer

### State Transitions
- New task: `completed = False`
- Mark complete: `completed = True`
- Mark incomplete: `completed = False`

## TaskList Collection

### Structure
- Python list containing Task objects/dictionaries
- Maintains order of task creation
- Provides methods for CRUD operations

### Operations
- Add task: Append to list with next available ID
- Get task by ID: Search list for matching ID
- Update task: Find by ID and modify fields
- Delete task: Find by ID and remove from list
- List all tasks: Return entire collection