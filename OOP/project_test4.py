# OOP 4

# Polymorphism

class A :

    def do_something(self) :
        
        print("From Class A")

        # this method must be implemented in the derived class which inherits from this class
        raise NotImplementedError("Derived Class Must Implement This Method")

class B(A) :

    def do_something(self) :
        
        print("From Class B")

class C(A) :

    def do_something(self) :
        
        print("From Class C")

# my_instance = C()

# my_instance.do_something()






# Encapsulation


# class Member :

#     def __init__(self, name) :

#         self.name = name    # public

# one = Member("Ahmed")

# print(one.name)

# one.name = "Nader"

# print(one.name)




# class Member :

#     def __init__(self, name) :

#         self._name = name    # protected

# one = Member("Ahmed")

# print(one._name)

# one._name = "Nader"

# print(one._name)




# class Member :

#     def __init__(self, name) :

#         self.__name = name    # private

#     def say_hello(self) :   # this method is encapsulated inside the class so it has access to the private attribute

#         return f"Hello {self.__name}"

# one = Member("Ahmed")

# print(one.__name)  # prints an error

# print(one._Member__name)  # this will print the value

# print(one.say_hello())



# Getters and Setters

class Member :

    def __init__(self, name) :

        self.__name = name    # private

    def say_hello(self) :

        return f"Hello {self.__name}"

    def get_name(self) :    # Getter

        return self.__name

    def set_name(self, new_name) :     # Setter

        self.__name = new_name


one = Member("Ahmed")

print(one.get_name())

one.set_name("Anas")

print(one.get_name())