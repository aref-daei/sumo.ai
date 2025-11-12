from pathlib import Path
from typing import List, Dict

from config import SRT_ENCODING


class SubtitleGenerator:
    """Generating SRT files"""

    @staticmethod
    def format_timestamp(seconds: float) -> str:
        """
        Convert seconds to SRT format: 00:00:00,000

        Args:
            seconds: time in seconds

        Returns:
            formatted string
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)

        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

    def generate_srt(self, segments: List[Dict], output_path: str) -> str:
        """
        Generate SRT file

        Args:
            segments: list of segments with text, start, end
            output_path: output file path

        Returns:
            path to generated file
        """
        srt_content = []

        for i, segment in enumerate(segments, start=1):
            # Subtitle number
            srt_content.append(str(i))

            # Scheduling
            start_time = self.format_timestamp(segment['start'])
            end_time = self.format_timestamp(segment['end'])
            srt_content.append(f"{start_time} --> {end_time}")

            # Text
            srt_content.append(segment['text'])

            # Blank line between subtitles
            srt_content.append("")

        # Writing a file
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding=SRT_ENCODING) as f:
            f.write('\n'.join(srt_content))

        print(f"SRT file created: {output_path}")
        return str(output_path)

    def create_bilingual_srt(self, segments_en: List[Dict],
                             segments_fa: List[Dict],
                             output_path: str) -> str:
        """
        Generate bilingual SRT file (English + Persian)

        Args:
            segments_en: English segments
            segments_fa: Persian segments
            output_path: output file path

        Returns:
            path to generated file
        """
        srt_content = []

        for i, (seg_en, seg_fa) in enumerate(zip(segments_en, segments_fa), start=1):
            srt_content.append(str(i))

            start_time = self.format_timestamp(seg_en['start'])
            end_time = self.format_timestamp(seg_en['end'])
            srt_content.append(f"{start_time} --> {end_time}")

            # Display two languages
            srt_content.append(seg_en['text'])
            srt_content.append(seg_fa['text'])
            srt_content.append("")

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding=SRT_ENCODING) as f:
            f.write('\n'.join(srt_content))

        print(f"Bilingual SRT file created: {output_path}")
        return str(output_path)
