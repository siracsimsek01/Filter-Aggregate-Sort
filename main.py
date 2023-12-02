# Example dataset
dataset = [
    #  { "name": "James", "class": "FC01", "exam score": 75, "coursework score": 45 },
    #  { "name": "Natasha", "class": "FC02", "exam score": 95, "coursework score": 85 },
    #  { "name": "Kumail", "class": "FC02", "exam score": 85, "coursework score": 75 },
    #  { "name": "Tariq", "class": "FC01", "exam score": 75, "coursework score": 55 },
    #  { "name": "Qimeng", "class": "FC01", "exam score": 80, "coursework score": 80 },
    #  { "name": "Ming", "class": "FC02", "exam score": 90, "coursework score": 75 }


    {"name": "Mauro", "surname": "Icardi", "position": "Striker", "age": 30, "overall": 90, "country": "Argentina", "team": "Galatasaray"},
    {"name": "Fernando", "surname": "Muslera", "position": "Goalkeeper", "age": 37, "overall": 85, "country": "Uruguay", "team": "Galatasaray"},
    {"name": "Wilfred", "surname": "Zaha", "position": "Striker", "age": 30, "overall": 90, "country": "Ireland", "team": "Galatasaray"},
    {"name": "Lucas", "surname": "Torreira", "position": "Midfielder", "age": 27, "overall": 88, "country": "Uruguay", "team": "Galatasaray"},
    {"name": "Sacha", "surname": "Boey", "position": "Defender", "age": 23, "overall": 88, "country": "France", "team": "Galatasaray"},
    {"name": "Ederson", "surname": "Moraes", "position": "Goalkeeper", "age": 30, "overall": 90, "country": "Brazil", "team": "Manchester City"},
    {"name": "Jeremy", "surname": "Doku", "position": "Striker", "age": 30, "overall": 90, "country": "Belgium", "team": "Manchester City"},
    {"name": "Erling", "surname": "Haaland", "position": "Striker", "age": 23, "overall": 95, "country": "Norway", "team": "Manchester City"},
    {"name": "Kevin", "surname": "De Bruyne", "position": "Midfielder", "age": 30, "overall": 95, "country": "Belgium", "team": "Manchester City"},
    {"name": "Phil", "surname": "Foden", "position": "Midfielder", "age": 23, "overall": 90, "country": "England", "team": "Manchester City"},
    {"name": "Manuel", "surname": "Neuer", "position": "Goalkeeper", "age": 37, "overall": 95, "country": "Germany", "team": "Bayern Munich"},
    {"name": "Harry", "surname": "Kane", "position": "Striker", "age": 30, "overall": 95, "country": "England", "team": "Bayern Munich"},
    {"name": "Thomas", "surname": "Muller", "position": "Midfielder", "age": 30, "overall": 95, "country": "Germany", "team": "Bayern Munich"},
    {"name": "Jamal", "surname": "Musiala", "position": "Midfielder", "age": 23, "overall": 90, "country": "Germany", "team": "Bayern Munich"},
    {"name": "Leroy", "surname": "Sane", "position": "Midfielder", "age": 23, "overall": 90, "country": "Germany", "team": "Bayern Munich"}


]

# Filtering function
def filter_data(data_list, key, value):
    # initialize empty list
    filtered_list = []
    
    for item in data_list:
 # if the condition is true add the item to the filtered_list
        if item[key] == value:
            filtered_list.append(item)
    return filtered_list

# Aggregating function
def calculate_average(data, key):
    
    # initialize total and count variables
    total = 0
    count = 0

# loop through the data and add the values to the total and increment the count
    for item in data:
        if key in item:
            total += item[key]
            count += 1

    # calculate the average
    if count > 0:
        average = total / count
    else:
        average = 0

    return average


# Sorting function 
def sort_data(data, sort_key):
    def custom_key(item):
        return item[sort_key]
    # Using the sorted function with the custom key 
    sorted_data = sorted(data, key=custom_key)
    
    # Excluding sorted names and surnames from the list
    sorted_names = []
    for item in sorted_data:
        name_string = f"{item['name'], item['surname']}"
        if sort_key not in ['name']:
            name_string += f" {item[sort_key]}"
        sorted_names.append(name_string)
        #Returning the new list
    return sorted_names

# Main function
def main():
    while True:
        print("Choose an operation: \n1. Filter \n2. Sort \n3. Aggregate")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Filtering
            key = input("Enter the filter key: ")
            value = input("Enter the filter value: ")
            result = filter_data(dataset, key, value)
            print("Filtered Data:")
            for item in result:
                print(item)

        elif choice == '2':
            # Sorting
            sort_key = input("Enter the sort key: ")
            result = sort_data(dataset, sort_key)
            print("Sorted Data:")
            for item in result:
                print(item)

        elif choice == '3':
            # Aggregating
            key = input("Enter the key for average calculation (e.g., age): ")
            average_value = calculate_average(dataset, key)
            print(f"Average {key.capitalize()}: {average_value}")


        else:
            print("Invalid choice.")

        another_operation = input("Do you want to perform another operation? (yes/no): ")
        if another_operation.lower() != "yes":
            print("Thank you for using the program 😇. To use it again, run 'python3 main.py' on the terminal.")
            break
# Call the main function
if __name__ == "__main__":
    main()
