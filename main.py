# TASK 1

from players import players
from filtering import filter_players
from aggregating import average_overall
from sorting import sorting_players

'''
!!! To test the algorithms, you need to comment out the tasks you are not working on !!!

'''

# Filtering players by position, overall, country and age.

filtered_by_position = filter_players(players, "position", "Striker")
filtered_by_overall = filter_players(players, "overall", 88)
filtered_by_country = filter_players(players, "country", "Uruguay")
filtered_by_age = filter_players(players, "age", 30)


# # This shows the output of the filtered players properly

print("\nPlayers filtered by position:")
for players in filtered_by_position:
    print(players)

print("\nPlayers filtered by overall:")
for players in filtered_by_overall:
    print(players)

print("\nPlayers filtered by country:")
for players in filtered_by_country:
    print(players)

print("\nPlayers filtered by age:")
for players in filtered_by_age:
    print(players)


# TASK 2

average_by_age = average_overall(players, "age")
average_by_country = average_overall(players, "country")

print("\nAverage Overall by Age:")
for key in average_by_age:
    print(key, ":", average_by_age[key])
    
print("\nAverage Overall by Country:")
for key in average_by_country:
    print(key, ":", average_by_country[key])   
    
# TASK 3

sorted_by_age = sorting_players(players, 'age')
sorted_by_name = sorting_players(players, 'name')

print("\nSorted Players by Age:")
for players in sorted_by_age:
    print(players)
    
print("\nSorted Players by Name:")
for players in sorted_by_name:
    print(players)  
    