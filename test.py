import os
import zipfile
import rarfile
import subprocess
import shutil

# Define the current directory (same as the script)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define paths
cars_folder = os.path.join(current_directory, "car")
dlcpacks_folder = r"C:\Program Files\Epic Games\GTAV\update\x64\dlcpacks"
dlc_generator = os.path.join(current_directory, "DLCList Generator.exe")

# Step 1: Unzip all .zip and .rar files from the car folder to a temporary folder
def unzip_files(source_directory, temp_extract_directory):
    if not os.path.exists(temp_extract_directory):
        os.makedirs(temp_extract_directory)

    for item in os.listdir(source_directory):
        file_path = os.path.join(source_directory, item)
        if item.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(temp_extract_directory)
            print(f"Extracted {file_path} to {temp_extract_directory}")
        elif item.endswith('.rar'):
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                rar_ref.extractall(temp_extract_directory)
            print(f"Extracted {file_path} to {temp_extract_directory}")

# Step 2: Search each folder for dlc.rpf and move the containing folder
def find_and_move_dlc_folders(source_directory, destination_directory):
    for root, dirs, files in os.walk(source_directory):
        # If dlc.rpf is found in current directory, move the parent folder
        if 'dlc.rpf' in files:
            # The folder containing the dlc.rpf file
            parent_folder = os.path.basename(root)
            destination_path = os.path.join(destination_directory, parent_folder)
            
            if not os.path.exists(destination_path):
                shutil.move(root, destination_path)
                print(f"Moved {root} to {destination_path}")
            else:
                print(f"{destination_path} already exists, skipping.")

# Step 3: Run the DLCList Generator.exe
def run_dlc_generator():
    try:
        subprocess.run([dlc_generator], check=True)
        print(f"Successfully ran {dlc_generator}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {dlc_generator}: {e}")

# Step 4: Prompt to delete all files in the car folder
def delete_all_files(directory):
    confirm = input(f"Do you want to delete all files in {directory}? (y/n): ").lower()
    if confirm == 'y':
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(f"All files in {directory} have been deleted.")
    else:
        print("Deletion cancelled.")

# Main function to execute the steps
def main():
    temp_extract_directory = os.path.join(current_directory, "temp_extract")

    # Step 1: Unzip files to a temporary directory
    unzip_files(cars_folder, temp_extract_directory)
    
    # Step 2: Find and move the folders containing dlc.rpf
    find_and_move_dlc_folders(temp_extract_directory, dlcpacks_folder)
    
    # Step 3: Run DLCList Generator
    run_dlc_generator()
    
    # Step 4: Delete all files in the car folder
    delete_all_files(cars_folder)

    # Cleanup temporary extract directory
    shutil.rmtree(temp_extract_directory)

if __name__ == "__main__":
    main()
