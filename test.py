items = {   "8500015419386":{"name":"Aspire Black Raspberry",
                                "price": 2.50,
                                "category": "Energy Drink"},
            "041220883592": {"name":"HEB Peanuts",
                                "price": 5.00,
                                "category": "Snack"},
            "300672000248": {"name":"Ibuprofen",
                                "price": 6.00,
                                "category":"Medicine"}
        }

total_bill = 0
bill = []

while True:
    print("Scan your BarCode")
    value = input()
    if value == "exit":
        break

    for key in items.keys():
        if key == value:
            item = items[key]
            print(f"This is: {item['name']}, Price is: {items['price']}")
            total_bill += item['price']
            break
        else:
            print("Item Not Found", value)

for i, item in enumerate(bill):
    print(f"{i}, item['name'], item['price']")

print(f'Your total cost is: Rs.{total_bill}')