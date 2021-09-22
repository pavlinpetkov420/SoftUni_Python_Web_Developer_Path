import os


def create_file(file_name):
    try:
        with open(file_name, 'x') as file:
            file.write("")
    except FileExistsError:
        with open(file_name, 'w') as file:
            file.write("")


def add_data_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content + "\n")


def replace_data(file_name, old_data, new_data):
    try:
        with open(file_name, "r+") as file:
            lines = file.readlines()
            for line in lines:
                if line == old_data:
                    line.replace(old_data, new_data)
                    file.writelines(line)
    except Exception:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.path.exists(file_name)
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


mapper = {
    "Create": create_file,
    "Add": add_data_to_file,
    "Replace": replace_data,
    "Delete": delete_file
}


def cmd_processing():
    while True:
        cmd_data = input().split('-')
        if cmd_data[0] == "End":
            break
        command, command_args = cmd_data[0], cmd_data[1:]
        mapper[command](*command_args)


cmd_processing()
