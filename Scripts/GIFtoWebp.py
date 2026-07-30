import os
import subprocess

def convert_gif_to_webp(ffmpeg_path='ffmpeg'):
    # List all .gif files in current directory
    gifs = [f for f in os.listdir('.') if f.lower().endswith('.gif')]
    if not gifs:
        print("No GIF files found in the current directory.")
        return
    
    for gif in gifs:
        webp = os.path.splitext(gif)[0] + '.webp'
        print(f'Converting "{gif}" to "{webp}"...')
        
        # Build ffmpeg command
        cmd = [
            ffmpeg_path,
            '-i', gif,
            '-loop', '0',  # infinite loop in output
            webp
        ]
        
        # Run the command and capture output
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f'Successfully converted {gif} → {webp}')
        else:
            print(f'Error converting {gif}:\n{result.stderr.decode()}')

if __name__ == '__main__':
    # If ffmpeg is not in PATH, specify full path here, e.g.:
    # convert_gif_to_webp(ffmpeg_path=r'C:\ffmpeg\bin\ffmpeg.exe')
    convert_gif_to_webp()
