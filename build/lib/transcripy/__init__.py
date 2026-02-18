"""
transcripy - Multi-speaker audio transcription
"""

# Initialize ffmpeg-binaries to make ffmpeg available to pydub and other tools
try:
    import ffmpeg as ffmpeg_binaries
    ffmpeg_binaries.init()
    ffmpeg_binaries.add_to_path()
except ImportError:
    # If ffmpeg-binaries is not installed, assume system ffmpeg is available
    pass

__version__ = "0.1.0"
