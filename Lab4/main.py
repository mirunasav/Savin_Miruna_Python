import os

# 1. extensiile unice sortate crescator


def unique_file_extensions(directory):
    extensions = set()
    try:
        for root, directories, files in os.walk(directory):
            for fileName in files:
                extension = fileName.split('.')[-1].lower()
                extensions.add(extension)
        extensions = sorted(extensions)
        for extension in extensions:
            print(extension)
    except OSError:
        print("Directory does not exist")
        return set()


# unique_file_extensions("C:\\Users\\Miruna Savin\\OneDrive")

# 2. in fisierul de la calea fisier sa fie scris pe cate o linie calea absoluta
# a fiecarui fisier din directorul de la calea folder, de incepe cu litera A

def write_absolute_paths_to_file(directory, file):
    try:
        with open(file, 'w') as file_writer:
            file_writer.write(f"Files starting with A in the directory {directory}: \n")
            for root, directories, files in os.walk(directory):
                for fileName in files:
                    if fileName.startswith('D'):
                      full_fileName = os.path.join(root, fileName)
                      absolute_path = os.path.abspath(full_fileName)
                      file_writer.write(absolute_path + '\n')
    except OSError:
        print("could not write to the specified file")


# write_absolute_paths_to_file("C:\\Users\\Miruna Savin\\OneDrive","C:\\Users\\Miruna Savin\\OneDrive\\output.txt")


# 3. fisier: ultimele 20 de caractere; director: lista de tuple(extensie, count)
# cu toate fisierele din director

def number_of_extensions_in_directory(directoryPath):
    extensionsCount = {}
    for root, directories, files in os.walk(directoryPath):
        for fileName in files:
            extension = fileName.split('.')[-1]
            extensionsCount[extension] = extensionsCount.get(extension, 0) + 1
    sortedExtensions = sorted(extensionsCount.items(), key=lambda x: x[1], reverse=True)

    # extensionsCount.items() returns a list of tuples, each tuple = key value pair
    # key: the function used to extract a comparison key from each element of the list ( the second element)

    return sortedExtensions


def last_20_chars(filePath):
    try:
        with open(filePath, "r", encoding='utf-8') as file:
            content = file.read()
            return content[-20:]
    except OSError:
        return "could not read the file content!"


def last_20_chars_or_number_of_extensions(my_path):
    if os.path.isfile(my_path):
        return last_20_chars(my_path)

    if os.path.isdir(my_path):
        return number_of_extensions_in_directory(my_path)


print(last_20_chars_or_number_of_extensions("C:\\Users\\Miruna Savin\\OneDrive\\output.txt"))

# 4. extensions of files from the directory given as argument in the command line
def unique_file_extensions(directory):
    extensions = set()
    try:
        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        for file in files:
            base, extension = os.path.splitext # returns tuple (root , extension)
            if extension:
                extensions.add(extension[1:].lower())

        extensions = list(sorted(extensions))
        return extensions
    except OSError:
        print("unable to access the directory")
        return []


