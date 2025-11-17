from typing import List

import torch
from transformers import MarianMTModel, MarianTokenizer, M2M100ForConditionalGeneration, M2M100Tokenizer

from config import TRANSLATION_MODEL, MAX_TRANSLATION_LENGTH, BATCH_SIZE


class Translator:
    """Text translation with HuggingFace Transformers"""

    def __init__(self, model_name: str = TRANSLATION_MODEL):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using the device: {self.device}")

    def load_model(self):
        """Loading translation model"""
        if self.model is None:
            print(f"Loading translation model: {self.model_name}")

            if "opus-mt" in self.model_name:
                # Helsinki-NLP models
                self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
                self.model = MarianMTModel.from_pretrained(self.model_name)
            elif "m2m100" in self.model_name:
                # M2M100 models
                self.tokenizer = M2M100Tokenizer.from_pretrained(self.model_name)
                self.model = M2M100ForConditionalGeneration.from_pretrained(self.model_name)
                self.tokenizer.src_lang = "en"
                self.tokenizer.tgt_lang = "fa"

            self.model.to(self.device)
            print("Translation model loaded")

    def translate_text(self, text: str) -> str:
        """
        Translating a text

        Args:
            text: English text

        Returns:
            Persian text
        """
        self.load_model()

        if not text.strip():
            return ""

        # Tokenize
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=MAX_TRANSLATION_LENGTH
        ).to(self.device)

        # Translation
        with torch.no_grad():
            translated = self.model.generate(
                **inputs,
                max_length=MAX_TRANSLATION_LENGTH,
                num_beams=4,
                early_stopping=True
            )

        # Decode
        translated_text = self.tokenizer.decode(
            translated[0],
            skip_special_tokens=True
        )

        return translated_text.strip()

    def translate_batch(self, texts: List[str]) -> List[str]:
        """
        Batch translation of texts (faster)

        Args:
            texts: List of English texts

        Returns:
            List of Persian texts
        """
        self.load_model()

        translations = []

        # Batch processing
        for i in range(0, len(texts), BATCH_SIZE):
            batch = texts[i:i + BATCH_SIZE]

            # Remove empty text
            non_empty_batch = [t for t in batch if t.strip()]

            if not non_empty_batch:
                translations.extend([""] * len(batch))
                continue

            # Tokenize
            inputs = self.tokenizer(
                non_empty_batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=MAX_TRANSLATION_LENGTH
            ).to(self.device)

            # Translation
            with torch.no_grad():
                translated = self.model.generate(
                    **inputs,
                    max_length=MAX_TRANSLATION_LENGTH,
                    num_beams=4,
                    early_stopping=True
                )

            # Decode
            batch_translations = [
                self.tokenizer.decode(t, skip_special_tokens=True).strip()
                for t in translated
            ]

            translations.extend(batch_translations)

            print(f"Translated: {i + len(batch)}/{len(texts)}")

        return translations
