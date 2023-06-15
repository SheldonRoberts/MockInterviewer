"""Use wisper to convert speech to text. This file contains the function that converts speech to text."""

import whisper


def speech_to_text(audio_file_path: str) -> str:
    """Converts speech to text using the wisper library"""
    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path)
    return result["text"]


if __name__ == "__main__":
    file_name = "data/Conflict_Resp_Interview.mp3"
    print(speech_to_text(file_name))
