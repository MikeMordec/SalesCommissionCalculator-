# SalesCommissionCalculator

A Python application designed to calculate commissions, gross income, and total commissions for a set of salespeople based on their sales data stored in a dictionary. This project provides an efficient way to analyze sales performance and commission structures.

## Features

- **Commission Calculation**: Calculates the commission for each salesperson based on their earnings and commission rates.
- **Gross Income Calculation**: Computes the gross income by adding base sales to commissions.
- **Total Commission Summary**: Provides a summary of total commissions earned across all salespeople.
- **Key Inclusion Check**: Allows users to verify if a specific salesperson's name exists in the records.

## How It Works

1. **Data Structure**: Sales data is stored in a dictionary where each key is a salesperson's name, and the value is a list containing:
   - Base sales
   - Total earnings
   - Commission rate

2. **Calculations**:
   - **Commission**: Calculated as `total earnings * commission rate * 0.01`.
   - **Gross Income**: Calculated as `base sales + commission`.

3. **User Interaction**:
   - The program prompts the user to enter a salesperson's name to check if it exists in the records.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SalesCommissionCalculator.git

    Navigate to the project directory:

    bash

    cd SalesCommissionCalculator

    Ensure you have Python installed on your system.

Usage

    Run the main script:

    bash

    python main.py

    Follow the on-screen prompts to view commission calculations and input salesperson names for key checks.

Code Structure

    main.py: The main script that executes the program and handles calculations and user interactions.

Example Output

plaintext

Commission: 
Clarence Carson: 32.0
Daphne Danvers: 39.0

Gross Income: 
Clarence Carson: 282.0
Daphne Danvers: 639.0

Total Commission: 
Total: 71.0

please enter a key to search
Clarence Carson
the key exists in the dictionary

