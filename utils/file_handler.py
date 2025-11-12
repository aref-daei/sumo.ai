import os
import shutil
from pathlib import Path

from config import TEMP_DIR


class FileHandler:
    """File management"""

    @staticmethod
    def get_file_size(file_path: str) -> int:
        """Get file size in bytes"""
        return os.path.getsize(file_path)

    @staticmethod
    def format_size(size_bytes: int) -> str:
        """Formatting file size"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f} TB"

    @staticmethod
    def clean_temp_files():
        """Clear temporary files"""
        if TEMP_DIR.exists():
            for file in TEMP_DIR.glob("*"):
                try:
                    if file.is_file():
                        file.unlink()
                    elif file.is_dir():
                        shutil.rmtree(file)
                except Exception as e:
                    print(f"Error deleting {file}: {e}")

    @staticmethod
    def ensure_directory(path: str):
        """Make sure the folder exists"""
        Path(path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def get_safe_filename(filename: str) -> str:
        """Remove illegal characters from file names"""
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename
