'''if the word is bro it should break and type sorry  but if the word is not it should continue '''
while True:
    word = input("Enter a word: ")

    if word == "chupacabra":
        print("You've successfully left the loop.")
        break  # Exit the loop
    else:
        continue  # Skip to the next iteration
