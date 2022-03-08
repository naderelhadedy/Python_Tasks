# OOP 3

# Inheritance

class Food : # Base Class

    def __init__(self, name, price) :

        self.name = name

        self.price = price

        print(f"{name} is created from Base class")

    def eat(self) :

        print("Eat method from Base class")



# Inherit from Food Class

class Apple(Food) : # Derived Class

    def __init__(self, name, price, amount) :

        # inherits from the food class with __init__ function, so he didn't want to write self.name = name
        # Food.__init__(self, name) # create instance from Base Class

        # it does the same as above line
        super().__init__(name, price)

        self.amount = amount

        print(f"{self.name} is created from Derived class and the price is {self.price} and the amount is {self.amount}")


    def get_from_tree(self) :

        print("Get from tree from derived class")

    # override a method
    def eat(self) :

        print("Eat method from Derived class")


# food_one = Food("Pizza", 1000)

# print('#' * 150)

# food_two = Apple("Mango", 150, '2 Kilos')

# print('#' * 150)

# food_two.eat() # method inherited

# print('#' * 150)

# food_two.get_from_tree() # method created




# Multiple Inheritance

class BaseOne :

    def __init__(self) :
        print("Base One")

    def func_one(self) :
        print("ONE")

class BaseTwo :

    def __init__(self) :
        print("Base Two")

    def func_two(self) :
        print("TWO")

class Derived(BaseOne, BaseTwo) :

    pass


my_var = Derived()

# multiple resolution order
# print(Derived.mro())

print(my_var.func_one)
print(my_var.func_two)

# access methods of inherited classes
my_var.func_one()
my_var.func_two()



# Multiple Inheritance in another way

class Base :

    pass

class One(Base) :

    pass

# class two is like inherting from class base and also of course class one if has another methods
class Two(One) :

    pass