# Speech to Text

Transcribe speech from `sample.mp3` using the Google Speech Recognition service.
The recognition request requires an internet connection.

## Requirements

- Python 3
- FFmpeg available on your `PATH` (required by pydub to read MP3 files)
- The included `sample.mp3` synthetic English speech sample; replace it with your own audio to transcribe a different clip

Install FFmpeg:

- Ubuntu, Debian, or Codespaces: `sudo apt update && sudo apt install -y ffmpeg`
- macOS: `brew install ffmpeg`
- Windows: install FFmpeg and add its `bin` folder to `PATH`

Verify the installation with `ffmpeg -version`.

## Install and run

```bash
python3 -m pip install -r requirements.txt
python3 speech_to_text.py
```

The script converts the MP3 to a temporary WAV file, transcribes it, prints the
recognized text, and removes the temporary file.

## Sample output

Running `python3 speech_to_text.py` with the included sample produces:

```text
Recognized Text:
hello this is a speech recognition test the quick brown fox jumped over the lazy dog
```