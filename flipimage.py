import os
import subprocess
from pathlib import Path

def flip_image(image_path, direction):
    try:
        # Construct the ImageMagick command
        if direction.lower() == 'h':
            command = ['magick', image_path, '-flop', image_path]
        elif direction.lower() == 'v':
            command = ['magick', image_path, '-flip', image_path]
        else:
            print("Invalid direction. Please use 'h' for horizontal or 'v' for vertical.")
            return False
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Successfully flipped {image_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error processing image: {e}")
        return False

def main():
    # Get the image filename
    image_path = input("Enter the image filename (with extension): ").strip()
    
    # Check if file exists
    if not os.path.exists(image_path):
        print("Error: File does not exist!")
        return
    
    # Get flip direction
    direction = input("Enter flip direction (h for Horizontal, v for Vertical): ").strip()
    
    # Process the image
    flip_image(image_path, direction)

if __name__ == "__main__":
    main()