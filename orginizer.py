import os
import shutil

# Get the path of downloads folder
user_home = os.path.expanduser("~")
target_folder = os.path.join(user_home, 'Downloads')

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.rar'],
    'Code': ['.py', '.js', '.html', '.css']
}

# Loop through every file in the folder
for file_name in os.listdir(target_folder):
    # Build full path of the folder
    full_path = os.path.join(target_folder, file_name)

    # Only process if it's a file 
    if os.path.isfile(full_path):
        _, extension = os.path.splitext(file_name)
        extension = extension.lower()

    # Loop through each category and its extensions
    for category, extensions in file_types.items():
        if extension in extensions:
            # Create the destination folder path
            destination_folder = os.path.join(target_folder, category)

            # Create the folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)

            # Create the new path for the file
            new_path = os.path.join(destination_folder, file_name)

            # Move the file to the new folder
            shutil.move(full_path, new_path)

            print(f'Moved: {file_name} → {category}')
            break  # Stop checking other categories once matched