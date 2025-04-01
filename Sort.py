import os

# Change this to your test folder path
folder_path = r"C:\Users\user\Desktop\Coding\Test files"

files = os.listdir(folder_path)
files.sort()  # To make sure they’re renamed in order

for i, filename in enumerate(files, start=1):
    file_ext = os.path.splitext(filename)[1]
    new_name = f"file_{i:03}{file_ext}"
    
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)

print("Done renaming files!")
