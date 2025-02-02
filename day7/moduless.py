#module-file containing python definitions and statements
#group of variables,methods,functions and classes they are executed only the first time the module is encountered in an import statement.
#types of models---user defined.built-in-ex:array,numpy,pandas,dis.
#where modules are used---database,calculation,,searching
import customers,orders,order_item
print("************************************")

customer1 = customers.Customer(1, "John", "Doe", "123-456-7890", "john.doe@example.com", "123 Main St", "New York", "NY", "10001")
customer1.display_info()
print("***********************************")

order1 = orders.Order(101, 1, "Shipped", "2023-10-01", "2023-10-05", "2023-10-03", 1, 1)
order1.display_info()
print("*************************************")

order_item1 = order_item.OrderItems(101, 1, 1001, 1, 499.99, 0.1)
order_item1.display_info()

#we can give alias_name for function_name
#from cal import add as s
#separation of concerns
#ddd=domain driven development approach 