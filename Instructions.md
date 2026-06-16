You are an expert Python software engineer.

Your task is to implement this lab exactly as specified. Treat this as an academic assignment that will be graded by automated tests. Do not over-engineer the solution or introduce unnecessary abstractions that could cause the tests to fail.

Goal

Build a Python automation project that demonstrates:

Python scripting
pip package usage
File I/O
requirements.txt dependency tracking
Modular code
Command-line execution

The implementation must strictly satisfy the grading rubric.

Project Structure

Create the following project structure:

project/
│
├── generate_log.py
├── requirements.txt
├── README.md
└── .gitignore
Functional Requirements
1. Implement generate_log()

Inside generate_log.py, create a function named:

generate_log(log_data)

This function must:

Accept exactly one argument called log_data
Require that log_data is a list
Raise
ValueError

if the argument is not a list.

2. Filename

The generated filename must exactly follow this format:

log_YYYYMMDD.txt

Example:

log_20260616.txt

Generate the date using:

datetime.now().strftime("%Y%m%d")
3. File Writing

Write every item in the list to the file.

Each item must occupy its own line.

Example input:

[
    "User logged in",
    "User updated profile",
    "Report exported"
]

Generated file:

User logged in
User updated profile
Report exported

No extra formatting.

No numbering.

No timestamps.

No JSON.

No bullets.

Exactly one log entry per line.

4. Empty List

If:

generate_log([])

is called,

the function must still:

create the log file
create an empty file
not raise any exception
5. Confirmation Message

After writing the file, print:

Log written to log_YYYYMMDD.txt

The filename must match the generated filename.

6. Return Value

Return the generated filename.

Example:

filename = generate_log(log_data)

should return

"log_20260616.txt"
7. Script Execution

Include:

if __name__ == "__main__":

Inside this block:

Create the sample data:

[
    "User logged in",
    "User updated profile",
    "Report exported"
]

Call:

generate_log(log_data)
External Package Requirement

Install and use the package:

requests

Create a function:

fetch_data()

that fetches:

https://jsonplaceholder.typicode.com/posts/1

using:

requests.get()

If successful:

Return:

response.json()

Otherwise return:

{}

Inside the __main__ block print:

Fetched Post Title: ...

using:

post.get("title", "No title found")

Do not mix this API response into the log file.

The API example exists only to demonstrate usage of an external package.

requirements.txt

Include:

requests

(or the exact output of pip freeze if version pinning is desired).

README.md

Write a concise README including:

Project overview
Installation
pip install -r requirements.txt
Running
python generate_log.py
Expected output
Project structure
Coding Requirements

Use:

functions
clear variable names
comments where appropriate
File I/O
datetime
requests
modular design
Constraints

Do NOT:

build a CLI with argparse
create classes
use OOP
create multiple Python modules
use pandas
use rich
use click
write JSON files
use CSV output
add logging libraries
add unit tests unless explicitly requested

The solution should remain as simple as possible while satisfying every rubric requirement.

Rubric Compliance Checklist

Ensure the implementation passes all of the following:

✅ generate_log() exists
✅ Filename is exactly log_YYYYMMDD.txt
✅ File contents exactly match the input list
✅ Raises ValueError for non-list input
✅ Empty list creates an empty file successfully
✅ Prints a confirmation message including the filename
✅ File is created in the working directory
✅ Uses requests
✅ Includes requirements.txt
✅ Uses if __name__ == "__main__":
Deliverables

Generate the complete project, including:

generate_log.py
requirements.txt
README.md

Return each file in its own Markdown code block with the filename as the heading. Do not omit any required files. Ensure the code is immediately runnable without modification.