"""
transcripy - Multi-speaker audio transcription
"""

# Initialize ffmpeg-binaries to make ffmpeg available to pydub and other tools
try:
    # Try to import ffmpeg. Note: both ffmpeg-binaries and ffmpeg-python use the same
    # import name 'ffmpeg'. ffmpeg-python (from spleeter) doesn't need initialization,
    # while ffmpeg-binaries requires calling init(). We check for the 'init' attribute
    # to determine which package is installed.
    import ffmpeg as ffmpeg_module
    if hasattr(ffmpeg_module, 'init'):
        # This is ffmpeg-binaries - initialize and add to PATH
        ffmpeg_module.init()
        ffmpeg_module.add_to_path()
    # else: This is ffmpeg-python (from spleeter), which doesn't need initialization
except ImportError:
    # If neither is installed, assume system ffmpeg is available
    pass

__version__ = "0.1.0"
