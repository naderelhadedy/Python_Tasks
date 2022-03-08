# OOP 1

# class Member:

#     def __init__(self):

#         print("A New Member Has Been Added")

    
# member_one = Member()
# member_two = Member()

# print(member_two.__class__)


class Member:

    #class attribute
    not_allowed_names = ["Hell", "Shit", "Damn"]

    users_num = 0

    # class method

    @classmethod
    def show_users_count(cls) :

        print(f"We have {cls.users_num} users in our system.")

    
    @staticmethod
    def say_hello() :

        print("Hello from static method")

    # instance methods
    def __init__(self, first_name, last_name, gender) :

        # instance attribute
        self.fname = first_name
        self.lname = last_name
        self.gender = gender

        # class attribute
        Member.users_num += 1

    def get_full_name(self) :

        if self.fname in Member.not_allowed_names:

            raise ValueError("Not Allowed Name")

        else:

            return f"{self.fname} {self.lname}"

    def name_with_title(self) :

        # print(self.get_full_name())

        if self.gender == "Male" :
            return f"Hello Mr. {self.fname}"
        
        elif self.gender == "Female" :
            return f"Hello Mrs. {self.fname}"

        else :
            return f"Hello {self.fname}"


    def get_all_info(self) :

        return f"{self.name_with_title()}, your full name is {self.get_full_name()}"

    def delete_member(self) :

        Member.users_num -= 1

        return f"User {self.fname} is deleted"


member_one = Member("Nader", "Elhadedy", "Male")

member_two = Member("Rovan", "Elhadedy", "Female")

member_three = Member("Mayada", "Elhadedy", "")


# print(member_one.fname, member_one.lname)

# print(member_one.get_full_name())

# print(member_one.name_with_title())
# print(member_two.name_with_title())
# print(member_three.name_with_title())

# print(member_one.get_all_info())

print(Member.users_num)

print(member_three.delete_member())

print(Member.users_num)


print("#"*100)

Member.show_users_count()

print("#"*100)

Member.say_hello()