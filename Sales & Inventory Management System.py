import csv
import os

filename = "products.csv"


def load_products():
    products = []

    if os.path.exists(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["price"] = float(row["price"])
                row["quantity"] = int(row["quantity"])
                row["sold"] = int(row["sold"])
                products.append(row)

    return products


def save_products(products):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["name", "price", "quantity", "sold"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for product in products:
            writer.writerow(product)


products = load_products()


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter available quantity: "))
    sold = int(input("Enter sold quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "sold": sold
    }

    products.append(product)
    save_products(products)

    print("Product added successfully!\n")


def view_products():
    if not products:
        print("No product records found.\n")
        return

    print("\n--- Product List ---")

    for product in products:
        print(product)

    print()


def search_product():
    name = input("Enter product name to search: ")

    for product in products:
        if product["name"].lower() == name.lower():
            print("\nProduct Found:")
            print(product)
            print()
            return

    print("Product not found.\n")


def update_stock():
    name = input("Enter product name to update stock: ")

    for product in products:
        if product["name"].lower() == name.lower():
            new_quantity = int(input("Enter new quantity: "))
            product["quantity"] = new_quantity

            save_products(products)
            print("Stock updated successfully!\n")
            return

    print("Product not found.\n")


def delete_product():
    name = input("Enter product name to delete: ")

    for product in products:
        if product["name"].lower() == name.lower():
            products.remove(product)

            save_products(products)
            print("Product deleted successfully!\n")
            return

    print("Product not found.\n")


def low_stock_alert():
    print("\n--- Low Stock Products ---")
    found = False

    for product in products:
        if product["quantity"] < 5:
            print(product)
            found = True

    if not found:
        print("No low stock products found.")

    print()


def total_revenue():
    revenue = 0

    for product in products:
        revenue += product["price"] * product["sold"]

    print(f"Total Revenue: ₹{revenue}\n")


def best_selling_product():
    if not products:
        print("No product records found.\n")
        return

    best = max(products, key=lambda x: x["sold"])

    print("\n--- Best Selling Product ---")
    print(best)
    print()


def profit_calculation():
    total_profit = 0

    for product in products:
        cost_price = product["price"] * 0.7
        profit = (product["price"] - cost_price) * product["sold"]
        total_profit += profit

    print(f"Estimated Total Profit: ₹{total_profit}\n")


while True:
    print("====== Sales & Inventory Management System ======")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Low Stock Alert")
    print("7. Total Revenue")
    print("8. Best Selling Product")
    print("9. Profit Calculation")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        low_stock_alert()

    elif choice == "7":
        total_revenue()

    elif choice == "8":
        best_selling_product()

    elif choice == "9":
        profit_calculation()

    elif choice == "10":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.\n")