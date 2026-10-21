# CLI Calculator Documentation

## Project Overview

The Command-Line Interface Calculator is a collaborative Python project designed to build a practical calculator application that runs in the terminal. The goal is to apply programming and mathematical concepts learned during university study while improving teamwork, code organization, and problem solving.

This project focuses on creating a usable command-line calculator with a clear modular structure, efficient functions, and maintainable code.

## Objectives

- Build a functional calculator in Python
- Practice mathematical problem solving
- Improve code organization and modular design
- Strengthen teamwork and Git/GitHub collaboration
- Learn how to manage shared code in a project environment

## Features

The calculator is intended to support the following categories of operations:

### Basic Operations
- Addition
- Subtraction
- Multiplication
- Division
- Modulus

### Area Calculations
- Square
- Rectangle
- Circle
- Triangle

### Volume Calculations
- Cube
- Cuboid
- Sphere
- Cylinder

### Sequences
- Arithmetic sequence
- Geometric sequence

## Project Structure

```text
CLI-Calculator/
├── main.py
├── functions.py
├── jobs.xlsx
├── README.md
├── DOCUMENTATION.md
└── .gitignore
```

### main.py
Responsible for the user interface and overall program flow. It handles:
- Displaying menus
- Reading input from the user
- Calling functions from `functions.py`
- Showing results
- Managing invalid input and repeated actions

### functions.py
Contains the mathematical logic used by the program. Each function should:
- Accept the needed parameters
- Perform a calculation
- Return a result in a predictable format

### jobs.xlsx
Used to track tasks, responsibilities, function requirements, and progress for the project.

## How to Run

1. Make sure Python is installed on your system.
2. Open the project folder in your preferred Python editor or terminal.
3. Run the following command:

```bash
python main.py
```

The calculator will start in the command line and allow the user to select operations from the menu.

## Example Workflow

A typical flow for the app includes:

1. User chooses a category such as basic operations or area calculations
2. User selects the specific function
3. Program asks for required values
4. Function calculates the result
5. Result is displayed in the console
6. User can continue using the calculator or exit

## Collaboration Guidelines

This project is designed for teamwork. When contributing:

- Keep functions clearly named and easy to understand
- Communicate changes that affect shared code
- Check `jobs.xlsx` before implementing a new calculation
- Review other team members' work when possible
- Keep code readable and consistent

## Future Improvements

Possible enhancements for the project include:

- More mathematical formulas
- Physics-related calculations
- Advanced sequence types
- Trigonometric functions
- Calculation history
- Better error handling
- Graphical user interface (GUI)

## Development Notes

This project is primarily a learning experience. The main focus is not only to build a working calculator, but also to improve practical programming skills, analytical thinking, and collaborative development habits.

## Summary

The CLI Calculator is a beginner-friendly but meaningful project that combines Python programming, mathematics, and teamwork. By organizing the code into separate modules and following clear requirements, the project becomes an effective learning tool for software development and collaboration.
