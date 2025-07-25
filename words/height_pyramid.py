# Total number of blocks (you can change this number for testing)
blocks = int(input("enter the number of blocks :"))  # <-- Replace with the test value

height = 0
needed = 1  # blocks needed for the current layer

while blocks >= needed:
    blocks -= needed
    height += 1
    needed += 1  # next layer requires one more block

print("Height of the pyramid:", height)
