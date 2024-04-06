# Proprietary File Checker

The Proprietary File Checker is a Python script designed to help you check if certain files listed in a `proprietary-files.txt` file exist within a specified folder. It is particularly useful when dealing with proprietary files in Android ROM development or similar contexts.

## Installation

1. Clone this repository to your local machine or download the `proprietary_file_checker.py` script.

2. Ensure you have Python 3.x installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/downloads/).

3. The script uses the Tkinter library for file dialog functionality, which is usually included with Python installations. If you encounter any issues related to Tkinter, ensure it is installed or refer to your system's package manager for installation instructions.

## Usage

1. Place the `proprietary-files.txt` file containing the list of file paths in your home directory.

2. Open a terminal or command prompt and navigate to the directory where you saved the `proprietary_file_checker.py` script.

3. Run the script by executing the following command:

python3 proprietary_file_checker.py


4. The script will prompt you to select the folder where you want to check for the existence of the files. Please ensure that you select the "vendor" folder inside either "dumpyara", "dumperx", or "downloaded dump" depending on your specific context.

5. After selecting the folder, the script will display the found files in the console. If any files listed in the `proprietary-files.txt` are not found, their paths will be saved to an `errorlist.txt` file in your home directory.

## Contributing

Contributions to this script are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute code, please feel free to open an issue or submit a pull request.

## Acknowledgements

This script utilizes the Tkinter library for GUI functionality.

## Examples

```bash
$ python3 proprietary_file_checker.py
# Script prompts for folder selection
# User selects folder containing vendor files
# Script displays found files or saves error list if files are missing

