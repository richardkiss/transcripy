"""
transcripy - Multi-speaker audio transcription
"""

# Initialize ffmpeg-binaries to make ffmpeg available to pydub and other tools
try:
    # Try to import ffmpeg-binaries. Note: if ffmpeg-python is installed (from spleeter),
    # it will conflict. In that case, we skip initialization and assume system ffmpeg is available.
    import ffmpeg as ffmpeg_module
    if hasattr(ffmpeg_module, 'init'):
        # This is ffmpeg-binaries
        ffmpeg_module.init()
        ffmpeg_module.add_to_path()
    # else: This is ffmpeg-python (from spleeter), which doesn't need initialization
except ImportError:
    # If neither is installed, assume system ffmpeg is available
    pass

__version__ = "0.1.0"
