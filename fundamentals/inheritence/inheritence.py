


class Parent():
    """The parent"""
    def __init__(self, first_name, last_name, eye_color):
        # print("Parent Constructor Called")
        self.first_name = first_name
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print(self.__class__) 
        print(self.__doc__) 
        print("First Name: " + self.first_name) 
        print("Last Name: " + self.last_name) 
        print("Eye Color: " + self.eye_color) 

class Child(Parent):
    """The child"""
    def __init__(self, first_name, last_name, eye_color, num_of_toys):
        # print("Child Constructor Called")
        Parent.__init__(self, first_name, last_name, eye_color)
        self.num_of_toys = num_of_toys

    def show_info(self):
        Parent.show_info(self)
        print("Toys: " + str(self.num_of_toys))


parent = Parent("Billy", "Cyrus", "blue")
child = Child("Miley", "Cyrus", "green", 5)

parent.show_info()
child.show_info()