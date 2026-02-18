# Multi-speaker audio transcription

This project is a CLI for multi-speaker audio transcription using [OpenAI Whisper](https://github.com/openai/whisper) (text transcription), [Pyannote-Audio](https://github.com/pyannote/pyannote-audio) (speaker-detection) and [Spleeter](https://github.com/deezer/spleeter) (voice extraction). It can be used to extract audio-segments for each speaker and to create transcriptions in various formats (txt, srt, sami, dfx, transc).

It's compatible with Windows, Linux and Mac.
___

## Installation with uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. It can install Python for you and manage dependencies efficiently.

### Install uv

```shell
# on macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# on Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# or with pip
pip install uv
```

### Install transcripy

**Note**: On Linux, you may need to install ALSA development headers first:
```shell
# on Ubuntu or Debian
sudo apt update && sudo apt install libasound2-dev

# on Arch Linux  
sudo pacman -S alsa-lib
```

**Basic installation** (without Spleeter voice extraction):
```shell
# Let uv install Python 3.11 (recommended)
uv python install 3.11

# Create a virtual environment and install transcripy
uv venv --python 3.11
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install transcripy
```

**With Spleeter** (for voice extraction feature, requires Python 3.11):
```shell
uv python install 3.11
uv venv --python 3.11
source .venv/bin/activate
uv pip install "transcripy[spleeter]"
```

**Note**: `ffmpeg` is included automatically via `ffmpeg-binaries` package - no need to install it separately!

### Quick start

```shell
# Create a simple transcription
transcripy --audio-to-text --model tiny

# See all options
transcripy --help
```

___

## Traditional Installation (Alternative)

<details>
<summary>Click to expand traditional pip-based installation instructions</summary>

### Install system dependencies

**Note**: With the uv installation method above, ffmpeg is included automatically. Only use these instructions if you're not using uv.

```shell
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg libasound2-dev

# on Arch Linux
sudo pacman -S ffmpeg alsa-lib

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

### Install python dependencies

```shell
pip3 install transcripy

# Or with Spleeter (voice extraction):
pip3 install "transcripy[spleeter]"
```

</details>

___

## Data structure

This project requires a fixed folder structure for your data.
Your input data in ``raw_audio/`` or `raw_audio_voices/` may be structured in subfolders

```shell
data/
    raw_audio/              Your original audio data (any formats)
    raw_audio_voices/       Preprocessed audio data (only .wav)

    diarization/            Output-folder of --audio-to-voices and --set-speakers
    text/                   Output-folder of --audio-to-text
    voice_splits/           Output-folder of --text-to-splits
    output/                 Outout-folder for various results
        slices/                 Audio-slices ordered by speaker (--slice)
        analysis/               Analysis output (--viewer)
        transcripts/            Transcripts output (--transcribe)
```

___

## 1. Optional: Audio preprocessing / voice extraction

Follow the setup instructions from [Spleeter](https://github.com/deezer/spleeter).

Run the voice extraction process to filter background audio in audio-files located in `raw_audio/`.

```shell
python -m transcripy --audio-extract-voice
```

Optional arguments:

```shell
--model [spleeter:2stems, spleeter:4stems, spleeter:5stems]    \\ Select the spleeter-model (2 voices, 4 voices, 5 voices) 
--data-path [path]              \\ Root direction of data (without raw_audio/)
--extract-all                   \\ Extract all voices
```

### Alternatives

- Use RipX to extract voices from audio files in `data/raw_audio`. Place them in `data/raw_audio_voices`.

___

## 2. Automatic speech recognition

Follow the setup instructions from [OpenAI Whisper](https://github.com/openai/whisper).

Run the transcription of audio-files (.wav only!) located in  `raw_audio_voices/` with

```shell
python -m transcripy --audio-to-text 
```

Optional arguments:

```shell
--model [tiny,base,small,medium,large]    \\ Select the whisper-model 
--language [lang]               \\ Force the language to detect
--data-path [path]              \\ Root direction of data (without raw_audio_voices/)
```

___

## 3. Detect individual people

Follow the setup instructions from [Pyannote-Audio](https://github.com/pyannote/pyannote-audio).

Run the diarization process to detect multiple readers in audio-files located in `raw_audio_voices/`.

```shell
python -m transcripy --audio-to-voices 
```

Optional arguments:

```shell
--model [pyannote/speaker-diarization, pyannote/segmentation, pyannote/speaker-segmentation, pyannote/overlapped-speech-detection, pyannote/voice-activity-detection]    \\ Select the pyannote-model 
--data-path [path]              \\ Root direction of data (without raw_audio_voices/)
```

### Optional: Assign speakers

To rename the speakers of the audio-files, run

```shell
python -m transcripy --set-speakers
```

___

## 4. Create outputs

> **Important: Make sure that you have completed step 2 and 3**

Create the data you need.

### Transcriptions

Create transcriptions in various formats with

```shell
python -m transcripy --transcribe
```

### Analysis

Create HTML files for visualization of the results with

```shell
python -m transcripy --viewer
```

### Slice

Slice the audio files in separate text-slices with

```shell
python -m transcripy --slice
```

___

## Extra: Text to speech synthetis

### Option 1: Voice Cloning App

- Download the executable for [Voice-Cloning-App](https://github.com/BenAAndrew/Voice-Cloning-App)
- Start it
- Download model for your language
- Create dataset for one speaker with `python -m create-dataset <SPEAKER>`
- Load the dataset into Voice-Cloning-App

### Option 2: Real Time Voice Cloning

Follow the setup instructions from [Real-Time Voice Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning).

```shell
python -m voice-synthesis
```

___

## Related

See this [jupyter-notebook](https://github.com/Majdoddin/nlp/blob/main/Pyannote_plays_and_Whisper_rhymes.ipynb) for a different implementation.
