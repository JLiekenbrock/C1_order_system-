from C1_order_system.datamodel import Order


class OrderDataStore:
    """
    class that defines a container to hold Order objects and
    provide functions to access, filter and query data
    """

    def __init__(self):
        """
        Constructor
        """
        # print(f'OrderDataStore singleton instantiated')
        self.__data = {}

    def add_order(self, _order: Order):
        self.__data[_order.get_id()] = _order

    def remove_order(self, _order_id: int):
        self.__data.pop(_order_id, None)  # remove key from dict, return object if key existed or None otherwise

    def size(self) -> int:
        return len(self.__data)

    def find_order_by_id(self, _id: int) -> Order:
        return self.__data.get(_id)  # get(key) returns None if key is not found

    def find_all_orders(self) -> []:
        return list(self.__data.values())

    def filter(self, _filter_func: bool) -> [Order]:
        _filtered = []
        for o in self.__data.values():
            if _filter_func(o):
                _filtered.append(o)
        # shorter with build-in filter() function, list() converts filtered-object to list[]
        # _filtered = list(filter(_filter_func, self.__data.values()))
        return _filtered

