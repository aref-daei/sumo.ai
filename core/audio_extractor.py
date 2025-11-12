from pathlib import Path

import ffmpeg

from config import TEMP_DIR, FFMPEG_AUDIO_RATE, FFMPEG_AUDIO_CODEC


class AudioExtractor:
    """Extract audio from video with ffmpeg"""

    def __init__(self):
        self.verify_ffmpeg()

    @staticmethod
    def verify_ffmpeg():
        """Check if ffmpeg is installed"""
        try:
            ffmpeg.probe("test")
        except ffmpeg.Error:
            pass
        except FileNotFoundError:
            raise RuntimeError(
                "ffmpeg is not installed. Please download from https://ffmpeg.org"
            )

    @staticmethod
    def extract(video_path: str, output_name: str = None) -> str:
        """
        Extract audio from video

        Args:
            video_path: video file path
            output_name: output file name (optional)

        Returns:
            Path to the extracted audio file
        """
        if output_name is None:
            output_name = f"{Path(video_path).stem}_audio.wav"

        output_path = TEMP_DIR / output_name

        try:
            # Audio extraction with optimized settings for Whisper
            stream = ffmpeg.input(video_path)
            stream = ffmpeg.output(
                stream,
                str(output_path),
                acodec=FFMPEG_AUDIO_CODEC,
                ar=FFMPEG_AUDIO_RATE,
                ac=1  # Convert to mono
            )
            ffmpeg.run(stream, overwrite_output=True, capture_stderr=True)

            return str(output_path)

        except ffmpeg.Error as e:
            error_message = e.stderr.decode() if e.stderr else str(e)
            raise RuntimeError(f"Error extracting audio: {error_message}")

    @staticmethod
    def get_video_duration(video_path: str) -> float:
        """Get video length in seconds"""
        try:
            probe = ffmpeg.probe(video_path)
            duration = float(probe['format']['duration'])
            return duration
        except Exception as e:
            raise RuntimeError(f"Error reading video information: {e}")
