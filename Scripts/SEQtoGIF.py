# ...existing code...
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

# Extensions to include (add or remove as needed)

# Extensions to include (add or remove as needed)
image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')
exr_extension = '.exr'

# Step 1: Convert EXR files from ACEScg to sRGB using oiiotool
exr_files = sorted([f for f in os.listdir('.') if f.lower().endswith(exr_extension)])
png_files = []


# Parallel EXR to PNG conversion function
def convert_exr_to_png(exr_file):
    png_file = exr_file.rsplit('.', 1)[0] + '_srgb.png'
    cmd = [
        'oiiotool',
        '--colorconvert', 'ACEScg', 'sRGB',
        '-d', 'uint8',
        exr_file,
        '-o', png_file
    ]
    try:
        subprocess.run(cmd, check=True)
        return png_file
    except subprocess.CalledProcessError as e:
        return None

# Use ThreadPoolExecutor for parallel conversion
png_files = []
if exr_files:
    with ThreadPoolExecutor() as executor:
        future_to_exr = {executor.submit(convert_exr_to_png, exr): exr for exr in exr_files}
        for future in as_completed(future_to_exr):
            result = future.result()
            if result:
                png_files.append(result)

# Step 2: Collect all image files (including converted PNGs and other supported formats)
other_images = sorted([f for f in os.listdir('.') if f.lower().endswith(image_extensions)])
image_files = png_files + [f for f in other_images if f not in png_files]

if not image_files:
    print("No image files found in the current directory.")
    exit(1)


# Output GIF filename based on sequence pattern
import re
if exr_files:
    # Remove extension
    base = exr_files[0].rsplit('.', 1)[0]
    # Remove _#### at the end
    output_base = re.sub(r'_[0-9]+$', '', base)
    output_gif = f'{output_base}.gif'
else:
    output_gif = 'output.gif'



# Build the ImageMagick command
# -delay 4 sets the delay between frames (4 = ~24 fps)
# -resize 50% scales images to half size
# -loop 0 makes the GIF loop forever
cmd = ['magick', '-delay', '4.17', '-loop', '0'] + image_files + ['-resize', '50%', '-coalesce', '-dispose', 'previous', output_gif]



# Print a summary of the processed sequence
def print_sequence_summary(files, action="Processed sequence"):
    if not files:
        return
    match = re.match(r'(.*)_([0-9]+)\.[^.]+$', files[0])
    if match:
        base = match.group(1)
        first_frame = match.group(2)
        match_last = re.match(r'.*_([0-9]+)\.[^.]+$', files[-1])
        last_frame = match_last.group(1) if match_last else first_frame
        print(f"{action}: {base}_({first_frame}-{last_frame}) [{len(files)} files]")
    else:
        print(f"{action}: {len(files)} images")

if png_files:
    print_sequence_summary(png_files, action="Converted EXR to PNG")
print_sequence_summary(image_files)
print("Running command for GIF creation.")


try:
    subprocess.run(cmd, check=True)
    print(f"GIF created successfully: {output_gif}")
    # Cleanup: delete temporary PNG files
    if png_files:
        deleted = 0
        for png_file in png_files:
            try:
                os.remove(png_file)
                deleted += 1
            except Exception:
                pass
        print_sequence_summary(png_files, action="Deleted temporary PNG files")
except subprocess.CalledProcessError as e:
    print("Error creating GIF:", e)