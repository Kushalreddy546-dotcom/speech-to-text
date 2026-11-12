import os
import sys
import tempfile
from pathlib import Path


def main():
    project_dir = Path(__file__).resolve().parent
    mp3_file = project_dir / "sample.mp3"

    if not mp3_file.is_file():
        print(f"Error: {mp3_file.name} not found in {project_dir}.", file=sys.stderr)
        return 1

    import speech_recognition as sr
    from pydub import AudioSegment

    wav_path = None
    try:
        print("Converting MP3 to WAV...")
        audio = AudioSegment.from_mp3(mp3_file)
        with tempfile.NamedTemporaryFile(suffix=".wav", dir=project_dir, delete=False) as wav_file:
            wav_path = Path(wav_file.name)
        audio.export(wav_path, format="wav")

        recognizer = sr.Recognizer()
        with sr.AudioFile(str(wav_path)) as source:
            print("Reading audio file...")
            audio_data = recognizer.record(source)

        print("Converting speech to text...")
        text = recognizer.recognize_google(audio_data)
        print("\nRecognized Text:")
        print(text)
        return 0
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return 1
    except sr.RequestError as error:
        print("Speech recognition service error:")
        print(error)
        return 1
    except (OSError, RuntimeError) as error:
        print(f"Audio processing error: {error}", file=sys.stderr)
        return 1
    finally:
        if wav_path is not None and wav_path.exists():
            os.remove(wav_path)


if __name__ == "__main__":
    raise SystemExit(main())
