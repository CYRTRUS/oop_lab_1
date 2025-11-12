# Cities and Countries Data Analysis Lab

## Lab Overview

This lab focuses on data processing and analysis of cities and countries' data using object-oriented programming principles. The project implements a mini-database system that can load, filter, join, and aggregate data from CSV files containing information about cities (including temperature, coordinates) and countries (including population, EU membership, and coastline status).

## Project Structure

```bash
oop_lab_1/
├── README.md # Project documentation
├── Cities.csv # Dataset containing city information (name, country, coordinates, temperature)
├── Countries.csv # Dataset containing country information (population, EU membership, coastline)
└── data_processing.py # Main analysis code with DataLoader, DB, and Table classes
```

## Design Overview

### DataLoader Class

Handles file operations and CSV data loading with path resolution.

**Attributes:**

- `base_path`: Path object representing the directory where data files are located

**Key Methods:**

- `__init__(base_path=None)`: Initializes the DataLoader with an optional base path (defaults to script directory)
- `load_csv(filename)`: Loads a CSV file and returns its contents as a list of dictionaries

### DB Class

Implements a simple database system to store and retrieve tables.

**Attributes:**

- `tables`: Dictionary storing table names as keys and Table objects as values

**Key Methods:**

- `insert(table)`: Adds a Table object to the database
- `search(table_name)`: Retrieves a Table object by name from the database

### Table Class

Represents a tabular dataset and provides methods for data manipulation and analysis.

**Attributes:**

- `table_name`: String representing the table name
- `table`: List of dictionaries containing the actual data

**Key Methods:**

- `__init__(table_name, table)`: Initializes a Table with name and data
- `filter(condition)`: Filters the table based on a lambda function condition and returns a new Table
- `aggregate(aggregation_function, aggregation_key)`: Performs aggregation operations (sum, average, min, max, count) on specified columns
- `join(other_table, key)`: Performs an inner join with another table on a specified key column
- `__str__()`: Returns a string representation of the table

## How to Test and Run Your Code

### Running the Code

1. Navigate to the project directory containing all the files
2. Run the script using Python:

```bash
python data_processing.py
```
