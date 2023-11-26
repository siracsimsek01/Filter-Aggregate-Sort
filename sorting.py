from players import players

# Function to sort the list by anything in ascending or descending order

def sorting_players(players, sort_key):
    """
    Sorts a list of players based on a specified key using built-in sorted function.
    Returns a list of player names and surnames in the sorted order.
    """
    # Sorting players using the sorted function and a custom sorting key
    sorted_players = sorted(players, key=lambda player: player[sort_key])

    # Extracting sorted names and surnames
    sorted_names = [f"{player['name']} {player['surname']} {player[sort_key]}" for player in sorted_players]
    
    # to avoid printing the name twice if the sort key is name or surname
    if sort_key == 'name' or sort_key == 'surname':
        sorted_names = [f"{player['name']} {player['surname']}" for player in sorted_players]
    
    return sorted_names

# Example Usage
sorted_by_age = sorting_players(players, 'age') 
sorted_by_name = sorting_players(players, 'name')  

# Printing results
print("Sorted Players by Age:", sorted_by_age)
print("Sorted Players by Name:", sorted_by_name)




