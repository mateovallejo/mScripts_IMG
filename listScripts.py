import os

def get_command_descriptions():
    return {
        "createMontage": "Creates a grid montage from all PNGs in the folder",
        "EXRcompress":   "Compresses EXR files (DWAA, float16 half precision)",
        "EXRread":       "Prints EXR header metadata (compression, data window, etc.)",
        "flipimage":     "Flips/mirrors an image horizontally or vertically",
        "GIFtoWebp":     "Converts GIF animations to WebP format",
        "icoLayers":     "Rebuilds .ico files with multi-resolution layers (16-256px)",
        "imgConvert":    "General-purpose image resize/format converter (interactive)",
        "listScripts":   "Lists all available scripts with descriptions (this command)",
        "Mp4Thumbnail":  "Extracts a JPEG thumbnail frame from MP4 videos",
        "MP4toGIF":      "Converts MP4 videos to GIF (with palette optimization)",
        "MP4toWebp15":   "Converts MP4 to animated WebP at 15fps",
        "MP4toWebp24":   "Converts MP4 to animated WebP at 24fps",
        "NewProject":    "Creates a standard client/project folder structure",
        "PNGtoEXR":      "Converts PNG images to DWAA-compressed half-float EXR",
        "PNGtoTiff":     "Converts PNGs to 64x64 TIFF",
        "PSDtoEXR":      "Converts a Photoshop PSD file to EXR (16-bit half float)",
        "rename":        "Interactively batch-renames all files in a folder",
        "SEQtoGIF":      "Converts an EXR/image sequence into an animated GIF",
        "toTiff":        "Converts PNGs to 64x64 TIFF (Cinema 4D-style metadata)",
        "toWeb":         "Batch-converts images to web-ready JPG and noise-dithered WebP",
        # Present but currently empty / unimplemented — listed so they're not forgotten
        "MP4toWebp":     "(empty placeholder — not yet implemented)",
        "renameFiles":   "(empty placeholder — not yet implemented)",
    }

def list_scripts():
    # Always look in the folder this script lives in, not the caller's cwd,
    # so the command works no matter where you run it from.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bat_files = sorted(
        f[:-4] for f in os.listdir(script_dir)
        if f.lower().endswith('.bat')
    )

    descriptions = get_command_descriptions()

    print("\n=== mScriptsIMG — Available Commands ===\n")

    if not bat_files:
        print("No .bat commands found in", script_dir)
        return

    max_length = max(len(name) for name in bat_files)
    for name in bat_files:
        desc = descriptions.get(name, "No description available")
        print(f"  {name:<{max_length}}  -  {desc}")

    print("\nRun any command above by typing its name in CMD (from any folder,")
    print("as long as this scripts folder is on your PATH).\n")

if __name__ == "__main__":
    list_scripts()
