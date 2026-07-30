import os
from PIL import Image

def get_supported_formats():
    # Get list of supported formats from Pillow
    supported = [fmt.lower() for fmt, desc in Image.registered_extensions().items()]
    # Remove duplicates and sort
    supported = sorted(list(set(supported)))
    # Remove the dot from extensions
    return [fmt[1:] if fmt.startswith('.') else fmt for fmt in supported]

def get_valid_format():
    formats = get_supported_formats()
    while True:
        print("\nSupported output formats:", ', '.join(formats))
        format_choice = input("Enter desired output format (e.g., png, jpg, tiff): ").lower()
        if format_choice in formats:
            return format_choice
        print(f"Invalid format. Please choose from the supported formats.")

def get_dimension(dimension_name):
    while True:
        value = input(f"Enter desired {dimension_name} (or 0 to maintain aspect ratio): ")
        try:
            value = int(value)
            if value < 0:
                print("Please enter a positive number or 0")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

def calculate_new_dimensions(img, width, height):
    original_width, original_height = img.size
    
    # If both dimensions are 0, keep original size
    if width == 0 and height == 0:
        return original_width, original_height
    
    # If one dimension is 0, calculate it to maintain aspect ratio
    if width == 0:
        aspect_ratio = original_width / original_height
        width = int(height * aspect_ratio)
    elif height == 0:
        aspect_ratio = original_height / original_width
        height = int(width * aspect_ratio)
    
    return width, height

def convert_images():
    # Get current directory
    directory = os.getcwd()
    
    # Create 'Converted' folder if it doesn't exist
    output_dir = os.path.join(directory, "Converted")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get list of image files
    image_files = [f for f in os.listdir(directory) if any(f.lower().endswith(ext) 
                  for ext in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'])]
    
    if not image_files:
        print("No image files found in the current directory!")
        return
    
    print(f"\nFound {len(image_files)} image(s) to process.")
    
    # Ask about filename format
    while True:
        include_size = input("Include size information in filenames? (Y/N): ").upper()
        if include_size in ['Y', 'N']:
            break
        print("Please enter Y or N")
    
    # Get desired output format once
    output_format = get_valid_format()
    
    # Get desired dimensions once
    print("\nEnter target dimensions for all images:")
    width = get_dimension("width")
    height = get_dimension("height")
    
    # Process all files in directory
    print("\nProcessing images...")
    for filename in image_files:
        try:
            # Open image
            with Image.open(filename) as img:
                print(f"\nProcessing: {filename}")
                print(f"Original size: {img.size}")
                
                # Calculate new dimensions maintaining aspect ratio if needed
                new_width, new_height = calculate_new_dimensions(img, width, height)
                
                # Create new filename
                base_name = os.path.splitext(filename)[0]
                if include_size == 'Y':
                    new_filename = f"{base_name}_{new_width}x{new_height}.{output_format}"
                else:
                    new_filename = f"{base_name}.{output_format}"
                
                # Add output directory to path
                output_path = os.path.join(output_dir, new_filename)
                
                # Resize and save
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                resized_img.save(output_path, format=output_format)
                print(f"Saved as: {new_filename}")
                print(f"New size: {new_width}x{new_height}")
                
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    print("Image Converter - Resize and Convert Images")
    print("==========================================")
    convert_images()
