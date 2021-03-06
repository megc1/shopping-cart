# shopping_cart.py
import datetime
#Basic Challenge: Formatting Prices
def to_usd(price):
    return "${0:,.2f}".format(price)

#Basic Challenge: Formatting Timestamps
#Reference: https://docs.python.org/2/library/datetime.html
def human_friendly_timestamp(time):
    formatted_time = time.strftime("%B %d %Y ") + " at " + time.strftime("%I:%M%p")
    return formatted_time

#Intermediate Challenge: Find product
def find_product(ids, products):
    matching_products = [p for p in products if str(p["id"]) == str(ids)]
    matching_product = matching_products[0]
    return matching_product

def calculate_total_price(total_price):
    tax = total_price * .06
    total = total_price + tax
    return total

if __name__ == "__main__":
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] 

    total_price = 0
    selected_ids = []

    while True: 
        selected_id = input("Please input a product identifier. Enter \"DONE\" if finished. ")
        if selected_id == "DONE":
            break
        elif int(selected_id) < 1:
            print("Are you sure this product identifier is correct? Please try again!")
            continue
        elif int(selected_id) > 20:
            print("Are you sure this product identifier is correct? Please try again!")
            continue
        else:
            selected_ids.append(selected_id)

    my_time = human_friendly_timestamp(datetime.datetime.today())
    line_break = "\r\n" + "----------------------------------------------------------------" + "\r\n"
    store_name = "D.C. Grocery"
    website = "www.dcgrocery.com"
    phone = "+1 (123)-456-7899"
    print(line_break + store_name + line_break + "\r" + website + "\r\n" + phone + "\r\n" + "Start Time: " + my_time + line_break + "Items in Cart: ")
    for selected_id in selected_ids:
        matching_product = find_product(selected_id, products)
        total_price = total_price + matching_product["price"]
        print(" ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")
    print(line_break + "Subtotal: " + str('${:,.2f}'.format(total_price)))
    tax = total_price * .06
    print("Plus tax: " + str('${:,.2f}'.format(tax)))
    total = calculate_total_price(total_price)
    print("Total: " + str('${:,.2f}'.format(total)))
    print("Thank you for shopping at D.C. Grocery! We hope to see you soon!")
