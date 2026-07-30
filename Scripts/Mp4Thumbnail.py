import os
import subprocess

def export_thumbnails(ffmpeg_path='ffmpeg', timestamp="00:00:01"):
    """
    Exports JPEG thumbnails from all MP4 files in the current directory.
    
    Args:
        ffmpeg_path: Path to ffmpeg executable (defaults to 'ffmpeg' in PATH).
        timestamp: Time in the video (HH:MM:SS) where the thumbnail is taken.
    """
    mp4_files = [f for f in os.listdir('.') if f.lower().endswith('.mp4')]
    
    if not mp4_files:
        print("No MP4 files found in the current directory.")
        return

    for video in mp4_files:
        thumbnail_name = os.path.splitext(video)[0] + "_thumb.jpg"
        print(f'Extracting thumbnail from "{video}" → "{thumbnail_name}"...')

        cmd = [
            ffmpeg_path,
            '-ss', timestamp,   # seek to position
            '-i', video,        # input file
            '-frames:v', '1',   # extract 1 frame
            '-q:v', '2',        # quality (2=high, 31=low)
            '-y', thumbnail_name
        ]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print(f'Successfully created {thumbnail_name}')
        else:
            print(f'Error creating thumbnail for {video}:\n{result.stderr.decode()}')

if __name__ == '__main__':
    # Example: grab frame at 3 seconds instead of 1
    export_thumbnails(timestamp="00:00:03")
