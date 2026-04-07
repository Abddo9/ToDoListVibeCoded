# ToDoListVibeCoded 📝

A modern, interactive ToDo List application built with **React** and **Flask**. This single-page application allows users to manage their tasks seamlessly with inline add, edit, and delete functionality—no page redirects needed!

## ✨ Features

- ✅ **Add new todos** - Quick and easy task creation
- ✏️ **Inline editing** - Edit tasks directly without leaving the page
- 🗑️ **Delete todos** - Remove completed or unwanted tasks
- ☑️ **Mark as complete** - Toggle completion status with a checkbox
- 🎨 **Beautiful UI** - Modern gradient design with smooth animations
- 📱 **Responsive design** - Works perfectly on mobile and desktop
- ⚡ **Real-time updates** - Instant UI updates without page refreshes
- 🛡️ **Error handling** - User-friendly error messages
- 🧪 **Fully tested** - Comprehensive test suite with pytest

## 🛠️ Technologies Used

### Backend
- **Flask** - Lightweight WSGI web application framework
- **Flask-SQLAlchemy** - ORM for database management
- **SQLAlchemy** - SQL toolkit and Object-Relational Mapping
- **Python 3.8+** - Programming language

### Frontend
- **React 18** - JavaScript library for building UI components
- **Babel** - JavaScript compiler for JSX support
- **CSS3** - Modern styling with gradients and animations

### Testing
- **Pytest** - Testing framework
- **Pytest-Cov** - Code coverage reporting

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abddo9/ToDoListVibeCoded.git
   cd ToDoListVibeCoded
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python -m src.app
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:8080
   ```

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
python -m pytest tests/ -v
```

For code coverage report:

```bash
python -m pytest tests/ --cov=src
```

## 📁 Project Structure

```
ToDoListVibeCoded/
├── src/
│   ├── __init__.py           # Flask app initialization
│   ├── app.py                # Application entry point
│   ├── models/
│   │   └── todo.py           # Todo model definition
│   ├── routes/
│   │   └── todo_routes.py    # REST API endpoints
│   ├── static/
│   │   └── style.css         # Styling
│   └── templates/
│       └── index.html        # React single-page app
├── tests/
│   ├── conftest.py           # Test configuration
│   └── test_todo.py          # Test cases
├── config.py                 # Application configuration
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/todos` | Get all todos |
| POST | `/api/todos` | Create a new todo |
| PUT | `/api/todos/<id>` | Update a todo |
| DELETE | `/api/todos/<id>` | Delete a todo |

## 🎯 Usage

1. **Add a Todo**: Type in the input field and click "Add Todo"
2. **Edit a Todo**: Click the "Edit" button next to a todo, update the text, and click "Save"
3. **Delete a Todo**: Click the "Delete" button and confirm the deletion
4. **Mark Complete**: Click the checkbox next to a todo to toggle completion status

## 🚀 Features Highlights

- **No Page Reloads**: Everything happens inline with React's virtual DOM
- **Smooth Animations**: Delightful transitions and hover effects
- **Persistent Data**: All todos are saved in the SQLite database
- **Input Validation**: Empty titles are prevented from being added
- **Confirmation Dialogs**: Delete operations require confirmation
- **Responsive Layout**: Adapts beautifully to different screen sizes

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 👨‍💻 Author

Created by **Abdalwhab Bakheet Mohamed Abdalwhab** - Feel free to contribute or report issues!

---

Made with ❤️ by Abddo9
