def filter_players(players_list, key, value):
    # This function takes in a list of players, a key and a value as parameters.
    # It filters the players based on the given key and value and returns a new list of filtered players.

    filtered_list = []
    # Create an empty list to store the filtered players.

    for player in players_list:
        # Iterate over each player in the players_list.

        if player[key] == value:
            # Checks if the value of the specified key in the current player matches the given value.

            filtered_list.append(player)
            # If the condition is true, add the player to the filtered_list.

    return filtered_list
    # Return the filtered_list containing the filtered players.


# Example usage:

players = [
    {
        "name": "Mauro",
        "surname": "Icardi",
        "position": "Striker",
        "overall": 90,
        "country": "Argentina",
    },
    {
        "name": "Erling",
        "surname": "Haaland",
        "position": "Striker",
        "overall": 95,
        "country": "Norway",
    },
    {
        "name": "Manuel",
        "surname": "Neuer",
        "position": "Goal Keeper",
        "overall": 93,
        "country": "Germany",
    },
    {
        "name": "Lucas",
        "surname": "Torreira",
        "position": "Midfielder",
        "score": 85,
        "country": "Uruguay",
    },
    {
        "name": "Fernando",
        "surname": "Muslera",
        "position": "Goal Keeper",
        "score": 83,
        "country": "Uruguay",
    },
    {
        "name": "Lionel",
        "surname": "Messi",
        "position": "Striker",
        "score": 97,
        "country": "Argentina",
    },
]


filtered_by_position = filter_players(players, "position", "Striker")
# Call the players function to filter the players 

print(filtered_by_position)
# Print the filtered list of players.
