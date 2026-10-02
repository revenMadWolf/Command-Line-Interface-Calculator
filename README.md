# Command Line Interface Calculator

A collaborative Python CLI calculator project developed as our first official programming project.

The purpose of this project is not only to create a functional calculator, but also to practice the programming and mathematical concepts we have learned at university, learn new concepts, and gain experience working collaboratively on a software project.

## 📌 About the Project

The **CLI Calculator** is a command-line application that can perform a variety of mathematical calculations.

The initial version of the calculator will include:

* Basic Operations
* Area Calculations
* Volume Calculations
* Sequences

More calculations, including Physics-related calculations, may be added as the project develops.

## 🖥️ Why CLI?

CLI stands for **Command Line Interface**.

Instead of using a graphical interface with buttons and visual elements, users interact with this calculator through the console by entering inputs.

We chose a CLI for this project because it allows us to focus on the programming logic and mathematical calculations before moving on to more advanced interfaces.

## 🛠️ Technologies and Tools

* **Python** – Main programming language
* **PyCharm / Thonny** – Python development environment
* **GitHub** – Version control and collaboration
* **GitHub Desktop** – Git management
* **Discord** – Team communication

## 📂 Project Structure

The project will mainly consist of two Python files:

```text
CLI-Calculator/
│
├── main.py
├── functions.py
├── jobs.xlsx
└── README.md
```

### `main.py`

Responsible for the user interface and interaction.

It will:

* Display menus
* Receive user input
* Call functions from `functions.py`
* Display calculation results
* Handle invalid input
* Control the main program loop

### `functions.py`

Contains the mathematical functions used by the calculator.

It will receive the required values from `main.py`, perform the calculations, and return the results.

### `jobs.xlsx`

Contains the project's task list and function requirements.

It will be used to keep track of:

* Tasks that need to be completed
* Completed tasks
* Assigned tasks
* Required parameters
* Expected return values

### `README.md`

Contains general information about the project, its purpose, structure, and how to use it.

## 🧮 Initial Calculations

### Basic Operators

* Addition
* Subtraction
* Multiplication
* Division
* Modulus

### Area

* Square
* Rectangle
* Circle
* Triangle
* Other required shapes

### Volume

* Cube
* Cuboid
* Sphere
* Cylinder
* Other required solids

### Sequences

* Arithmetic Sequence
* Geometric Sequence

Additional calculations may be added as the project develops.

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone or download the repository and open the project folder in your preferred Python IDE.

Run:

```bash
python main.py
```

The calculator will then start in the command line.

## 🤝 Collaboration

This is a collaborative project, so changes should be communicated with the team when they affect other parts of the program.

In particular, changes to functions in `functions.py` should be communicated to anyone working on `main.py`.

Before implementing a function, check `jobs.xlsx` to make sure you understand:

* The required function name
* The required parameters
* What the function should calculate
* What the function should return

## 🎯 Project Goals

The main goal of this project is to develop a working calculator while gaining practical experience in:

* Python programming
* Functions
* Mathematical problem solving
* Error handling
* Modular programming
* Git and GitHub
* Team collaboration
* Code organization
* Working with other people's code

## 🚀 Future Improvements

Possible future additions include:

* More mathematical formulas
* Physics calculations
* Additional sequence types
* Trigonometric calculations
* More advanced mathematical operations
* Calculation history
* Improved error handling
* A graphical user interface (GUI)

## 👥 Team

This project is being developed collaboratively as our first official programming project.

Each team member is encouraged to contribute, communicate, review each other's work, and learn from the development process.

---

**This project is primarily a learning experience. The goal is not just to build a calculator, but to become better programmers and better collaborators.**
