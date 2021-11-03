from datetime import datetime

class OrderItem:
    pass

class Order:
    """
    class that defines an Order entity, which represents a transaction
    between a selling business and a Customer
    """

    def __init__(self, _id: str, _customer_id: int, _item: OrderItem, _date: datetime = datetime.now() ):
        """
        Constructor
        :param _id: stock keeping unit (SKU) (private, final, cannot be altered)
        :param _description: description of article or stock unit
        :param _date: date of order, defaults to 0
        """
        self.__id = _id                   # private, final attribute, cannot be altered
        self.__customer_id = _customer_id
        self.__date = _date
        self.__items = [_item]

    def get_id(self) -> int:
        """
        id getter, returns private order identifier
        :return: order identifier
        """
        return self.__id

    def get_customer_id(self) -> int:
        """
        customer id getter, returns private customer identifier
        :return: customer identifier
        """
        return self.__customer_id

    def get_date(self) -> int:
        """
        order date getter, returns private order date
        :return: order date
        """
        return self.__date

    def add_item(self, _sku: str, _units: int) -> int:
        """  
        """
        self.__items.append(OrderItem(_sku,_units))

    def items_count(self) -> int:
        """
        number of items counter, returns number of items in order
        :return: number of items in order
        """
        return len(self.__items)

    def get_item(self, i: int) -> OrderItem:
        """
        item getter, returns Order item by index
        :return: order i-th item  
        """
        return self.__items[i]

class OrderItem:
    def __init__(self, _sku: str, _units: int):
        """
        Constructor
        :param _sku: ordered item as stock keeping unit (SKU) id in Stock
        :param _units: ordered units
        """
        self.__sku = _sku       # private, final attribute, cannot be altered
        self.units = _units

    def get_sku(self):
        return self.__sku

def customer_id_func(_o: Order) -> int:
    """
    customer id getter, returns private customer identifier
    return customer id of order
    :param _c: customer object
    :return: last name part of name attribute
    """
    return _o.get_customer_id()
