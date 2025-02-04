# Library Management System
This is a Library Management System built in Python using the Test-Driven Development (TDD) approach. The system allows users to manage books in a library, including adding books, borrowing books, returning books, and viewing available books. All interactions with the system are done through a terminal-based menu.

## Table of Contents
* Features
* Prerequisites
* Installation
* Testing
- What is TDD?
- What is unittest?
* Run the Project
* Project Workflow

## Features
+ **Add Book:** Add a new book to the library's collection.
+ **Borrow Book:** Borrow a book from the library if it is available.
+ **Return Book:** Return a borrowed book to the library.
+ **View Available Books:** Display a list of all books currently available in the library.

## Prerequisites
* Python 3.12 installed on your machine.

## Installation
1.  **Clone the Repository:**
##
        git clone https://github.com/dishagitt/KATA_Library_Management_System.git
        cd KATA_Library_Management_System

## Testing
This project was developed using the Test-Driven Development (TDD) approach. Below is an overview of TDD and the **unittest** framework used in this project.

### What is TDD?
Test-Driven Development (TDD) is a software development process where developers write tests for their code before writing the actual feature code. The TDD cycle typically involves the following steps:

1. Write a Test: Define a test for a new feature based on the requirements.
2. Run the Test: Initially, the test will fail since the feature isn't implemented yet.
3. Write the Feature Code: Implement the minimal amount of code needed to make the test pass.
4. Run All Tests: Ensure that all tests pass, including the newly added one.
5. Refactor: Improve the code while keeping it functional and ensuring all tests still pass.

### What is Unittest?
**unittest** is a built-in Python module that provides a framework for writing and running tests. It is inspired by the xUnit family of testing frameworks and is designed to support a wide range of testing needs, from simple unit tests to more complex integration tests.

+ **Test Cases:** A test case is a single unit of testing. **unittest** provides the **TestCase** class, which you can subclass to create new test cases.
+ **Test Suite:** A collection of test cases, test suites, or both. **unittest** allows you to group multiple test cases together for easier management.
+ **Test Runner:** A component that orchestrates the execution of tests and provides the outcome to the user. The simplest way to run tests using **unittest** is via the command line.

In this project, the test cases are located in the **test_library.py** file, and they test the functionality of the code written in **library.py**.

To run the tests, use the following command:
##
        python.exe test_library.py

This command will discover and run all test cases found in the test_library.py file.

# Run the System
1. **Run the Project**
##
        python.exe library.py

2. **Navigate the menu:**
+ You will be presented with a menu in the terminal where you can choose to:
1. Add a Book
2. Borrow a Book
3. Return a Book
4. View Available Books
5. Exit
+ Enter the number corresponding to the action you want to perform.

# Project Workflow
- Add a Book: Enter details such as ISBN, title, author, and publication year.
- Borrow a Book: Select a book from the list of available books by its ISBN.
- Return a Book: Provide the ISBN of the borrowed book to return it.
- View Available Books: See a list of all books currently available in the library.