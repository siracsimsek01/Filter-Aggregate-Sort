# DataOps: Filter, Aggregate, Sort

 Filter, Aggregate, Sort is a Python-based tool designed to perform three key operations on datasets: filtering, aggregating, and sorting. This utility is especially useful in processing and analyzing structured data, such as in data science projects, database management, or any application where dataset manipulation is required.

## Features

- **Filter Data**: Selects and displays data based on specified criteria.
- **Aggregate Data**: Calculates averages or sums based on specific keys within the data.
- **Sort Data**: Organizes data in ascending order based on a chosen key.

## Installation

No installation required. Ensure you have Python installed on your system to run the scripts.

## Usage

To use DataOps, follow these steps:

1. Prepare your dataset in a Python list of dictionaries format.
2. Run `main.py`.
3. Choose the desired operation (Filter, Aggregate, Sort) by entering 1, 2, or 3.
4. Provide the necessary inputs as prompted.
5. View the processed results in the console.

### Example Dataset

Your dataset should be structured as a list of dictionaries. Each dictionary represents a data record. For example:

```python
dataset = [
    {"name": "John Doe", "age": 30, "occupation": "Engineer"},
    {"name": "Jane Smith", "age": 25, "occupation": "Designer"},
    # Add more records as needed
]
