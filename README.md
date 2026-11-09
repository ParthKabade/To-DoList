# To-Do List Application

A simple **console-based To-Do List application** developed using Python. It allows users to add, view, and remove tasks, with persistent storage using file handling.

## Features

- **Add Tasks:** Add new tasks to your list.
- **View Tasks:** Display all available tasks with their serial numbers.
- **Remove Tasks:** Remove a selected task using its task number.
- **Persistent Storage:** Save tasks in a text file (`tasks.txt`).
- **Automatic Loading:** Load previously saved tasks when the application starts.
- **Data Persistence:** Changes are saved after successful task additions and removals.
- **Error Handling:** Handle missing task files and invalid numeric input.

## Technologies Used

- Python 3
- File Handling
- Python Lists
- Exception Handling
- String Manipulation

## Project Structure

```text
Todo/
│
├── todo.py
├── tasks.txt
└── README.md
```

| File | Description |
|---|---|
| `todo.py` | Main Python application |
| `tasks.txt` | Stores tasks persistently |
| `README.md` | Project documentation |

## Requirements

- Python 3 installed on your system.
- A code editor such as Visual Studio Code.

No external Python libraries are required.

## How to Run

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the application:

```bash
python3 todo.py
```

The application will automatically load previously saved tasks from `tasks.txt`. If the file does not exist, it starts with an empty task list.

## Application Menu

```text
-------------Menu-------------

1:Add_Task
2:View_Task
3:Remove_Task
4:Exit

select one of the above
```

### Example Usage

**Adding Tasks**

```text
select one of the above1
Enter Task: Learn Python
Learn Python : Task Added Successfully
```

**Viewing Tasks**

```text
select one of the above2

1 : Learn Python
2 : Complete Project
```

**Removing Tasks**

```text
select one of the above3

1 : Learn Python
2 : Complete Project

enter task number which you want to remove: 1
Removed task : Learn Python
```

## Data Storage

The application uses a text file named `tasks.txt` to maintain task information.

- Each task is stored on a separate line.
- Tasks are loaded when the application starts.
- The updated task list is saved after successful additions and removals.
- The application uses Python's file-handling operations and context managers.

## Concepts Learned

This project demonstrates practical implementation of:

- Python functions
- Lists and list methods (`append()`, `pop()`)
- Loops and conditional statements
- User input handling
- File reading and writing
- Exception handling (`FileNotFoundError`, `ValueError`)
- Context managers (`with open()`)
- Modular program design

## Future Improvements

- Prevent empty task entries.
- Improve input validation.
- Add task completion status.
- Add task editing functionality.
- Introduce task priorities and deadlines.

## Author

**Parth Nilesh Kabade**

## Project Type

Python Developer Internship – Task 2

**Project:** Console-based To-Do List Application
