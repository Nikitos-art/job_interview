class ItemDiscount:

    def __init__(self, title, price):
        self.__title = title
        self.__price = price

    @property
    def get_title(self):
        return self.__title

    @property
    def get_price(self):
        return self.__price

    def set_title(self, title):
        self.__title = title

    def set_price(self, price):
        if price < 0:
            raise ValueError("price cannot be negative")
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.get_title, self.get_price)


a = ItemDiscount("pen", 20)
print(a.get_title)
print(a.get_price)


b = ItemDiscountReport("pencil", 15)
b.get_parent_data()
