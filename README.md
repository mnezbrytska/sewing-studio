# this project will be changed!!!

# Sewing Studio Management System

 for lad data -> python manage.py loaddata data.json


This project is a **Django-based application** designed to manage the operations of a sewing studio. The system helps to manage customers, tailors, orders, and the services provided. It allows for tracking orders, assigning tailors, and calculating service costs.

## 

- **Customer Management**: Add, edit, and manage customer information, including name, phone number, and email.
- **Tailor Management**: Manage tailors who are responsible for fulfilling orders, using Django’s `AbstractUser` model for user authentication and profile management.
- **Service Management**: Define various services offered by the sewing studio, each with a specific price.
- **Order Management**:
    - Create and manage customer orders.
    - Assign tailors to orders.
    - Add multiple services to an order.
    - Track the order’s progress through fields like `is_active`, `is_paid`, and `is_urgent`.
    - Automatically calculate the total price based on the selected services.

## Database Design

The system's data model includes the following entities:

1. **Customer**:
    - Stores basic customer details such as first name, last name, phone number, and email.
    - Customers can place multiple orders.
2. **Tailor**:
    - Inherits from Django’s `AbstractUser` model, storing tailor information and authentication data.
    - Tailors can be assigned to multiple orders.
3. **Service**:
    - Defines the types of services offered by the studio, each having a name and price.
    - Each order can include multiple services.
4. **Order**:
    - Stores information about individual orders such as start date, finish date, and a short description.
    - Linked to a customer and a tailor, and contains multiple services.
    - Flags like `is_active`, `is_paid`, and `is_urgent` are used to manage the order lifecycle.

![models.jpg](static%2Fimages%2Fmodels.jpg)