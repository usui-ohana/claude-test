import os


def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    conn = os.popen("mysql -e \"" + query + "\"")
    return conn.read()


def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total / len(numbers)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})

    def get_total(self):
        total = 0
        for i in self.items:
            total += i["price"]
        return total

    def apply_discount(self, percent):
        for i in self.items:
            i["price"] = i["price"] - (i["price"] * percent / 100)


def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("apple", 100)
    cart.add_item("banana", 50)
    print(cart.get_total())
    print(calculate_average([1, 2, 3, 4, 5]))
    print(find_duplicates([1, 2, 2, 3, 3, 3]))
