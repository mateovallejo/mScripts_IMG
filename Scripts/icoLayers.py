import os
import subprocess
from pathlib import Path

def process_ico_files():
    # Create output directory if it doesn't exist
    output_dir = Path('processed_icons')
    output_dir.mkdir(exist_ok=True)

    # Get all .ico files in the current directory
    current_dir = Path('.')
    ico_files = list(current_dir.glob('*.ico'))

    if not ico_files:
        print("No .ico files found in the current directory.")
        return

    # Process each ico file
    for ico_file in ico_files:
        input_file = str(ico_file)
        output_file = str(output_dir / ico_file.name)
        
        print(f"Processing {input_file}...")
        
        try:
            # Run the ImageMagick command
            command = [
                'magick',
                input_file,
                '-define',
                'icon:auto-resize=16,20,24,32,40,48,64,256',
                output_file
            ]
            
            subprocess.run(command, check=True)
            print(f"Successfully processed {input_file} -> {output_file}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error processing {input_file}: {e}")
        except Exception as e:
            print(f"Unexpected error processing {input_file}: {e}")

if __name__ == '__main__':
    print("Starting ICO file processing...")
    process_ico_files()
    print("Processing complete!")