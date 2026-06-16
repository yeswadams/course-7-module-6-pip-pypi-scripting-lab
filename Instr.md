Lab: Automating Python Projects with Pip, PyPi & Scripting
In this lab, you will build a lightweight automation tool that:

Uses external packages installed via pip.
Writes modular Python scripts that can be run from the command line.
Tracks project dependencies in requirements.txt.
Ensures reproducibility across environments.
The lab focuses on applying pip, PyPi, and scripting fundamentals to automate small-scale, real-world tasks efficiently.

The Scenario
In this lab, you'll design and implement a Python Command-Line Interface (CLI) tool that models real-world behavior using OOP. You'll use Python's built-in argparse module to define commands, and object-oriented classes to manage task-related actions.

The CLI tool will allow you to:

Add tasks to a user account via add-task
Mark tasks as complete via complete-task
Display feedback directly in the terminal
This lab combines CLI architecture with OOP principles to help you build intuitive and testable developer tools.

Tools and Resources
GitHub Repo: Lab - Automating Python Projects with Pip, PyPi & ScriptingLinks to an external site.

Instructions
Set Up
Task 1: Define the Problem
Task 2: Determine the Design
Task 3: Develop, Test, and Refine the Code
Task 4: Document and Maintain
Task 4: Document and Maintain
Best Practices

Use pip freeze and requirements.txt to document dependencies.
Use virtual environments to isolate package installations.
Write comments and use functions to separate concerns.
Wrap script logic in the if __name__ == "__main__" block.
Keep your GitHub repo organized with a clear README.md.
  Important 
Before you submit your solution, you need to save your progress with git.

Add your changes to the staging area by executing git add.
Create a commit by executing git commit -m "Your commit message"
Push your commits to GitHub by executing git push origin main or git push origin master, depending on the name of your branch (use git branch to check on which branch you are).
Submission and Grading Criteria
Use the rubric below as a guide for how this lab is graded.
Your submission will be automatically scored in CodeGrade, using the most recent commit.

Remember to make sure you have pushed your commit to GitHub before submitting your assignment. 
You can review your submission in CodeGrade and see your final score in your Canvas gradebook.
When you are ready to submit, launch CodeGrade.
Click on + Create Submission. Connect your repository for this lab.
For additional information on submitting assignments in CodeGrade: Getting Started in CanvasLinks to an external site..

Rubric
Lab: Automating Python Projects with Pip, PyPi & Scripting
Lab: Automating Python Projects with Pip, PyPi & Scripting
Criteria	Ratings
This criterion is linked to a Learning OutcomeThe generate_log() function
The generate_log() function creates a file with the correct timestamped filename.
Autotest Passed
Autotest Did Not Pass
This criterion is linked to a Learning Outcomefilename follows pattern log_YYYYMMDD.txt
The filename follows the pattern log_YYYYMMDD.txt.
Autotest Passed
Autotest Did Not Pass
This criterion is linked to a Learning OutcomeFile contents exactly match the input list
The file contents exactly match the input list provided to the function.
Autotest Passed
Autotest Did Not Pass
This criterion is linked to a Learning OutcomeThe function raises a ValueError
The function raises a ValueError when called with invalid input (non-list types).
Autotest Passed
Autotest Did Not Pass
This criterion is linked to a Learning Outcomevalid (empty) log file without errors.
An empty list still creates a valid (empty) log file without errors.
Autotest Passed
Autotest Did Not Pass
This criterion is linked to a Learning OutcomeFunction prints a confirmation message
The function prints a confirmation message including the filename.
Autotest Passed
Autotest Did Not Pass
This criterion is linked to a Learning OutcomeLog file is created and removed
The log file is created in the expected directory and removed cleanly during test teardown.
Autotest Passed
Autotest Did Not Pass
