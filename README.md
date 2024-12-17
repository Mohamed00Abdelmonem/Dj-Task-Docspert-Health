
# Dj-Task Docspert Health Company 

## Overview

**Dj-Task** is a Django-based web application designed to manage tasks for a health company. It allows users to transfer funds between accounts, import account data, and perform other essential operations.

## Features

- **Fund Transfer:** Securely transfer funds between accounts.
- **Account Import:** Import account data via CSV files.
- **User Authentication:** Register, log in, and manage user sessions.
- **Admin Interface:** Manage accounts and transactions through Django's built-in admin panel.


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/dj-task.git
   cd dj-task
   ```

2. **Set Up Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


6. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Access the Admin Panel:** Navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.
- **Transfer Funds:** Use the "Transfer Funds" feature to move money between accounts.
- **Import Accounts:** Use the "Import Accounts" feature to upload account data via CSV.

## Running Tests

To run the unit tests:

```bash
python manage.py test accounts
```

 
