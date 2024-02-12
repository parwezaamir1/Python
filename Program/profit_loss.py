# Write a program that will take user input of cost price and selling price 
# and determines whether its a loss or a profit

def calculate_profit_loss(cost_price, selling_price):
    """Calculate profit or loss."""
    if selling_price > cost_price:
        return "Profit"
    elif selling_price < cost_price:
        return "Loss"
    else:
        return "No profit, no loss"

try:
    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))

    result = calculate_profit_loss(cost_price, selling_price)
    print("You made a", result)
except ValueError:
    print("Please enter valid numerical values for cost price and selling price.")
