from pathlib import Path

# Project name
PROJECT_NAME = "Ziro.ai"
PROJECT_LICENSE = "(c) 2025 Aref Daei - MIT License"
PROJECT_VERSION = "1.0.0-rc"

# Project paths
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
TEMP_DIR = OUTPUT_DIR / "temp"

DEBUG = True

# Whisper settings
WHISPER_MODEL = "base"  # tiny, base, small, medium, large
WHISPER_DEVICE = "cpu"  # or "cuda" for GPU
WHISPER_LANGUAGE = "en"

# Translate settings
TRANSLATION_MODEL = "facebook/m2m100_418M"
MAX_TRANSLATION_LENGTH = 512
BATCH_SIZE = 8

# ffmpeg settings
AUDIO_FORMAT = "wav"
AUDIO_CODEC = "pcm_s16le"
AUDIO_RATE = 16000

# Subtitle settings
SRT_ENCODING = "utf-8"
MAX_SUBTITLE_LENGTH = 42  # Maximum character in a line

# Create directories
OUTPUT_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(exist_ok=True)
