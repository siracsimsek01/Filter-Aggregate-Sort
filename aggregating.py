# Aggregating Algorithm

from players import players



# Function to calculate average overall score by key
def average_overall(players, key):
    totals = {}
    counts = {}

    for player in players:
        key_value = player[key]
        overall_score = player["overall"]

        if key_value in totals:
            totals[key_value] += overall_score
            counts[key_value] += 1
        else:
            totals[key_value] = overall_score
            counts[key_value] = 1

    averages = {}
    for key_value in totals:
        average_score = totals[key_value] / counts[key_value]
        averages[key_value] = average_score

    return averages


# Example Usage
average_by_age = average_overall(players, "country")
average_by_country = average_overall(players, "team")
# Printing results
print("Average Overall by Team:", average_by_age)
print("Average Overall by Country:", average_by_country)



