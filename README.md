# ToDoListFlask

ToDoListFlask is a simple Flask application that allows users to manage a list of todo items. Each todo item has a title and an "is_completed" flag, enabling users to track their tasks effectively.

## Features

- Add new todo items
- Edit existing todo items
- Delete todo items
- View a list of all todo items
- Responsive design for mobile and desktop

## Technologies Used

- Flask: A lightweight WSGI web application framework.
- Flask-SQLAlchemy: An extension for Flask that adds support for SQLAlchemy.
- HTML/CSS: For the frontend design.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd ToDoListFlask
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database (if necessary):
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.