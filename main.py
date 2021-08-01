import os
from shutil import copy2, SameFileError


def main():
    req_path = input("Enter path: ")
    if os.path.exists(req_path):
        if not req_path.endswith("\\"):
            req_path = req_path + "\\"

        folder_name = input("Choose folder name: ")

        os.mkdir(req_path + folder_name)

        for root, dirs, files in os.walk(req_path):
            for file in files:
                if file.endswith('.cpp'):
                    print(file)
                    dest = req_path + "\\{0}".format(folder_name)
                    src = root + "\\" + file

                    print(src)
                    print(dest)

                    try:
                        copy2(src, dest)
                    except SameFileError:
                        print("File with same name found")
    else:
        print("Incorrect path")


if __name__ == '__main__':
    main()
