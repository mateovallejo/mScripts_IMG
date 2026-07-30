import subprocess
import glob

# Get all PNG files in current directory
png_files = sorted(glob.glob("*.png"))

if not png_files:
    print("No PNG files found in current directory.")
else:
    # Run ImageMagick montage
    subprocess.run([
        "magick", "montage",
        *png_files,          # unpack all files
        "-tile", "x4",       # 4 images per row (adjust as needed)
        "-geometry", "+2+2", # spacing between images
        "montage_grid.png"   # output file
    ])

    print("✅ Montage created: montage_grid.png")
