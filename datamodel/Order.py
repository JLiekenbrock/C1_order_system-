from datetime import datetime


class Order:
    """
    class that defines an Order entity, which represents a transaction
    between a selling business and a Customer
    """

    def __init__(self, _id: str, _customer_id: int, _date: datetime = datetime.now()):
        """
        Constructor
        :param _id: stock keeping unit (SKU) (private, final, cannot be altered)
        :param _description: description of article or stock unit
        :param _price: price (private, in cent)
        :param _units_available: units available in stock (private)
        :param _category: stock category
        """
        self.__id = _id                   # private, final attribute, cannot be altered
        self.customer_id = _customer_id
        self.date = _date

    def get_id(self) -> int:
        """
        id getter, returns private order identifier
        :return: order identifier
        """
        return self.__id
    # TODO: complete class


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

def customer_id_func(_o: Order) -> str:
    """
    return lastname part of customer name, e.g. "Megan Cantrell" -> "Megan "Cantrell"
    :param _c: customer object
    :return: last name part of name attribute
    """
    return _o.customer_id
