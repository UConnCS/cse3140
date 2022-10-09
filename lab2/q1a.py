import os

if __name__ == '__main__':
    for file in os.listdir("."):
        if os.path.isfile(os.path.join(".", file)):
            print(file)