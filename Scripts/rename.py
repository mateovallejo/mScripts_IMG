import os

def rename_files():
    # Use current directory
    directory = os.getcwd()
    
    # Ask for the base name
    base_name = input("Enter the base name for files: ")
    
    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Skip the script file itself
    script_name = os.path.basename(__file__)
    files = [f for f in files if f != script_name]
    
    # Sort files to ensure consistent numbering
    files.sort()
    
    # Keep track of the number of files renamed
    count = 1
    
    # Store original and new names for preview
    rename_pairs = []
    
    # Get file extensions and prepare new names
    for file in files:
        # Get the file extension
        _, ext = os.path.splitext(file)
        # Create new name
        new_name = f"{base_name}_{count:03d}{ext}"
        rename_pairs.append((file, new_name))
        count += 1
    
    # Show preview
    print("\nPreview of renaming:")
    for old_name, new_name in rename_pairs:
        print(f"{old_name} -> {new_name}")
    
    # Ask for confirmation
    confirm = input("\nDo you want to proceed with renaming? (y/n): ").lower()
    
    if confirm == 'y':
        # Perform the renaming
        for old_name, new_name in rename_pairs:
            old_path = os.path.join(directory, old_name)
            new_path = os.path.join(directory, new_name)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {old_name}: {str(e)}")
        print("\nRenaming completed!")
    else:
        print("\nRenaming cancelled.")

if __name__ == "__main__":
    rename_files()
