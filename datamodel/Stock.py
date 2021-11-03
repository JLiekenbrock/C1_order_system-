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
        self.__price = _price                            # private
        self.__units_available = _units_available   # private

    def get_sku(self) -> int:
        """
        id getter, returns private order identifier
        :return: order identifier
        """
        return self.__sku
        
    def get_price(self) -> int:
        """
        price getter, returns price
        :return: order price
        """
        return self.__price
            
    def set_price(self, _price) -> int:
        """
        price setter, sets price
        """
        self.__price = _price

    def get_units_available(self) -> int:
        """
        units available getter, returns number of available units
        :return: number of available units
        """
        return self.__units_available

    def has_units_available(self) -> bool:
        """
        units available getter, returns wheter units are available
        :return: are units availabe
        """
        return self.__units_available > 0

    def transact_units(self, _n: int) -> bool:
        """
        transact units
        :return: wether transaction finished
        """
        valid = self.__units_available >= _n
        if valid:
            self.__units_available -= _n   
        return valid  


