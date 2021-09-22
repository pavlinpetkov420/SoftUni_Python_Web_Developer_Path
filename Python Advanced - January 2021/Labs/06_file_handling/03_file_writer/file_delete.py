import os
# Delete a file, if it is already deleted print a special message
try:
    os.remove("my_first_file.txt")
    print("Deleted")
except FileNotFoundError:
    print("File already deleted!")

# return boolean
print(os.path.exists("my_first_file.txt"))
