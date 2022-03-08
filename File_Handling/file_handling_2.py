# write mode, creates a file if not found
my_file = open(r"D:\2021\ELZERO\File_Handling\my_second_file.txt", "w")

# to entre input to the file
# if I used write then deleted that line and used another write, the first will be deleted

# my_file.write("Hello\n")
# my_file.write("from\n")
# my_file.write("the other side\n")


# write lines takes a list and loop over it and print it in the file
my_list = ["Hello\n", "From\n", "The other side\n", "Heeey\n"]
my_file.writelines(my_list)


# append, adds to what was written before and when you use it and then delete the append line, you will find what was appended

my_file = open(r"D:\2021\ELZERO\File_Handling\my_second_file.txt", "a")
my_file.write("okay\n")
my_file.write("okay again")
my_file.write("okay final")
my_file.write("the end\n")