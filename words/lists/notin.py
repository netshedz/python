# Hard-coded source list (you can change it to test with different numbers)
source_list = [4, 5, 6, 4, 7, 5, 8, 9, 6, 10]

# Temporary list to store unique numbers
unique_list = []

# Iterate over each element in the source list
for number in source_list:
    if number not in unique_list:
        unique_list.append(number)

# Display the original and cleaned-up lists
print("Original list:", source_list)
print("List with duplicates removed:", unique_list)
