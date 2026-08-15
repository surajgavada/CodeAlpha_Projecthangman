import os
import shutil

source_folder = r"B:\movies\New folder"
destination_folder = r"B:\New folder\hii"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):

    if file.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")

print("All .jpg files have been moved successfully!")