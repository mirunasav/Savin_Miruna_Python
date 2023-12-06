import os.path
import sys


# 1
def files_with_extension_in_directory():
    try:
        if len(sys.argv) != 3:
            raise Exception("The command should be : python main.py directory_path file_extension")
        directory = sys.argv[1]
        fileExtension = sys.argv[2]

        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        for filename in os.listdir(directory):
            if filename.endswith(fileExtension):
                file_path = os.path.join(directory, filename)
                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                        print(f"Contents of {filename}:\n{content}")
                except Exception as e:
                    print(f"Error reading {filename} : {e}")

    except FileNotFoundError as e:
        print(F"File not found error :{e}")

    except OSError as e:
        print(f"Error accessing files: {e}")
    except Exception as e:
        print(f"Exception :{e}")


# files_with_extension_in_directory()


# 2. rename all files to a sequential number prefix
def rename_files(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Directory path is invalid")

        files = os.listdir(directory)

        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(directory, filename)
            new_filename = f"file{index}.{filename.split('.')[-1]}"
            new_path = os.path.join(directory, new_filename)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed {old_path} to {new_path}")
            except Exception as e:
                print(f"Error renaming {old_path} to {new_path}")

    except FileNotFoundError as e:
        print(f"error :{e}")
    except OSError as e:
        print(f"error accesing files : {e}")


# rename_files("C:\\Users\\Miruna Savin\\PycharmProjects\\PP\\Lab6\\files to rename")

# 3. size of all files

def size_of_all_files(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("directory path is invalid")

        # or read directory from command line and use
        # directory = sys.argv[1] like I did at points 1 and 4

        size = 0

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size += os.path.getsize(file_path)
                except OSError as e:
                    print(f"error accessing files: {e}")
        print(f"total file size in directory {directory} : {size} bytes")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")


# size_of_all_files("C:\\Users\\Miruna Savin\\PycharmProjects\\PP")


# 4 number of files with a specific extension

def number_of_files_with_extension():
    try:
        if len(sys.argv) != 2:
            raise Exception("System arguments should be: path and directory path")
        directory = sys.argv[1]

        if not os.path.isdir(directory):
            raise FileNotFoundError(f"directory path is invalid")

        extension_dictionary = {}
        found_files = False

        for root, directories, files in os.walk(directory):
            for file in files:
                file_extension = file.split('.')[-1]
                extension_dictionary[file_extension] = extension_dictionary.get(file_extension, 0) + 1
                found_files = True

        if not found_files:
            raise Exception("empty directory")

        for key, value in extension_dictionary.items():
            print(f"extension :{key}; count :{value}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Exception :{e}")


number_of_files_with_extension()
