class Stock:
    """
    class that defines a Stock entity, which can be ordered
    """

    def __init__(self, _id: str, _description: str = "", _price: int = 0, _units_available: int = 0):
        """
        Constructor of class
        :param _id: stock keeping unit (SKU) (private, final, cannot be altered)
        :param _description: description of article or stock unit
        :param _price: price (private, in cent)
        :param _units_available: units available in stock (private)
        :param _category: stock category
        """
        self.__sku = _id                            # private, final, cannot be altered
        self.description = _description
        #self.__price = 0                            # private
        #self.set_price(_price)
        #self.__units_available = _units_available   # private

    def get_id(self) -> int:
        """
        id getter, returns private order identifier
        :return: order identifier
        """
        return self.__sku
    # TODO: complete class
