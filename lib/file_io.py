
# The file_name can be a combined file path/name, you will need to add the .txt file extension to the file_name when opening a file for all three of the methods.

# This function should use file_name and file_content to write a .txt file.

# Write a append_file function that takes in the same parameters and appends to the .txt file.

# Write a read_file function that takes in a file name and returns the content of the .txt file.


# # use write_file function. 
# write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
# append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

# read_file(file_name="logfile")
# # Log 1: 5 bananas added
# # Log 2: 3 bananas subtracted





# def write_file(file_name, file_content):
#     pass
#     file_name += ".txt"
#     with open (file_name, mode='w', encoding='utf-8') as file_io:
#         file_io.write('file_content')

# def append_file(file_name, append_content):
#     pass
#     file_name += ".txt"
#     with open(file_name, mode='a', encoding='utf-8') as file_io:
#         file_io.write('append_content')

# def read_file(file_name):
#     pass
#     file_name += ".txt"
#     # file_io = open('file.io.txt', encoding='utf-8')
#     with open(file_name, mode='r', encoding='utf-8') as file_io:
#     print(file_io.read())

def write_file(file_name, file_content):
    """Writes content to a new .txt file (overwriting if it exists)."""
    file_path = f"{file_name}.txt"  # Add the .txt extension dynamically
    with open(file_path, mode="w", encoding="utf-8") as file_io:
        file_io.write(file_content)


def append_file(file_name, append_content):
    """Appends content to an existing .txt file."""
    file_path = f"{file_name}.txt"  # Add the .txt extension dynamically
    with open(file_path, mode="a", encoding="utf-8") as file_io:
        file_io.write(append_content)


def read_file(file_name):
    """Reads the content of a .txt file and returns it."""
    file_path = f"{file_name}.txt"  # Add the .txt extension dynamically
    with open(file_path, mode="r", encoding="utf-8") as file_io:
        return file_io.read()





