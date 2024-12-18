# Project Setup Guide

This guide will help you set up and run the project on your local machine. Follow the steps below based on your operating system.

## Prerequisites

- Ensure Python (3.8 or higher) is installed on your machine. You can download it from [python.org](https://www.python.org/).
- Install `pip` (Python package installer) if not already installed.

## Setup Instructions

### Step 1: Create a Virtual Environment

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On Linux/Mac OS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Requirements

Install the necessary dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Edit the `.env` file and set up the environment variables as needed.

### Step 4: Run the Seeder Script

Execute the `seeder.py` script to populate initial data:

```bash
python seeder.py
```

You should see the message:

```
Seeder sukses!
```

### Step 5: Run the Application

Finally, start the main application:

```bash
python main.py
```

---

## Default Login Credentials

After running the seeder, you can log in using the following default credentials:

- **Admin Account:**
  - Email: `admin@gmail.com`
  - Password: `password`

---

## Notes

- Make sure to activate the virtual environment before running any commands.
- If you encounter issues, ensure all dependencies are properly installed and the `.env` file is correctly configured.
- For additional help, consult the project documentation or contact the maintainer.
