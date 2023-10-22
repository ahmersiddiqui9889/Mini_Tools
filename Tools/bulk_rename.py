import os

# Function to rename multiple files
def main():
    i = 0
    directory_path = r"specify path"  # specify the path
    for filename in os.listdir(directory_path):
        if filename.endswith(".mp4"):  # specify the extension
            new_filename = f"new_{i}.mp4"  # create a new filename with the desired pattern
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))  # rename the file
            i += 1

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
