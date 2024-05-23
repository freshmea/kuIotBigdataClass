class Product:
    pass

class Inventory:
    def __init__(self):
        self.__item = []

    def add_new_item(self, product):
        if type(product) == Product:
            self.__item.append(product)
            print("새로운 아이템 추가됨")
        else:
            raise ValueError("Product 타입이 아닙니다.")

    def get_number_of_items(self):
        return len(self.__item)
    
    @property
    def items(self):
        return self.__item


def main():
    inven = Inventory()
    # print(inven.__item)
    inven.add_new_item(Product())
    inven.add_new_item(Product())
    print(inven.items)
    # inven.add_new_item("Product")
    print(inven.get_number_of_items())

if __name__ == '__main__':
    main()
