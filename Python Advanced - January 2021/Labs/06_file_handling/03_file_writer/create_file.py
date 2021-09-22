# Create a file, add a line to it
with open("my_first_file.txt", "a") as file:
    file.writelines("I just create my first file!")
