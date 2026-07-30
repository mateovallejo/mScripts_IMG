import os
import subprocess

def convert_png_to_tiff(input_file):
    """Convert a PNG file to 64x64 TIFF format using ImageMagick."""
    output_file = os.path.splitext(input_file)[0] + '.tif'
    
    cmd = [
        'magick',
        input_file,
        '-resize', '64x64!',  # Resize to exactly 64x64
        '-colorspace', 'sRGB',
        '-compress', 'RLE',
        '-depth', '8',
        output_file
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f'Successfully converted {input_file} → {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'Error converting {input_file}: {e.stderr.decode()}')

def main():
    # Find all PNG files in current directory
    png_files = [f for f in os.listdir('.') if f.lower().endswith('.png')]
    
    if not png_files:
        print("No PNG files found in the current directory.")
        return
    
    print(f"Found {len(png_files)} PNG files to convert...")
    
    # Process each PNG file
    for png_file in png_files:
        convert_png_to_tiff(png_file)

if __name__ == '__main__':
    main()
