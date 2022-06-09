class ItemDiscount:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f"{self.title}, {self.price}")


a = ItemDiscount("pen", 20)

b = ItemDiscountReport("pencil", 15)

print(a.title)
print(a.price)
b.get_parent_data()
