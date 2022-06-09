# class ItemDiscount:
#
#     def __init__(self, title, price, discount):
#         self.__title = title
#         self.__price = price
#         self.discount = discount
#
#     @property
#     def get_title(self):
#         return self.__title
#
#     @property
#     def get_price(self):
#         return self.__price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_price(self, price):
#         if price < 0:
#             raise ValueError("price cannot be negative")
#         self.__price = price

class ItemTitle():
    def get_info(self, title):
        return title


class ItemPrice():
    def get_info(self, price, discount):
        return price - (price / 100 * discount)

b = ItemTitle()
c = ItemPrice()

print(b.get_info("marker"))
print(c.get_info(20, 5))

