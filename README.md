# QuickNotes

A simple and efficient note-taking application built with Flask

# Team
  @ayushagrawalgla
  @DevangMittal23

## Features

- **User Authentication**
  - User registration with username, email, and password
  - User login/logout functionality
  - Password hashing for security

- **Note Management**
  - Create new notes with title and content
  - View notes in a dashboard
  - Edit existing notes
  - Delete notes

- **User Interface**
  - Responsive design using Bootstrap
  - Clean and intuitive interface
  - Flash messages for user feedback

## Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Python with Flask
- **Database**: SQLite

## Project Structure

```
QuickNotes/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── forms.py               # Form classes
├── config.py              # Configuration settings
├── static/                # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── edit_note.html
│   └── view_note.html
├── instance/              # SQLite database (auto-created)
└── requirements.txt       # Project dependencies
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/sanatanisher01/Python-Projects-Intel.git
   cd Python-Projects-Intel
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. **Register a new account**
   - Click on "Register" in the navigation bar
   - Fill in the registration form with username, email, and password

2. **Login to your account**
   - Click on "Login" in the navigation bar
   - Enter your email and password

3. **Create a new note**
   - After logging in, you'll be redirected to the dashboard
   - Click on "New Note" button
   - Fill in the title and content for your note
   - Click "Save"

4. **View, edit, or delete notes**
   - All your notes are displayed on the dashboard
   - Use the dropdown menu on each note card to view, edit, or delete

## License

This project is licensed under the MIT License - see the LICENSE file for details.
