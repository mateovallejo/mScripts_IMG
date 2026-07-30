# mScripts_IMG

A collection of Windows batch and Python scripts for image and video conversion, montage creation, EXR handling, and related utilities.

## Project layout

The main scripts now live in the Scripts folder to keep the project easier to manage:

- Scripts/ contains the batch files and Python scripts
- install.bat adds the Scripts folder to your user PATH so the scripts can be launched from anywhere

## Installation

Run the installer once from the project root:

```bat
install.bat
```

This updates your user PATH so commands such as `createMontage.bat` can be run from any terminal after opening a new session.

## Dependencies

This project relies on both Python packages and external system tools.

### Python packages

Install the Python dependencies with:

```bat
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

Required Python packages:
- OpenEXR
- Imath
- numpy
- Pillow
- OpenImageIO

### External tools

These scripts also require the following executables to be installed and available on your PATH:
- ImageMagick (`magick`)
- FFmpeg (`ffmpeg`)

### Windows install suggestions

If you are on Windows, the easiest way is usually:

```bat
winget install --id Gyan.dev.FFmpeg -e
winget install --id ImageMagick.ImageMagick -e
```

If you prefer manual installation, make sure the `bin` folders for FFmpeg and ImageMagick are added to your system PATH.

## Notes

- Some scripts expect to be run from the folder containing the source files.
- For EXR and PSD workflows, OpenEXR and OpenImageIO are the key dependencies.
- For GIF/WebP/MP4 conversion, FFmpeg is required.
- For montage, resizing, and image conversion tasks, ImageMagick is required.
