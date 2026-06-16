# Python Automation Lab: Pip, PyPi & Scripting

## Overview
This project is a Python automation tool that demonstrates how to use `pip` for dependency management, interact with external APIs using the `requests` library, and perform file I/O operations to generate log files.

## Project Structure
- `generate_log.py`: The main script containing the automation logic.
- `requirements.txt`: List of project dependencies.
- `README.md`: Project documentation.
- `.gitignore`: Files and directories to be ignored by Git.

## Installation
To set up the project and install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Running the Script
Execute the script using the following command:

```bash
python generate_log.py
```

## Expected Output
When executed, the script will:
1. Create a log file named `log_YYYYMMDD.txt` (where `YYYYMMDD` is the current date) in the working directory.
2. Write sample log entries to the file.
3. Fetch data from an external API and print the title of the fetched post.
4. Display a confirmation message: `Log written to log_YYYYMMDD.txt`.
5. Display the API result: `Fetched Post Title: [Post Title]`.
