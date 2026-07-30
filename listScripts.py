import os
import glob

def get_script_descriptions():
    return {
        "EXRcompress.py": "Compresses EXR image files",
        "EXRread.py": "Reads and displays EXR file information",
        "GIFtoWebp.py": "Converts GIF animations to WebP format",
        "MP4toGIF.py": "Converts MP4 videos to GIF animations",
        "MP4toWebp15.py": "Converts MP4 to WebP with 15fps",
        "MP4toWebp24.py": "Converts MP4 to WebP with 24fps",
        "Mp4Thumbnail.py": "Generates thumbnails from MP4 videos",
        "PNGtoEXR.py": "Converts PNG images to EXR format",
        "PNGtoTiff.py": "Converts PNG images to TIFF format",
        "PSDtoEXR.py": "Converts Photoshop PSD files to EXR format",
        "flipimage.py": "Flips/mirrors images horizontally or vertically",
        "icoLayers.py": "Handles icon layers and conversions",
        "imgConvert.py": "General-purpose image format converter",
        "listScripts.py": "Lists all Python scripts with descriptions",
        "rename.py": "Renames a single file",
        "renameFiles.py": "Batch renames multiple files",
        "toTiff.py": "Converts various image formats to TIFF",
        "toWeb.py": "Optimizes images for web usage"
    }

def list_scripts():
    print("\n=== Available Python Scripts ===\n")
    
    # Get all .py files
    python_files = glob.glob("*.py")
    descriptions = get_script_descriptions()
    
    if python_files:
        max_length = max(len(file) for file in python_files)
        for file in sorted(python_files):
            description = descriptions.get(file, "No description available")
            print(f"• {file:<{max_length}} - {description}")
        print()

if __name__ == "__main__":
    list_scripts()
