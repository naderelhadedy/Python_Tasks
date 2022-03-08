import os

# get current folder directory
my_dir = os.path.dirname(os.path.abspath(__file__))
my_new_dir = rf"{my_dir}"+r"\my_first_file.txt"

my_file = open(my_new_dir, "r")

# print file data object like name and mode
# print(my_file)

# print(my_file.name)
# print(my_file.mode)

# takes number of letters to read and the default is (-1) till the end
# print(my_file.read())

# read only one line and can take the number of letters to read
# print(my_file.readline())

# returns all lines in a list
# print(my_file.readlines())

# prints each line in files
for line in my_file:
    print(line)
    # to print mohamed then stops not to load all data on memory
    if line.startswith("Mo"):
        break


# for best practice, close the file
my_file.close()