# file_handling_assignment.py

def create_file():
    """Creates a new file and writes initial content."""
    try:
        # Open the file in write mode ('w'). This will create the file if it doesn't exist.
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 12345\n")
            file.write("Finally, the third line with a mix: Hello, World! 6789\n")
        print("File created and initial content written.")
    except PermissionError:
        print("Error: Permission denied when trying to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_file():
    """Reads and displays the contents of the file."""
    try:
        # Open the file in read mode ('r').
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print("Contents of the file:")
            print(contents)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file():
    """Appends additional lines of text to the file."""
    try:
        # Open the file in append mode ('a').
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line with text.\n")
            file.write("Adding another line with number: 98765\n")
            file.write("And a final line with text: Goodbye, World!\n")
        print("Additional content appended to the file.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the script tasks."""
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read file again to show appended content

if __name__ == "__main__":
    main()

