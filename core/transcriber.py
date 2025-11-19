from typing import List, Dict

import whisper

from settings import WHISPER_MODEL, WHISPER_DEVICE


class Transcriber:
    """Speech to text conversion with OpenAI Whisper"""

    def __init__(self, model_name: str = WHISPER_MODEL, device: str = WHISPER_DEVICE):
        self.model_name = model_name
        self.device = device
        self.model = None
        print(f"Loading Whisper model ({model_name})...")

    def load_model(self):
        """Loading the Whisper model"""
        if self.model is None:
            self.model = whisper.load_model(
                self.model_name,
                device=self.device
            )
            print(f"Model {self.model_name} loaded")

    def transcribe(self, audio_path: str, language: str = "en") -> Dict:
        """
        Convert voice to text

        Args:
            audio_path: Path to the audio file
            language: Audio language (en, fa, ...)

        Returns:
            Dictionary containing text and segments with timestamp
        """
        self.load_model()

        print(f"Start transcription: {audio_path}")

        result = self.model.transcribe(
            audio_path,
            language=language,
            task="transcribe",
            verbose=False,
            word_timestamps=False
        )

        print(f"Transcription completed: {len(result['segments'])} segments")

        return result

    def get_segments(self, transcription_result: Dict) -> List[Dict]:
        """
        Extract segments with scheduling

        Returns:
            A list of dictionaries containing:
            - text: text
            - start: start time (seconds)
            - end: end time (seconds)
        """
        segments = []

        for segment in transcription_result['segments']:
            segments.append({
                'text': segment['text'].strip(),
                'start': segment['start'],
                'end': segment['end']
            })

        return segments
