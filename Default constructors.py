 #for default constructor
class GeekforGeeks:

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()

#Advantages of using constructors in Python:
#Initialization of objects: Constructors are used to initialize the objects of a class. They allow you to set default values for attributes or properties, and also allow you to initialize the object with custom data.
#Easy to implement: Constructors are easy to implement in Python, and can be defined using the __init__() method.
#Better readability: Constructors improve the readability of the code by making it clear what values are being initialized and how they are being initialized.
#Encapsulation: Constructors can be used to enforce encapsulation, by ensuring that the object’s attributes are initialized correctly and in a controlled manner.
#Disadvantages of using constructors in Python:
#Overloading not supported: Unlike other object-oriented languages, Python does not support method overloading. This means that you cannot have multiple constructors with different parameters in a single class.
#Limited functionality: Constructors in Python are limited in their functionality compared to constructors in other programming languages. For example, Python does not have constructors with access modifiers like public, private or protected.
#Constructors may be unnecessary: In some cases, constructors may not be necessary, as the default values of attributes may be sufficient. In these cases, using a constructor may add unnecessary complexity to the code.
