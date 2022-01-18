def update_order(new_item, current_order =[]):
    current_order.append(new_item)
    return current_order

# First Order, Burger
order1 = update_order({'item':'burger','cost':'3.50'})

# Second ordern just a soda
order2 = update_order({'item':'soda','cost':'1.50'})


# Whats in var order2 afer the operation
print(order2)

"""
To understand this, we must first establish what python classifies as mutable. A mutable object refers to various containers in python
that are intended to be changed. A list for exemple has append and remove operations that change the elements of the list. sets and dictionaris
are also two other mutable objects in pytho as they can be changed on the fly.
"""
def createStudent(name, age , grades= None ):
    if grades in None:
        grades = []
    return {
        'name': name,
        'age': age,
        'grades': grades
    } 

def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

addGrade(chrisley, 90)
addGrade(dallas, 100)
