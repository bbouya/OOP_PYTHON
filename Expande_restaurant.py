"""
    we want to expand our restaurant application$
    to also take orders from cutomers.
    this is the perfect titme to use the unpacking operator
    since we never know how many items customers are going to order
    To start we want to build a function that will compile a list of all the items  
    a customer wants to order and then print it out. This will help our kitchen to know what to cook
    
    
"""
# Checkpoint 1
def print_order(*order_items):
    print(order_items)

# Checkpoint 2
print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs','Pancakes')

"""[Working with *args]
    we wanted to build a function that works similarly to our trusty print()
    statement but instrad prints all of the arguments in uppercase form. Using 
    our knowledge of iteration, combined with the power of the unpacking operator,
    our solution might look like this:
    
"""
def shout_strings(*args):
    for argument in args :
        print(argument.upper())
        
        
# Test our function
shout_strings('working on', 'learning', 'arguement unpacking!')


"""
our originaly design did not account for storing orders for each 
specific table. so we need to adjust our application to be able to store 
the orderes that come in for each specific table and also be able to print
out the order for the kitchen staff

"""

tables = {
    1:{'name':'Jiho', 'vip_status':False,'order': 'Orange Juisce, Apple Juice'},
    2:{},
    3:{},
    4:{},
    5:{},
    6:{},
    7:{},
}
print('--------------------------')
print(tables)

def assign_table(table_number, name, vip_status= False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status 
    tables[table_number]['order'] = ''
    
# Checkpoint 2 
def assign_and_print_order(table_number, *order_items):
   # Checkpoint 3
  tables[table_number]['order'] = order_items
  # Checkpoint 4
  for order_item in order_items:
    print(order_item)