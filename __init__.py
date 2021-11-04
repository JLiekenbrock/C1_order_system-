import C1_order_system.data
import C1_order_system.datastore as ds

# public DataStore objects
cds = ds.CustomerDataStore()
sds = ds.StockDataStore()
ods = ds.OrderDataStore()

# DataFactory object instantiation without reference, invoke chainable functions
ds.DataFactory(cds, sds, ods) \
      .import_customers(data.customers) \
      .import_stock(data.stock) \
      .import_orders(data.orders)

print(f"--> {cds.size()} customers, {sds.size()} stock items, {ods.size()} "
      "orders loaded.")
