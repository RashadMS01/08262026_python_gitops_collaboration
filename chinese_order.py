print ("Hello World")

chinese_dish = "Combination Lo Mein"
dish_count = 2
price_per_dish = 10
dinner_budget = 40

##This function prints order details
def print_order_details():
    print("")
    print (chinese_dish)
    print (dish_count)
    print (price_per_dish)
    print (dinner_budget)
    
# print ("function call #1")
# print_order_details()

# print ("function call #2")
# print_order_details()

def print_order_with_vars(var1, var2, var3, var4):
    print(f"chinese_dish is {var1}. dish_count is {var2}. price_per_dish is {var3}. dinner_budget is {var4}")

print("function call #3")
print_order_with_vars(chinese_dish, dish_count, price_per_dish, dinner_budget)

print("")

print("function call #4")
print_order_with_vars("BBQ Ribs", 2, 12, 40)