#task1  
import os  
path = os.getcwd() 
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :")  
print(dir_list)

#task2
import os
def check_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    print(f"The path '{path}' exists.")
    if os.access(path, os.R_OK):
        print("The path is readable.")
    else:
        print("The path is not readable.")
    if os.access(path, os.W_OK):
        print("The path is writable.")
    else:
        print("The path is not writable.")
    if os.access(path, os.X_OK):
        print("The path is executable.")
    else:
        print("The path is not executable.")
path = os.getcwd() 
check_access(path)

#task3
import os
def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory = os.path.dirname(path)
        filename = os.path.basename(path)

        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")
path = os.getcwd() 
check_path(path)

#task4
def count_lines(file):
    with open(file, 'r') as file:
        line_count = sum(1 for line in file)
    print(f"The file '{file}' contains {line_count} lines.")
file = "demofile.txt"
count_lines(file)

#task5
def write_list_to_file(file, list):
        with open(file, 'w') as file:
            for item in list:
                file.write(f"{item}\n") 
        print(f"The list written to '{file}' successfully.")
file = "demofile.txt"
list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
write_list_to_file(file, list)

#task6
def generate_text_files():
        for letter in range(ord('A'), ord('Z') + 1):
            file_name = f"{chr(letter)}.txt"
            with open(file_name, 'w') as file:
                file.write(f"This is the file {chr(letter)}.txt\n")
        print("26 text files (A.txt to Z.txt) generated successfully in directory.")
generate_text_files()

#task7
def copy_file(source_file, destination_file):
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
source_file = "demofile.txt"
destination_file = "demofile2.txt"
copy_file(source_file, destination_file)

#task8
import os
def delete_file(file):
        if not os.path.exists(file):
            print(f"The file '{file}' does not exist.")
            return
        if not os.access(file, os.W_OK):
            print(f"You can't delete '{file}'.")
            return
        os.remove(file)
        print(f"The file '{file}' deleted.")
file = "demofile.txt"
delete_file(file)