import os
import subprocess

def convert_mp4_to_webp(ffmpeg_path='ffmpeg'):
    mp4_files = [f for f in os.listdir('.') if f.lower().endswith('.mp4')]
    if not mp4_files:
        print("No MP4 files found in the current directory.")
        return

    # Ensure 'Webp' folder exists
    webp_folder = 'Webp'
    os.makedirs(webp_folder, exist_ok=True)

    for mp4 in mp4_files:
        webp_filename = os.path.splitext(mp4)[0] + '_15fps.webp'
        webp_path = os.path.join(webp_folder, webp_filename)
        print(f'Converting "{mp4}" to "{webp_path}"...')

        # ffmpeg command to convert mp4 to animated webp
        cmd = [
            ffmpeg_path,
            '-i', mp4,
            '-vcodec', 'libwebp',
            '-filter:v', 'fps=15',      # adjust fps to control smoothness / file size
            '-lossless', '0',           # lossy compression
            '-compression_level', '6',  # 0=fast, 6=slow/better
            '-q:v', '50',               # quality (0-100)
            '-loop', '0',               # infinite loop
            '-preset', 'default',
            webp_path
        ]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f'Successfully converted {mp4} → {webp_path}')
        else:
            print(f'Error converting {mp4}:\n{result.stderr.decode()}')

if __name__ == '__main__':
    convert_mp4_to_webp()
