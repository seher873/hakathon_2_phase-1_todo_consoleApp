# Evolution of Todo - Phase 1

A robust command-line todo application built as part of Hackathon II. This application allows users to manage tasks efficiently in memory, following clean code principles and modular architecture.

## Features

- **Add Tasks**: Create new tasks with a title (max 100 chars) and an optional description.
- **View Tasks**: List all tasks with their IDs, detailed descriptions, and completion status.
- **Update Tasks**: Modify the title or description of existing tasks by ID.
- **Delete Tasks**: Safely remove tasks with a confirmation prompt.
- **Toggle Status**: Easily mark tasks as complete or incomplete.
- **Validation & Error Handling**: Robust input validation and graceful error messaging.
- **PEP 8 Compliant**: Codebase follows standard Python style guidelines.

## Usage

### Prerequisites
- Python 3.8 or higher is required.

### Running the Application
1. Clone the repository and navigate to the project root.
2. Run the application using the following command:
   ```bash
   python src/cli/main.py
   ```

### Menu Options
- **1: Add a new task** - Prompt for title and description.
- **2: View all tasks** - Shows all tasks with `[X]` for complete and `[ ]` for incomplete.
- **3: Update a task** - Edit details by entering the task ID.
- **4: Delete a task** - Remove a task by ID (requires confirmation).
- **5: Toggle status** - Change task from complete to incomplete (or vice versa).
- **0: Exit** - Securely close the application.

## Project Structure

```text
src/
├── models/
│   └── task.py          # Task data model and dictionary conversion
├── services/
│   └── task_service.py  # Core business logic and in-memory storage
├── cli/
│   └── main.py          # CLI menu system and user interaction
└── lib/
    └── utils.py         # Shared validation and display utilities
```

## Constraints
- **In-Memory Storage**: Data is lost when the application is closed.
- **No Dependencies**: Built entirely using the Python standard library.

## Future Evolution
This project is designed with modularity in mind to support future phases, including persistent storage, web interfaces, and cloud-native deployment.

---
🤖 Generated with [Claude Code](https://claude.com)
# hakathon_2_phase-1_todo_consoleApp
python3 src/cli/main.py