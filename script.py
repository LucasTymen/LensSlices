# Your code below:

# Step 1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Step 2
prices = [2, 6, 1, 3, 2, 7, 2]

# Step 3
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Step 4
num_pizzas = len(toppings)
print(num_pizzas)

# Step 5
print("We sell "+str(num_pizzas)+" different kinds of pizza!")

# Step 6
pizza_and_prices = [[2,"pepperoni"], [6,"pineapple"], [1,"cheese"], [3,"sausage"], [2,"olives"], [7,"anchovies"], [2,"mushrooms"]]

# Step 7
print(pizza_and_prices)
print("##############################")

# Step 8
pizza_and_prices.sort()
print(pizza_and_prices)

# Step 9
cheapest_pizza = pizza_and_prices[0]
print("Len ==>  Our cheapest pizza is the " + str(cheapest_pizza) + " pizza")

# Step 10
print("Rich guy ===> what's the most exensive of all ??")
priciest_pizza = pizza_and_prices[-1]
print("Len ==>  Our more expensive pizza is the " + str(priciest_pizza) + " pizza")

# Step 11
print("##############################")
pizza_and_prices.pop()

# Step 12
pizza_and_prices.insert(4, [2.5,"peppers"])
print(pizza_and_prices)

# Step 13
three_cheapest = pizza_and_prices[:3]

# Step 14
print("the 3 cheapests : " + str(three_cheapest))
