from C1_order_system.datamodel import Customer


class CustomerDataStore:
    """
    class that defines a container to hold Customer objects and
    provide functions to access, filter and query data
    """

    def __init__(self):
        """
        Constructor
        """
        # print(f'CustomerDataStore singleton instantiated')
        self.__data = {}        # data dictionary, private, final, cannot be altered

    def add_customer(self, _customer: Customer):
        self.__data[_customer.get_id()] = _customer

    def remove_customer(self, _customer_id: int):
        self.__data.pop(_customer_id, None)     # remove key from dict, return object if key existed or None otherwise

    def size(self) -> int:
        return len(self.__data)

    def find_customer_by_id(self, _id: int) -> Customer:
        return self.__data.get(_id)    # get(key) returns None if key is not found

    def find_all_customers(self) -> []:
        return list(self.__data.values())

    def filter(self, _filter_func: bool) -> [Customer]:
        _filtered = []
        for c in self.__data.values():
            if _filter_func(c):
                _filtered.append(c)
        # shorter with build-in filter() function, list() converts filtered-object to list[]
        # _filtered = list(filter(_filter_func, self.__data.values()))
        return _filtered
