import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pathlib

def check_files(input_folder, file_list):
    """
    Check if files listed in file_list exist within input_folder.
    """
    found_files = []
    missing_files = []
    for file_path in file_list:
        if not file_path.startswith("#"):  # Ignore lines starting with #
            file_path = file_path.replace("-vendor/", "vendor/")  # Replace -vendor/ with vendor/
            absolute_path = os.path.join(input_folder, *file_path.split('/'))
            if os.path.exists(absolute_path):
                found_files.append(absolute_path)
            else:
                missing_files.append(absolute_path)
    return found_files, missing_files

def read_file_list(file_path):
    """
    Read the list of files from the specified file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    messagebox.showinfo("Instructions", "Please choose the 'vendor' folder inside 'dumpyara', 'dumperx', or 'downloaded dump'")
    folder_path = filedialog.askdirectory(title="Select Input Folder")
    return folder_path

def main():
    input_folder = select_folder()
    if not input_folder:
        print("No folder selected. Exiting.")
        return

    home_dir = str(pathlib.Path.home())  # Get the path to the user's home directory
    file_list_path = os.path.join(home_dir, "proprietary-files.txt")  # Path to the file containing the list of files
    file_list = read_file_list(file_list_path)
    found_files, missing_files = check_files(input_folder, file_list)

    if found_files:
        print("Found the following files:")
        for file_path in found_files:
            print(file_path)
    else:
        print("No files found.")

    if missing_files:
        errorlist_file_path = os.path.join(home_dir, "errorlist.txt")
        with open(errorlist_file_path, 'w') as f:
            f.write("Files not found in input folder:\n")
            for file_path in missing_files:
                f.write(file_path + '\n')
        print(f"Error list saved to: {errorlist_file_path}")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("Error: tkinter package not found.")
        print("For Debian/Ubuntu Linux: sudo apt-get install python3-tk")
        print("For Fedora Linux: sudo dnf install python3-tkinter")
        print("For macOS: brew install python-tk")
        print("For Windows, tkinter should already be available with the Python installation.")
