# Video Splitter

A Python tool that automatically splits video files into smaller clips of specified duration.

## Inspiration
- After asking a few people for a script to split videos, I was met with silence and excuses. So, i decided to create my own script. 
- After a few iterations, I got a working version that eventually helped me.
- This was made for you and all the people who need video splitters.

## Features

- 🎬 Split videos into equal-duration clips (default: 60 seconds)
- 📁 Process entire folders of videos at once
- � Supports multiple video formats (.mp4, .mov, .avi, .mkv)
- ✅ Progress tracking with visual feedback
- 🛡️ Error handling and resource management

## Installation

1. Clone or download this project
2. Install required dependencies:
```bash
pip install moviepy
```

### Creating a Virtual Environment (Recommended)
It's good practice to create a virtual environment for Python projects to manage dependencies. Here's how:

1. Create the virtual environment:
```bash
python -m venv venv
```

2. Activate the environment:
   - On Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies within the virtual environment:
```bash
pip install moviepy
```

## Usage

### Basic Usage
```python
from video_split import process_folder

# Split all videos in a folder into 60-second clips
process_folder("path/to/your/videos")
```

### Custom Settings
```python
# Custom clip duration and output location
process_folder(
    folder_path="C:\\Users\\user\\Downloads\\videos",
    output_root="my_clips",
    clip_duration=30  # 30-second clips
)
```

### Run the Script
```bash
python video_split.py
```

## Output Structure
```
all_clips/
├── video1/
│   ├── video1_part001.mp4
│   ├── video1_part002.mp4
│   └── ...
└── video2/
    ├── video2_part001.mp4
    └── ...
```

## Configuration

Edit the example usage section in `video_split.py`:
```python
if __name__ == "__main__":
    input_folder = r"C:\path\to\your\videos"  # Change this path
    process_folder(input_folder)
```

## Requirements

- Python 3.6+
- moviepy
- FFmpeg (automatically installed with moviepy)

## Supported Formats

- Input: .mp4, .mov, .avi, .mkv
- Output: .mp4 (H.264 video, AAC audio)

## License

This project is open source and available under the MIT License.
