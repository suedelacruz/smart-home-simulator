# Smart Home Simulator

## Project Overview

The Smart Home Simulator is an object oriented Python application that simulates a modern smart home environment. The system manages smart devices, sensors, users, automation rules, notifications, and energy monitoring.

The project demonstrates software engineering concepts including SOLID principles, design patterns, layered architecture, persistence, and automated event processing.

---

## Architecture

The project follows a layered architecture:

* Domain Layer

  * Devices
  * Sensors
  * Users
  * Automation
  * House

* Service Layer

  * Automation Engine
  * Notification Service
  * Energy Service
  * Logger

* Repository Layer

  * JSON Repository

* Factory Layer

  * Device Factory

---

## Design Patterns Used

### Factory Pattern

Used to create smart devices without directly instantiating device classes.

Example:

```python
DeviceFactory.create_device(...)
```

### Observer Pattern

Sensors notify the Automation Engine when events occur.

Example:

* MotionSensor detects movement
* AutomationEngine receives event
* AutomationRule executes actions

### Strategy Pattern

Energy calculation algorithms can be changed dynamically.

Examples:

* NormalEnergyStrategy
* EcoEnergyStrategy

### Singleton Pattern

Logger is implemented as a Singleton to ensure only one instance exists.

---

## SOLID Principles

### Single Responsibility Principle (SRP)

Each class has one responsibility.

Examples:

* SmartDevice manages device behavior.
* JsonRepository manages persistence.
* NotificationService manages notifications.

### Open/Closed Principle (OCP)

New device types and strategies can be added without modifying existing code.

### Liskov Substitution Principle (LSP)

All SmartDevice subclasses can be used wherever a SmartDevice is expected.

### Interface Segregation Principle (ISP)

Separate abstractions are used for devices, sensors, and services.

### Dependency Inversion Principle (DIP)

Services depend on abstractions and strategies rather than concrete implementations.

---

## Features

* Smart Device Hierarchy
* Sensor Hierarchy
* Automation Rules
* Event Processing
* Notifications
* Energy Monitoring
* User Roles
* JSON Persistence
* Unit Testing

---

## Testing

The project includes 8 unit tests covering:

* Device state changes
* Factory creation
* User roles
* Room management
* House management
* Singleton behavior

Run tests:

```bash
python3 -m unittest tests/test_smart_home.py
```

---

## Running the Project

Run the Smart Home Simulator:

```bash
python3 main.py
```

---

## Future Improvements

* Web Dashboard
* Mobile Notifications
* Database Integration
* Advanced Automation Rules
* AI-Based Energy Optimization

