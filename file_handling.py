# File Handling - allows us to read and write to txt files with python
# 'r'  - reading files - grab information from a txt file
# 'w' - writing to files - creats information in a txt file - this will also replace whatever is already there
# 'a' -0 appending to files - add information to a txt file
# r+ w+ a+ - lets us read and write to a file

# Pathing - Absolute Path & Relative Path
# Relative Path - path from your current location <- USE THIS ONE - same for all computers
# Absolute Path - path from your hardrive -<- Specific to YOUR computer and will not work on others


# relative path to documents "documents\file.py"
# absolute path
# PC
# escaping the backslash with a backslash
# absolute_path = "C:\\Users\\YourUsername\\Documents\\file.txt"
# print(absolute_path)
# "C:\\Users\\YourUsername\\Documents\\file.txt"
# MAC
# absolute_path = "C:/Users/YourUsername/Documents/file.txt"

# If the file isn't already created - I can create a file use "w"
file = open("my_garden.txt", "w")
# do stuff with the file
# close the file here so that i dont unintentionally alter the data
file.close()# <closes file
# veryify if the file has been closed
print(file.closed)

# attemping to open a file for reading that doesnt exist
# we get an error FileNotFoundError
# file = open("swamp.txt", "r")

# using a context manager to open files
# opening the file                  names the file - file = open("my_garden.txt", "r")
with open("my_garden.txt", "r") as file:
    pass
    # read the file, do some stuff
# the file is automatically closed

# opening two files at the same time with a context manager
# as applies an alias to the opened file
with open("my_garden.txt", "r") as file1, open("my_swamp.txt", "w") as file2:
    pass
    # read the file1 and do some stuff with teh data
    # write to file2 and add txt to the file
# automatically closes the file

# "w" writing to a file with file.write("text to add to the file")
with open("my_garden.txt", "w") as file:
    # adding text to the file(writing)
    file.write("Today, I planted new sunflowers")

# writing will overwrite any current text
# with open("my_garden.txt", "w") as file:
#     # adding text to the file(writing)
#     file.write("Gardening is fun")

# "a" - add to a file without overwriting 
# its going to wherever the cursor left off in the text file  
with open("my_garden.txt", "a") as file:
    # append where the text left off
    # \n - newline to jump us down a line in the text file and write the following
    file.write("\nWater the sunflowers daily")

# adding a date to a text file
from datetime import date
with open("my_garden.txt", "a") as file:
    #               uses the datetime module to get a date string for todays date
    file.write(f"\n{date.today()}: Pruned the rose bushes")

# reading and formatting text files
with open("my_garden.txt", "r") as file:
    for line in file:
        
        print(line.strip()) #.strip() to remove the new line white space

# saving all the lines in a file to variable
with open("my_garden.txt", "r") as file:
    
    content = file.read() #also takes an argument for how much of the file to read
    # default argument is -1 which reads the whole file
    print(type(content))
    print(content)

# membership checks within lines of txt files
with open("my_garden.txt", "r") as file:
    for line in file:
        if "sunflowers" in line:
            print(line.strip())
        else:
            print("Theres no sunflowers in this line")


# Data structures with file handling
# we can take information from python data structures and add them
# to our files
# we can also take data from a file and add it to python data structures
flowers = ["Sunflower", "Rose", "Lavender"]
with open("my_garden_flowers.txt", "w") as file:
    for flower in flowers:
        file.write(flower + "\n")

# taking flowers from our txt file and add them to a list
flowers = []
with open("my_garden_flowers.txt", "r") as file:
    for line in file:
        flowers.append(line.strip()) #removing the new line character
print(flowers)
# for flower in flowers:
#     print(flower)

# taking info from dictionaries
garden_care = {"Sunflower": "full sun", "Rose": "prune regularly", "Lavender": "well-drained soil"}
with open("my_garden_care.txt", "w") as file:
    for plant, care in garden_care.items():
        file.write(f"{plant}: {care}\n")

# taking data from a txt file and adding it to our dictionary
garden_care = {}
with open("my_garden_care.txt", "r") as file:
    for line in file:
        print(line.strip().split(": "))
        plant, care = line.strip().split(": ")
        garden_care[plant] = care
print(garden_care)

# reading a file that doesn't exist, throws an error
# using exception handling to ensure that the file exists
try:
    with open("test.txt", "r") as file:
        for line in file:
            print(line.strip())
except: #FileNotFoundError
    print("That file does not exist")

# other errors you may encounter with file handling 
# PermissionError - we dont have permission to work with the file
# IOError - issue reading or writing to the file
# trying to write to a file that is read only
try:
    with open("my_garden.txt", "r") as file:
        file.write("hello")        
except Exception as e: #FileNotFoundError
    print(f"{e}")


# file handling methods
# .tell() - tell us our current position in the file
with open("my_garden.txt", "r") as file:
    file.read(32) #reads the first 32 characters
    position = file.tell() #tell the current position in the file
    print(position)


# Sequential Reading
with open("my_garden.txt", "r") as file:
    first_part = file.read(7)
    position = file.tell() # tells current position
    print(f"We are at position: {position}")
    second_part = file.read(25)
    position = file.tell() # tells current position
    print(f"We are at position: {position}")
    print("First part:", first_part)
    print("Second Part:", second_part)
   
# using seek to find a position within the txt file
with open("my_garden.txt", "r") as file:
    file.seek(33)
    line = file.readline() # read the line our cursor is on
    # readline(byte) - how much of that line are we reading
    print(f"This is the line i'm currently on: {line}")

# using seek to go a position that doesnt exist
with open("my_garden_flowers.txt", "r+") as file:
    file.seek(100)
    file.write("a new flower")

# using regex to search for patterns within a text file
import re
with open("my_garden_care.txt", "r") as file:
    content = file.read()
    matches = re.findall(r"Rose", content)
    print(f"Occurrences of Rose", matches)

# finding all flowers within the garden
with open("my_garden_care.txt", "r") as file:
    content = file.read()
    pattern = re.compile(r"([A-Z][a-z]+):") #pattern to match the format of our Flowers
    matches = re.findall(pattern, content)
    print(f"Behold! My flowers: {matches}")


# using the python OS modules - operating system
import os # gives python access to functionality that works with our folder structure
# and any general pathing, operating system stuff
# os.environ - mapping values of variables in .env file and applying to an app's configuration - configuration variables
# virtual environment - folder that exists within your project that holds all necessary dependencies for that project - actual installs for the project

# using the os module to create a folder
# mkdir to create a folder in teh current directory
os.makedirs("my_garden_files", exist_ok=True) #exist_ok=True prevents an error from being thrown if the folder already exists

# creating a relative path to create a folder within the newly created folder
# os.makedirs("my_garden_files\\test", exist_ok=True)

# change folder location of files with os
# file = "my_garden.txt"
# # create the path from a file to a location
# new_path = os.path.join("my_garden_files", file)
# # relocated the file to its new path
# os.rename(file, new_path)

print(os.listdir())

# google how to list only files in a directory with the os module in python
# is there a way to specify a type of file
def move_files():
    for file in os.listdir():
        if os.path.isfile(file): #so checking if each item in our current directory is a file
            # print(type(file))
            # checking for the .py extension
            if file[-1] == "t":
                new_path = os.path.join("my_garden_files", file)
                os.rename(file, new_path)


# move_files()
