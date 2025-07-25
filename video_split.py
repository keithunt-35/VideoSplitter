import os
import time
from moviepy import VideoFileClip

def split_video(video_path, output_dir, clip_duration=60):
    try:
        video_duration = int(VideoFileClip(video_path).duration)  # Get duration once

        os.makedirs(output_dir, exist_ok=True)
        base_filename = os.path.splitext(os.path.basename(video_path))[0]

        print(f"\n🎬 Splitting '{base_filename}' into {clip_duration}-second clips...")
        total_clips = (video_duration + clip_duration - 1) // clip_duration

        for i, start_time in enumerate(range(0, video_duration, clip_duration), 1):
            end_time = min(start_time + clip_duration, video_duration)
            clip_filename = os.path.join(output_dir, f"{base_filename}_part{i:03d}.mp4")

            # 🛡️ Isolate each FFmpeg call via 'with' block
            with VideoFileClip(video_path).subclipped(start_time, end_time) as clip:
                clip.write_videofile(clip_filename, codec="libx264", audio_codec="aac")
                print(f"✅ Saved: {clip_filename} ({i}/{total_clips})")

            time.sleep(1)  # 💤 Let FFmpeg fully settle before next round

        print(f"🎉 Finished splitting '{base_filename}'! Total clips created: {total_clips}")

    except Exception as e:
        print(f"❌ Error processing '{video_path}': {str(e)}")

def process_folder(folder_path, output_root="all_clips", clip_duration=60, video_exts=(".mp4", ".mov", ".avi", ".mkv")):
    if not os.path.exists(folder_path):
        print(f"❌ Input folder not found: {folder_path}")
        return

    os.makedirs(output_root, exist_ok=True)
    video_files = [f for f in os.listdir(folder_path) if f.lower().endswith(video_exts)]

    if not video_files:
        print(f"❌ No video files found in '{folder_path}'")
        return

    print(f"\n📁 Found {len(video_files)} video file(s) to process...")

    for filename in video_files:
        input_path = os.path.join(folder_path, filename)
        output_dir = os.path.join(output_root, os.path.splitext(filename)[0])
        split_video(input_path, output_dir, clip_duration)

# 🚀 Example usage
if __name__ == "__main__":
    input_folder = r"C:\\Users\\user\\Downloads\\videos71-80"
    process_folder(input_folder)
