FILEPATH = "Todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_loc:
        todos_loc = file_loc.readlines()
    return todos_loc

def write_fun( todos_arg , filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
