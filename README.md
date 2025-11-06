# Cities Data Analysis Lab

## Lab Overview

This lab focuses on data processing and analysis of European city climate data. The project demonstrates object-oriented programming principles by implementing data loading, filtering, and aggregation operations on a dataset containing information about various European cities, including their geographical coordinates and temperature readings.

The lab showcases practical data manipulation techniques using Python, including:
- CSV file handling and data loading
- Data filtering based on various criteria
- Statistical aggregation operations
- Method chaining for complex queries

## Project Structure
```bash
oop_lab_1/
├── README.md # This documentation file
├── Cities.csv # Dataset containing city information
└── data_processing.py # Main analysis code with DataLoader and Table classes
```

## Code Overview

### DataLoader Class

The `DataLoader` class handles file operations and CSV data loading.

**Attributes:**
- `base_path`: Path object representing the directory where data files are located

**Key Methods:**
- `__init__(base_path=None)`: Initializes the DataLoader with an optional base path
- `load_csv(filename)`: Loads a CSV file and returns its contents as a list of dictionaries

### Table Class

The `Table` class represents a tabular dataset and provides methods for data manipulation and analysis.

**Attributes:**
- `header`: String representing the table header/name
- `table`: List of dictionaries containing the actual data

**Key Methods:**
- `__init__(header, table)`: Initializes a Table with header and data
- `filter(condition)`: Filters the table based on a lambda function condition and returns a new Table
- `aggregate(aggregation_function, aggregation_key)`: Performs aggregation operations on specified columns

## How to run the code

### Running the Code

1. Ensure all files (`data_processing.py` and `Cities.csv`) are in the same directory
2. Run the script using Python:

```bash
python data_processing.py