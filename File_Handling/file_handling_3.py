# my_file = open(r"D:\2021\ELZERO\File_Handling\my_third_file.txt", "w")
# my_file.write("Hello\n")
# my_file.write("baby\n")

# truncate method, lets only the number of letters it takes and trash the remaining
# my_file = open(r"D:\2021\ELZERO\File_Handling\my_third_file.txt", "a")
# my_file.truncate(5)

# tell method says where the position of the cursor
# my_file = open(r"D:\2021\ELZERO\File_Handling\my_third_file.txt", "a")
# print(my_file.tell())


# seek method shifts the position of cursor to start reading from
# my_file = open(r"D:\2021\ELZERO\File_Handling\my_third_file.txt", "r")
# # put the cursor after five letters
# my_file.seek(6)

# print(my_file.read())


# import libraries to delete files
# create a file first
# my_file = open(r"D:\2021\ELZERO\File_Handling\my_fourth_file.txt", "w")
# then delete the file
import os
os.remove(r"D:\2021\ELZERO\File_Handling\my_fourth_file.txt")