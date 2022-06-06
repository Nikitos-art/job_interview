class ItemDiscount:

    def __init__(self, title, price, discount):
        self.__title = title
        self.__price = price
        self.discount = discount

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

    def __init__(self, title, price, discount):
        super().__init__(title, price, discount)
        self.discount = discount

    def __str__(self):
        final_price = self.get_price - (self.get_price / 100 * self.discount)
        return f"The price is {final_price}"


# a = ItemDiscount("marker", 30, 5)
# print(a.get_title, a.get_price)

b = ItemDiscountReport("pencil", 15, 5)
print(b)
