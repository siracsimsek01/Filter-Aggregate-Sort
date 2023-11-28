from players import players


#Helper function to get the sorting key
def get_key(player, sort_key):
    return player[sort_key]

# Function to sort the list by anything in ascending or descending order

def sorting_players(players, sort_key):
    
    # Custom key for sorting
    
    def custom_key(player):
        return get_key(player, sort_key)
    
    # Using the sorted function with the custom key function
    
    sorted_players = sorted(players, key=custom_key)
    
    # Excluding sorted names and surnames from the list
    
    sorted_names = []
    for player in sorted_players:
        name_string = f"{player['name']} {player['surname']}"
        if sort_key not in ['name', 'surname']:
            name_string += f" {player[sort_key]}"
        sorted_names.append(name_string)

    return sorted_names    




# Example Usage
sorted_by_age = sorting_players(players, 'age') 
sorted_by_name = sorting_players(players, 'name')  

# Printing results
print("Sorted Players by Age:", sorted_by_age)
print("Sorted Players by Name:", sorted_by_name)




