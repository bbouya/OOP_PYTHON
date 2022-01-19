class Dog:
    # To create a Dog, give it a name, breed, and age. age is in years.
    
    # If you don't give an age, we ll say it's 0 years old (a puppy)
    # All doggs also start as friendly!

    def __init__(self, input_name,input_breed, input_age =0, input_friendliness = True):
        #Dog attribute
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.is_friendly = input_friendliness
        self.friend = []
    
    # Self will equal this specific dog
    # other_ dog will be an argument we pass in 
    def become_friends(self, other_dog):
        if(other_dog.is_friendly):
            # if the other dog is friendly,
            # it adds other_dog to its friends
            self.friends.append(other_dog)
            # The other dog also adds this
            # Specific dog to its friends
            other_dog.friends.append(self)
            print("{name} become friends with {other_name}!".format(name = self.name, other_name = other_dog.name))
        else:  
            # If the other dog is NOT friendly,
            # no one becomes friends.
            print("{other_name} did not want to become friends with {name}!".format(name = self.name, other_name = other_dog.name))
    
    # Self will refer to a specific dog that we create. self.age refers to that specific dog's age
    # We can create a new dog by calling out constructor. Notice, we call it by saying Dog(), not __init__
    # Exemple lets create dog_one
    def have_birthday(self):
         # Add one to this specific dog"s age
        self.age = self.age + 1
        print('{name} had a birthday! {name} is {age} years old.'.format(name = self.name,age = self.age))
        

dog_one = Dog("Sparky", "Golden Retriever", 5)
# We can also update our code to add a second Dog a 10 year old unfreienndly 'Chihuahua' named 'Bruno'
dog_one = Dog('Sparky', 'Golden Retriever',5)

# The self parameter will see that self = dog_one
dog_one.have_birthday()

# This dog will have self.is_friendly set to False by default
dog_two = Dog("Bruno",'Chuihuahua', 10, False)


# When Sparky asks Bruno, Bruno says no.
dog_one.become_friends(dog_two)