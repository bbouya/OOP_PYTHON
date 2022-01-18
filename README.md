# OOP_PYTHON

In python 3, we ll learn how to leverage Pythons unique feature and technique tobuild powerful,
sophisticated applications. you ll also learn how to expedite your data processing and management,
manage our resources, test our code using the Unittest testing framework,
	* Functions Deep Dive
	* OOP_PYTHON
	* Iterators & Generators
	* Resource Management
	* Unit Testing

When writing function with default arguments, it can smoetimes be tempting to include an empty list as default argument to that function.

EXE: 
	def createStudent(name, age, grades = []):
		return(
			'name': name,
			'age' : age,
			'grade' : grades
			)
			
We can create two students based off this code 
	chrisley = createStudent('Chrisley', 15)
	dallas = creaeStudent('Dallas', 16)
	
Both Chrisley and dallas progress in school,
there shoud be a way for us to add new grades. Something like this method:

def addGrade(student, grade):
	student['grades'].append(grade)
	print(student['grades'])

