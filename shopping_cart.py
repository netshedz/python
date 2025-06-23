#create a shopping cart program that will continuously ask the user  for a food product and price of that product
#have an exit clause if the user wishes to stop adding more things to their card
#At the end show the food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food you want to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter a price of the {food}: R"))
        foods.append(food)
        prices.append(price)

        # Print cart
        print("\n...YOUR CART....")
        
        for food in foods:
            print(food, end=" ")
            
            for price in prices:
                 print(f"R{price}")
            
        # Calculate and show total
        print("\n")
        total = sum(prices)
        print(f"Your total is: R{total}")
