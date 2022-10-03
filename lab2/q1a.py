import os

if __name__ == '__main__':
    # List all files in the directory
    for file in os.listdir("."):
        # Check if the file is not a directory
        if os.path.isfile(os.path.join(".", file)):
            print(file)