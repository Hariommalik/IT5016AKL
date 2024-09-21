                                     Convenience Store with Membership Rewards
                                                    Overview
This project is a simple implementation of a convenience store system using Python. It incorporates a membership rewards program, allowing customers to earn and redeem points based on their purchases. The design follows basic object-oriented programming principles and emphasizes simplicity and maintainability.

Features
Display a list of products available for purchase.
Allow customers to make purchases and earn points.
Enable customers to redeem their membership points.
Show customer points and details.
Software Design Principles
KISS (Keep It Simple, Stupid)
The KISS principle is applied throughout the design by ensuring that the code remains straightforward and easy to understand. Here’s how:

Clear Class Responsibilities: Each class has a single responsibility:

Product: Represents a product with its attributes.
Customer: Manages customer details and membership points.
Store: Handles product inventory and customer transactions.
Simple User Interface: The menu-driven user interface is designed to be intuitive, allowing users to easily navigate options without complexity.

Minimal Dependencies: The code avoids unnecessary complexity and dependencies, focusing only on core functionality to enhance readability and maintainability.

DRY (Don't Repeat Yourself)
The DRY principle is applied to reduce redundancy and promote reusability. This is achieved through:

Reusable Methods: Common functionalities, such as adding points and redeeming points, are encapsulated within the Customer class, preventing code duplication across different parts of the program.

Single Responsibility Principle: Each method within the classes is designed to perform a single task, making it easier to manage and modify without repeating code.

Code Structure
plaintext
Copy code
.
├── convenience_store.py    # Main code file containing classes and functionalities
└── README.md                # Project documentation
How to Run the Program
Ensure you have Python installed on your machine.
Clone or download this repository.
Navigate to the project directory.
Run the program using the command:
bash
Copy code
python convenience_store.py
Follow the on-screen instructions to interact with the store.
Example Usage
Display Products: View the list of products available in the store.
Purchase Product: Enter your name and the product you want to buy to earn points.
Redeem Points: Enter your name and the number of points to redeem.
Show Customer Points: Check your current points balance.
Conclusion
This convenience store program demonstrates a clear application of the KISS and DRY principles, making it an effective and maintainable solution for a membership rewards system. Future enhancements could include expanding product offerings, implementing payment systems, or integrating a database for persistent data storage