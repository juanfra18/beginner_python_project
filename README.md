# Flight and Passenger Management System - 2019 Python Course Project

This repository contains the final project for a begginer's python programming course taken in 2019. The project is a flight and passenger management system that stores flight and passenger data across two text files and allows for various management and query operations via a menu interface.

## Structure

- **Flights File**: Stores flight data, including flight number, departure location, destination, airline, maximum passenger capacity, and the current number of passengers on the flight.
- **Passengers File**: Stores passenger information, including DNI, first name, last name, and assigned flight.

## Features

The system includes a CLI menu with the following options:

### Flight Management
- **Create a flight**: Add a new flight with specified details.
- **Modify a flight**: Edit any details of a flight except the flight number and the current number of passengers.
- **Delete a flight**: Remove a flight from the system. If the flight has assigned passengers, either remove those passengers or prevent the deletion until the passengers are reassigned or removed.

### Passenger Management
- **Add a passenger**: Assign a passenger to an existing flight as long as the flight has capacity. Prevent duplicate passenger assignments to the same flight.
- **Modify a passenger**: Update passenger information, including reassignment to a different flight if needed.
- **Delete a passenger**: Remove a passenger from the system and update the passenger count for their assigned flight.

### Queries
- List all flights
- List flights by airline
- List all passengers
- List passengers for a specific flight
- List flights by destination

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/juanfra18/beginner_python_project.git
   ```
2. Navigate to the project directory and run the main program `Programa.py`.

## Requirements
- Python 3.x
