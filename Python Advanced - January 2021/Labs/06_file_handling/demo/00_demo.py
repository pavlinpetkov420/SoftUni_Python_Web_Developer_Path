"""
modes
w - deletes everything and start writing new info
a - opens file goes to the end and start writing
r - reading the information
x - creating a new file and open it for writing
t - text mode default
b - binary mode
+ - open a disk file for updating(reading and writing)
open by default is at read mode
if we don't choose the full path and search only
by name, it will search it at the current directory
../ - relative path
absolute path - full path to the file (If we write on Windows, the path will not working on Linux server)
"""

# file = open("test_text.txt")
# file1 = open("relative_path_dir/some_other_demo_file.txt")
# file2 = open("demo_dir/new_demo_file.txt")
# file.close()
# file1.close()
# file2.close()

"""
This is a context manager opening,
use the needed stuff and close the file
"""
# with open("test_text.txt", "r") as file3:
#     print(file3.readlines())

with open("test_text.txt", 'r') as file4:
    # readline - read only the 1st line
    print(file4.readline())
    # takes the first 3 bytes of first line
    print(file4.readline(3))

