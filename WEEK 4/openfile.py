def modify_text(text):
    """Example modification: convert text to uppercase"""
    return text.upper()

def main():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content
        modified_content = modify_text(content)

        # Write to a new file (output.txt)
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print(f"File '{filename}' has been read and modified successfully.")
        print("Modified content saved to 'output.txt'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()