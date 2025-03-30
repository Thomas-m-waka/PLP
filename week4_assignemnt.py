def read_and_write_file():
    try:
        # Ask the user for the filename
        input_filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(input_filename, "r") as file:
            content = file.read()

        # Modify content (Example: Convert to uppercase)
        modified_content = content.upper()

        # Define output filename
        output_filename = "modified_" + input_filename

        # Write modified content to a new file
        with open(output_filename, "w") as file:
            file.write(modified_content)

        print(f"✅ File successfully read and modified! New file saved as: {output_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Unable to read/write the file. Check permissions or file format.")

# Run the function
read_and_write_file()
def read_and_write_file():
    try:
        # Ask the user for the filename
        input_filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(input_filename, "r") as file:
            content = file.read()

        # Modify content (Example: Convert to uppercase)
        modified_content = content.upper()

        # Define output filename
        output_filename = "modified_" + input_filename

        # Write modified content to a new file
        with open(output_filename, "w") as file:
            file.write(modified_content)

        print(f"File successfully read and modified! New file saved as: {output_filename}")

    except FileNotFoundError:
        print(" Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print(" Error: Unable to read/write the file. Check permissions or file format.")

# Run the function
read_and_write_file()
