import sys
import os

def save_file(file_path, upload_directory):
    try:
        # Ensure that the upload directory exists
        if not os.path.exists(upload_directory):
            os.makedirs(upload_directory)

        # Copy the provided file to the upload directory
        with open(file_path, "rb") as source_file:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(upload_directory, file_name)
            with open(destination_path, "wb") as destination_file:
                destination_file.write(source_file.read())

        print(f"File '{file_name}' uploaded successfully to '{upload_directory}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python upload_file.py <file_path> <upload_directory>")
        sys.exit(1)

    file_path = sys.argv[1]
    upload_directory = sys.argv[2]

    save_file(file_path, upload_directory)
