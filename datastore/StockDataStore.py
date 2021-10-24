from C1_order_system.datamodel import Stock


class StockDataStore:
    """
    class that defines a container to hold Stock objects and
    provide functions to access, filter and query data
    """

    def __init__(self):
        """
        Constructor
        """
        # print(f'CustomerDataStore singleton instantiated')
        self.__data = {}  # data dictionary, private, final, cannot be altered

    def add_stock(self, _stock: Stock):
        self.__data[_stock.get_id()] = _stock

    def remove_stock(self, _stock_id: int):
        self.__data.pop(_stock_id, None)  # remove key from dict, return object if key existed or None otherwise

    def size(self) -> int:
        return len(self.__data)

    def find_stock_by_id(self, _id: int) -> Stock:
        return self.__data.get(_id)  # get(key) returns None if key is not found

    def find_all_stocks(self) -> []:
        return list(self.__data.values())

    def filter(self, _filter_func: bool) -> [Stock]:
        _filtered = []
        for s in self.__data.values():
            if _filter_func(s):
                _filtered.append(s)
        # shorter with build-in filter() function, list() converts filtered-object to list[]
        # _filtered = list(filter(_filter_func, self.__data.values()))
        return _filtered
