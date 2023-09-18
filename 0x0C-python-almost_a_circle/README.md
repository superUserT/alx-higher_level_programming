# Almost a Circle - PythonOOP

# Background Context

The "Almost a Circle" project is a significant part of the Higher Level curriculum and will prepare you for the AirBnB project. In this project, you will review a wide range of Python concepts, including import, exceptions, classes, private attributes, getter/setter methods, class methods, static methods, inheritance, unittest, and file read/write operations. You will also learn about *args and **kwargs, serialization/deserialization, and JSON handling.

# Learning Objectives

By the end of this project, you will be able to explain the following concepts without relying on Google:

General:

    Unit testing and its implementation in a large project.
    Serialization and deserialization of a class.
    Reading and writing JSON files.
    *args and **kwargs in Python and how to use them.
    Handling named arguments in a function.

Almost a Circle - PythonOOP

Author: Guillaume

Weight: 1

Project Start: Sep 14, 2023 6:00 AM

Project End: Sep 19, 2023 6:00 AM

Checker Release: Sep 18, 2023 6:00 PM

Manual QA Review: Required upon project completion

Auto Review: Will be launched at the deadline
Background Context

The "Almost a Circle" project is a significant part of the Higher Level curriculum and will prepare you for the AirBnB project. In this project, you will review a wide range of Python concepts, including import, exceptions, classes, private attributes, getter/setter methods, class methods, static methods, inheritance, unittest, and file read/write operations. You will also learn about *args and **kwargs, serialization/deserialization, and JSON handling.
Learning Objectives

By the end of this project, you will be able to explain the following concepts without relying on Google:

General:

    Unit testing and its implementation in a large project.
    Serialization and deserialization of a class.
    Reading and writing JSON files.
    *args and **kwargs in Python and how to use them.
    Handling named arguments in a function.

Copyright - Plagiarism

    Solutions for the tasks must be developed independently to achieve the learning objectives.
    Copying and pasting someone else's work is not allowed.
    Publishing any content from this project is prohibited.
    Any form of plagiarism will result in removal from the program.

Requirements

Python Scripts:

    Allowed editors: vi, vim, emacs.
    All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
    All files should end with a newline character.
    The first line of all files should be #!/usr/bin/python3.
    A README.md file at the root of the project folder is mandatory.
    Your code should adhere to PEP 8 style guidelines (pycodestyle version 2.8.*).
    All files must be executable.
    The length of your files will be tested using wc.
    All modules, classes, and functions should be documented.
    Documentation should provide clear explanations of the purpose of the module, class, or method.

Python Unit Tests:

    Allowed editors: vi, vim, emacs.
    All files should end with a newline character.
    All test files should be inside a folder named tests.
    Use the unittest module for testing.
    Test files should have the extension .py.
    Test files and folders should start with test_.
    Execute all tests using python3 -m unittest discover tests.
    Work together on test cases to ensure comprehensive coverage.

Tasks
0. If it's not tested, it doesn't work (Mandatory)

    All your files, classes, and methods must be unit-tested and PEP 8 validated.
    Example:

    shell

    guillaume@ubuntu:~/$ python3 -m unittest discover tests

1. Base class (Mandatory)

    Create a folder named models with an empty file __init__.py inside it (this makes the folder a Python package).
    Create a file named models/base.py:
        Define a class called Base with a private class attribute __nb_objects set to 0.
        Implement the class constructor def __init__(self, id=None):
            If id is not None, assign it to the public instance attribute id. You can assume id is an integer, so no type checking is required.
            If id is None, increment __nb_objects and assign the new value to the id attribute.

2. First Rectangle (Mandatory)

    Write the first class Base.
    Create a folder named models with an empty file __init__.py inside it.
    Create a file named models/base.py:
        Define a class called Base with a private class attribute __nb_objects set to 0.
        Implement the class constructor def __init__(self, id=None):
            If id is not None, assign it to the public instance attribute id. You can assume id is an integer, so no type checking is required.
            If id is None, increment __nb_objects and assign the new value to the id attribute.

3. Validate attributes (Mandatory)

    Update the class Rectangle by adding validation to all setter methods and the constructor (except for id):
        If the input is not an integer, raise a TypeError with the message: <name of the attribute> must be an integer. For example, width must be an integer.
        If width or height is less than or equal to 0, raise a ValueError with the message: <name of the attribute> must be > 0. For example, width must be > 0.
        If x or y is less than 0, raise a ValueError with the message: <name of the attribute> must be >= 0. For example, x must be >= 0.

4. Area first (Mandatory)

    Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

5. Display #0 (Mandatory)

    Update the class Rectangle by adding the public method def display(self): that prints the rectangle using the # character.

6. str (Mandatory)

    Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.

7. Display #1 (Mandatory)

    Update the class Rectangle by improving the public method def display(self): to print the rectangle with the x and y offset.

8. Update #0 (Mandatory)

    Update the class Rectangle by adding the public method def update(self, *args): that assigns attributes.
    You can assume the arguments passed are in this order: id, width, height, x, and y.
    Each argument corresponds to the attribute:
        id -> id
        width -> width
        height -> height
        x -> x
        y -> y
    The method should not change the id attribute if the argument is not passed.
    Exception: If a non-keyword argument is the first argument (it's not a keyword argument), then assign its value to the attribute id.

9. Update #1 (Mandatory)

    Update the class Rectangle by updating the public method def update(self, *args): to assign attributes in this order: id, width, height, x, and y.

10. And now, the Square! (Mandatory)

    Create a class Square that inherits from Rectangle.
    Create a constructor (def __init__(self, size, x=0, y=0, id=None):) and override the setter and getter methods of the width and height attributes to manage the size attribute, which is the size of the square (private instance attribute).
    You must not create a new instance attribute for size (use width and height).
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer.
    All other methods should be the same as the Rectangle class (override __str__ and display methods).

11. Square size (Mandatory)

    Update the class Square by adding the public method def update(self, *args, **kwargs): that assigns attributes.
    You can assume the arguments passed are in this order: id, size, x, and y.
    Each argument corresponds to the attribute:
        id -> id
        size -> size
        x -> x
        y -> y
    The method should not change the id attribute if the argument is not passed.
    Exception: If a non-keyword argument is the first argument (it's not a keyword argument), then assign its value to the attribute id.
    Use the **kwargs method for this task.

12. Square update (Mandatory)

    Update the class Square by adding the public method def update(self, *args, **kwargs): that assigns attributes.
    You can assume the arguments passed are in this order: id, size, x, and y.
    Each argument corresponds to the attribute:
        id -> id
        size -> size
        x -> x
        y -> y
    The method should not change the id attribute if the argument is not passed.
    Exception: If a non-keyword argument is the first argument (it's not a keyword argument), then assign its value to the attribute id.
    Use the **kwargs method for this task.

13. Rectangle instance to dictionary representation (Mandatory)

    Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.

14. Square instance to dictionary representation (Mandatory)

    Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square.

Execution

Your project will be reviewed both manually and automatically. Manual review will cover:

    Your code's organization.
    Your use of the unittest module.
    Your ability to write and explain unit tests.

Your project should be formatted according to the PEP 8 style guide and the "requirements" section above. Use the unittest module for testing.

In the manual review, the reviewer will check that:

    Your code is correct and matches the expected output.
    Your code passes all test cases.
