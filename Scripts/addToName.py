import os

def add_prefix_suffix():
    # Use current directory
    directory = os.getcwd()

    # Ask whether prefix or suffix
    while True:
        mode = input("Add a Prefix or Suffix? (P/S): ").upper()
        if mode in ['P', 'S']:
            break
        print("Please enter P or S")

    # Ask for the string to add
    text = input(f"Enter the {'prefix' if mode == 'P' else 'suffix'} to add: ")

    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Skip the script file itself
    script_name = os.path.basename(__file__)
    files = [f for f in files if f != script_name]

    # Sort files to ensure consistent ordering
    files.sort()

    # Store original and new names for preview
    rename_pairs = []

    for file in files:
        base_name, ext = os.path.splitext(file)
        if mode == 'P':
            new_name = f"{text}{file}"
        else:
            new_name = f"{base_name}{text}{ext}"
        rename_pairs.append((file, new_name))

    if not rename_pairs:
        print("No files found to rename.")
        return

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
    add_prefix_suffix()
