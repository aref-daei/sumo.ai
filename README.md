# SUMO.AI 🎬

**Smart Desktop Application for Automated Bilingual Subtitle Generation**

Convert English videos to videos with Persian and English subtitles using AI.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

---

## ✨ Features

- 🎙️ **Speech-to-Text** with OpenAI Whisper
- 🌐 **Auto Translation** to Persian with HuggingFace Transformers
- 📝 Generate separate **SRT** files (English & Persian)
- 🎬 Add subtitles to video (**soft-subtitle**)
- 🖥️ **Graphical UI** with CustomTkinter
- ⚡ Support for **CPU** and **GPU**
- 📦 **Batch** processing of multiple videos

---

## 📋 Prerequisites

- Python 3.10 or higher
- ffmpeg
- 4GB+ RAM (8GB+ recommended)
- GPU optional (for faster processing)

---

## 📖 Usage

### Graphical Interface (GUI)

1. Run `python main.py`
2. Select video file
3. Adjust options
4. Click "Start Processing"

---

## ⚙️ Configuration

Edit `config.py`:

```python
# Whisper model
WHISPER_MODEL = "base"  # tiny, base, small, medium, large

# Processing device
WHISPER_DEVICE = "cpu"  # or "cuda"

# Translation model
TRANSLATION_MODEL = "facebook/m2m100_418M"

# Batch size
BATCH_SIZE = 8
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
