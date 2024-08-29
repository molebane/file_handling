# file_handling_assignment.py

try:
    # Create a new text file named "my_file.txt" in write mode ('w') and write initial content
    with open('my_file.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is line number 2.\n")
        file.write("The number is 12345.\n")

    # Open "my_file.txt" in append mode ('a') and append three additional lines
    with open('my_file.txt', 'a') as file:
        file.write("Appending line 4.\n")
        file.write("Appending line 5.\n")
        file.write("Final number is 67890.\n")

    # Read the contents of "my_file.txt" and display them on the console
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("Contents of my_file.txt:")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have the necessary permissions to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operation completed.")
