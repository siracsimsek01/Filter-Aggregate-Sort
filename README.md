# ProPlayerProfiler

## Project Overview
SportStatSorter is a Python-based project focused on the processing and analysis of sports player data. This project demonstrates fundamental data manipulation techniques using Python, ideal for those in the early stages of learning programming. Key components of the project include:

1. **Filtering Algorithm**: Filters player data based on specified criteria.
2. **Aggregating Algorithm**: Aggregates player data to calculate averages based on specified keys.
3. **Sorting Algorithm**: Sorts player data based on any given key in ascending order.

## Installation

Ensure Python is installed on your machine. Clone this repository to your local machine using:

git clone [https://github.com/siracsimsek01/ProPlayerProfiler]


## Usage

### Filtering Algorithm
To filter player data based on a specific key-value pair:

```python
filtered_players = filter_players(players, 'country', 'USA')

average_overall_by_key = average_overall_by_key(players, 'age')

sorted_players = sorting_players(players, 'age')


