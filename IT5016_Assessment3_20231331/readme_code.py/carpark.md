Car Parking System

Overview

This repository contains a simple car parking system implemented in Python. The project serves as an illustrative example of various software design principles and programming concepts, emphasizing clean and maintainable code.

Software Design Principles

Single Responsibility Principle (SRP)
Each class and method in this code is designed to perform a single, well-defined task:

The ParkingLot class manages all operations related to parking (adding and removing cars, tracking available slots).
This separation allows for easier testing and maintenance, as changes in one part of the system have minimal impact on others.
Open/Closed Principle (OCP)
The ParkingLot class is structured to be open for extension but closed for modification:

If new functionalities are required (like implementing different parking fees), these can be added as new methods or subclasses without altering existing code.
This design promotes code stability while allowing for growth.
Liskov Substitution Principle (LSP)
While the current implementation does not include inheritance, it allows for future extensions:

If a specialized parking lot class (e.g., for electric vehicles) is created, it can inherit from ParkingLot and override methods as needed.
The behavior of the code should remain consistent when subclasses are used, adhering to LSP.
Interface Segregation Principle (ISP)
The ParkingLot class provides a focused interface:

Users interact with methods directly related to parking management without unnecessary complexity.
If additional features are required (such as logging), they can be implemented in separate classes or modules without cluttering the existing interface.
Dependency Inversion Principle (DIP)
The design of the parking system currently has minimal external dependencies:

Future enhancements could involve integrating a database or a user interface, allowing for easy dependency management.
This principle ensures that high-level modules (like user interactions) do not depend on low-level modules (like data storage) directly, promoting a decoupled architecture.
conslusion
This README provides an overview of the software design principles applied in the car parking system, highlighting key programming concepts that enhance its structure and functionality. For further questions or details, please refer to the code or contact the maintainer.