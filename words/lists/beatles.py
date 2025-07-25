# Step 1: create an empty list named beatles
beatles = []

# Step 2: add John Lennon, Paul McCartney, and George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("The Beatles:", beatles)

# Step 3: prompt the user to add Stu Sutcliffe and Pete Best
for member in ["Stu Sutcliffe", "Pete Best"]:
    new_member = input(f"Add {member}: ")
    beatles.append(new_member)
    print("The Beatles:", beatles)

# Step 4: remove Stu Sutcliffe and Pete Best
del beatles[-1]  # Remove Pete Best
del beatles[-1]  # Remove Stu Sutcliffe
print("The Beatles:", beatles)

# Step 5: add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")
print("The Beatles:", beatles)

# Display the final list
print("The Fab", len(beatles))

