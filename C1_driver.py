import sys
sys.path.append("..")   # Path hack needed to run from commandline
from C1_order_system.datamodel import Order, last_name_func, customer_id_func
from C1_order_system import cds, sds, ods

"""
Customer, Stock, Order, OrderItem are classes defined in the datamodel module.
Objects of these classes are business objects relevant for order processing.

cds, sds, ods are global singleton objects defined the C1_order_system_full module
(C1_order_system_full.__init__.py):
 - cds, data store with Customer objects (subjects in orders)
 - sds, data store with Stock objects (orderable items)
 - ods, data store with Order objects (represent orders with >= 1 ordered items)
"""


def print_order_items(o: Order) -> int:
    """
    Print value of an order by compounding all ordered items.
    :param o: order object
    :return: total value of order in cent
    """
    print(f"- order {o.get_id()} ({o.items_count()} item):")
    _order_value = 0
    #
    # TODO: complete logic, consider steps
    #   - look up items of the order
    #   - foreach item:
    #       - retrieve sku and ordered units from item
    #       - look up stock unit from sku in StockStore(sds)
    #       - look up price and description from stock unit
    #       - calculate value of ordered item
    #       - print line for item:
    #           print(f"  - {_item.units} x {_stock_unit.description} = {float(_item_price / 100.0)}")
    #       - compound order value to the total value
    #   - print the total order value:
    #       print(f"  --> order value is: {float(_order_value / 100.0)}\n")
    #   - return order value
    #
    for i in range(o.items_count()):
        item = o.get_item(i)
        stock = sds.find_stock_by_sku(item.get_sku())
        print(stock.get_sku())
        print(stock.get_price())
        _order_value += stock.get_price()
        print(stock.get_sku())
    
    print(f"  --> order value is: {float(_order_value / 100.0)}")
    return _order_value


def print_orders(_customer_id: int):
    """
    Print all orders of a customer and compounding their total value
    that is printed at the end.
    :param _customer_id: customer id
    """
    #
    # TODO: complete logic, consider steps
    #   - look up orders of customer in OrderStore(ods)
    #   - print number of orders found for customer
    #   - foreach order:
    #       - invoke the print_order_value(order) function to print the order
    #       - compound order value to the total value
    #   - print the total value of all orders of the customer
    #
    # _customer_orders = []  # TODO: look up orders

    if _customer_id == -1:
        print("illegal customer")
    elif cds.find_customer_by_id(_customer_id):
        _customer_orders = ods.filter(lambda o: customer_id_func(o) ==_customer_id)
        print(f"\n--> customer {_customer_id} has {len(_customer_orders)} orders")
        for o in _customer_orders:
            print_order_items(o)
    else:
        print( "no customer")
        # ...
      # TODO: compute _total_order_value
    _total_order_value = 0
    print(f"==> total order value is: {float(_total_order_value / 100.0)}")


if __name__ == "__main__":
    # print number of orders in OrderStore and CustomerStore
    print(f"{len(ods.find_all_orders())} orders in OrderStore")
    print(f"{len(cds.find_all_customers())} customers in CustomerStore")

    # find customers in data store using find functions
    _c1 = cds.find_customer_by_id(898179)
    print("customer 898179:", _c1.name if _c1 is not None else "not found")

    # find customers using filter functions on data stores
    _last_name = "Cantrell"
    print(f"--> find customers with last name '{_last_name}':")
    _filtered_by_id = cds.filter(lambda c: c.get_id() == 898179 or c.get_id() == 192794)
    _filtered_by_name = cds.filter(lambda c: last_name_func(c) == _last_name)
    # print resulting customer list using the built-in map() function
    list(map(lambda c: print(f" - {c.name}, {c.address}"), _filtered_by_id))
    list(map(lambda c: print(f" - {c.name}, {c.address}"), _filtered_by_name))

    # find order in data store by id
    print("--> find orders by id")
    _filtered_by_id = ods.filter(lambda o: o.get_id() == "00-784-33313" or o.get_id() == "00-184-40592")
    list(map(lambda o: print(f" - {o.get_id()},{o.get_customer_id()},{o.get_date()},{o.items_count()}"), _filtered_by_id))
    
    print("--> find stocks by id")
    # find stock in data store by id
    _filtered_by_id = sds.filter(lambda o: o.get_sku() == "2208C002" or o.get_sku() == "0106C002")
    list(map(lambda s: print(f" - {s.get_sku()},{s.description},{s.get_price()},{s.get_units_available()}"), _filtered_by_id))



    # print resulting customer list using the built-in map() function


    # find all orders for each customer
    print_orders(258090)    # customer 258090: 2 orders with 1 item each
    print_orders(368075)    # customer 368075: 1 order with 1 item each
    print_orders(986973)    # customer 986973: 1 order with 4 items
    print_orders(193667)    # customer 193667: 4 orders with 1 item each
    print_orders(973407)    # customer 973407: 0 orders, is customer
    print_orders(333333)    # customer 333333: 0 orders, not a customer
    print_orders(-1)        # customer -1: illegal customer id
