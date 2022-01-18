tables = {
    1:['Jiho', False],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[],
}   

print(tables)
print("----------------------------")
#Checkpoint 2&5
def assign_table(table_number, name, vip_status = False):
    tables[table_number] = [name, vip_status]

# Checkpoint 3 
assign_table(6, 'Yoni', False)
print(tables) 
print("----------------------------")
# Checkpoint 4 
assign_table(table_number = 3 , name= 'Martha' ,vip_status=True)
print(tables)
print("----------------------------")

#Checkpoint 6 
assign_table(4, "Karla")
print(tables)
print("----------------------------")