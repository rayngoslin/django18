# Notes Application

This is a simple web application built with Django that allows users to create and view their notes.

## Features

- Create new notes
- View a list of all notes
- View details of individual notes

## Setup Instructions

1. **Clone the repository:**

   ```
   git clone <repository-url>
   cd notes_project
   ```

2. **Install dependencies:**

   Make sure you have Python and pip installed. Then run:

   ```
   pip install -r requirements.txt
   ```

3. **Run migrations:**

   ```
   python manage.py migrate
   ```

4. **Run the development server:**

   ```
   python manage.py runserver
   ```

5. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate to the notes list to view all your notes.
- Click on a note to view its details.
- Use the form to add new notes.