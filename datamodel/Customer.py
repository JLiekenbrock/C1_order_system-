class Customer:
    """
    class that defines a Customer entity, who is the subject of an order
    """

    def __init__(self, _id: int, _name: str = "", _address: str = "", _phone: str = ""):
        """
        Constructor of class
        :param _id: customer identifier (private, final, cannot be altered)
        :param _name: customer name (default="")
        :param _address: customer address (default="")
        :param _phone: customer phone number (default="")
        """
        self.__id = _id  # private, final attribute, cannot be altered
        self.name = _name
        self.address = _address
        self.phone = _phone

    def get_id(self) -> int:
        """
        id getter, returns private customer identifier
        :return: customer identifier
        """
        return self.__id


def last_name_func(_c: Customer) -> str:
    """
    return lastname part of customer name, e.g. "Megan Cantrell" -> "Megan "Cantrell"
    :param _c: customer object
    :return: last name part of name attribute
    """
    return _c.name[_c.name.index(" ") + 1:] if " " in _c.name else ""


def last_name_with_split(_c: Customer) -> str:
    _splits = _c.name.split(" ")
    if len(_splits) > 1:
        return _splits[1]
    return ""


def last_name_with_slice(_c: Customer) -> str:
    try:
        _i = _c.name.index(" ") + 1  # index throws ValueError exception
        return _c.name[_i:]
    except ValueError:
        return ""
