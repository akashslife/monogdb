# Student Management System

A simple desktop application for managing student records, built with **Python**, **Tkinter** (GUI), and **MongoDB** (database) via **PyMongo**.

## Features

- **Add Student** — Insert a new student record with validation on registration number, name, email, and mobile number.
- **Delete Student** — Remove a student record by registration number.
- **Update Student** — Edit an existing student's name, email, batch, or mobile number.
- **Show Student Details** — View all student records in a tabular popup window.

## Tech Stack

- Python 3
- Tkinter (standard GUI library)
- MongoDB (local instance)
- PyMongo (MongoDB driver for Python)

## Prerequisites

- Python 3.x installed
- MongoDB server running locally on the default port (`27017`)
- `pymongo` package installed

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. Install the required dependency:
   ```bash
   pip install pymongo
   ```

3. Make sure your local MongoDB server is running. By default, the app connects to:
   ```
   localhost:27017
   ```

## Usage

Run the application:

```bash
python main.py
```

This opens the main window with four options:

| Button | Action |
|---|---|
| Add New Students | Opens a form to add a new student record |
| Delete Student Entry | Opens a form to delete a student by registration number |
| Update Student Info | Opens a form to update an existing student's details |
| Show Student Details | Displays all students currently stored in the database |

## Database Structure

- **Database:** `Assignment08`
- **Collection:** `students`

Each student document has the following fields:

```json
{
  "Registration_No": "12345678",
  "Name": "John",
  "Email": "john@example.com",
  "Batch": "2024",
  "Mobile": "9876543210"
}
```

## Validation Rules

- All fields are required except **Mobile**.
- **Registration Number** must be an 8-digit number.
- **Name** must contain only alphabetic characters.
- **Email** must contain an `@` symbol.
- **Mobile** (if provided) must be a 10-digit number.

## Project Structure

```
student-management-system/
├── main.py        # Application source code
└── README.md      # Project documentation
```

## Notes

- The app will display an error popup and exit if it cannot connect to MongoDB on startup.
- This project is intended as a learning/assignment exercise and can be extended with features like search, sorting, or exporting records.

## License

This project is open source and available for educational use.
