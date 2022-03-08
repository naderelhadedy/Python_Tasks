# OOP 5


# Property Decorator

class Member :

    def __init__(self, name, age) :

        self.name = name

        self.age = age


    def say_hello(self) :

        return f"Hello {self.name}"


    @property
    def age_in_days(self) :     # property decorator

        return self.age * 365

    
one = Member("Ahmed", 25)

# print(one.name)
# print(one.age)
# print(one.say_hello())

# print(one.age_in_days())    # call like a method but without @property above , if called with @ above will get type error

# print(one.age_in_days)        # call like a property with @property above





# Abstract Base Class (ABC)


from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta) :      # Abstract Base Class

    @abstractmethod
    def has_oop(self) :     # Abstract Method

        pass            # abstract method does nothing

    @abstractmethod         # once this abstract method is created here, it should be created in each derived class
    def has_name(self) :

        pass


class Python(Programming) :

    def has_oop(self) :

        return "Yes"

    def has_name(self) :

        return "Python"


class Pascal(Programming) :

    def has_oop(self) :

        return "No"

    def has_name(self) :

        return "Pascal"


one = Python()
two = Pascal()

print(one.has_oop())
print(one.has_name())

print(two.has_oop())
print(two.has_name())