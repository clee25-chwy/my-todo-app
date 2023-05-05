FILEPATH = 'todos.txt'
def get_todos(filepath = FILEPATH):
    """
    Read a text file and return list of to-do items
    :param filepath: path to the file, , default: todos.txt
    :return: list of items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH ):
    """
    Write the to-do items list in the text file.
    :param filepath: path to the file, default: todos.txt
    :param todos_arg: list of todos
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)




































