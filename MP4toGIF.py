import os
import subprocess
import sys

def convert_mp4_to_gif(ffmpeg_path='ffmpeg', mp4_files=None):
    if mp4_files is None:
        mp4_files = [f for f in os.listdir('.') if f.lower().endswith('.mp4')]
    if not mp4_files:
        print("No MP4 files found in the current directory.")
        return

    # Ensure 'GIF' folder exists
    gif_folder = 'GIF'
    os.makedirs(gif_folder, exist_ok=True)

    for mp4 in mp4_files:
        gif_filename = os.path.splitext(mp4)[0] + '.gif'
        gif_path = os.path.join(gif_folder, gif_filename)
        print(f'Converting "{mp4}" to "{gif_path}"...')

        # ffmpeg command to convert mp4 to gif with good quality
        # First create a color palette for better quality
        palette = "palette.png"
        palette_cmd = [
            ffmpeg_path,
            '-i', mp4,
            '-vf', 'fps=24,scale=iw/2:ih/2,palettegen=max_colors=64',
            '-y', palette
        ]

        # Convert using the palette
        gif_cmd = [
            ffmpeg_path,
            '-i', mp4,
            '-i', palette,
            '-filter_complex', 'fps=24,scale=iw/2:ih/2[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5',
            '-y',
            gif_path
        ]

        try:
            # Generate palette
            result = subprocess.run(palette_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                # Convert to GIF using the palette
                result = subprocess.run(gif_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:
                    print(f'Successfully converted {mp4} → {gif_path}')
                else:
                    print(f'Error converting {mp4} to GIF:\n{result.stderr.decode()}')
            else:
                print(f'Error generating palette for {mp4}:\n{result.stderr.decode()}')
        finally:
            # Clean up palette file
            if os.path.exists(palette):
                os.remove(palette)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if os.path.isfile(filename) and filename.lower().endswith('.mp4'):
            convert_mp4_to_gif(mp4_files=[filename])
        else:
            print(f'File "{filename}" not found or is not an MP4 file.')
    else:
        convert_mp4_to_gif()
