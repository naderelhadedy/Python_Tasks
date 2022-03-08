# OOP 2

# magic methods

class Skill :

    def __init__(self) :

        self.skills = ["Html", "Css", "Js"]

    def __str__(self) :

        return f"This is my skills {self.skills}"

    def __len__(self) :

        return len(self.skills)


profile = Skill()

print(profile)

print(len(profile))


profile.skills.append("PHP")

profile.skills.append("MySQL")

print(profile)

print(len(profile))


# print(profile.__class__)

# my_string = "Hamada"

# print(my_string.__class__)

# print all methods and magic methods in the class
# print(dir(str))

# print(str.upper(my_string))