import subprocess
import tempfile
from pathlib import Path


VOICE_DIR = Path("voices")
OUTPUT_DIR = Path("output")


def generate_audio(text, voice_model, output_filename):

    OUTPUT_DIR.mkdir(exist_ok=True)

    output_path = OUTPUT_DIR / output_filename

    command = [
        "piper",
        "--model",
        str(voice_model),
        "--output_file",
        str(output_path)
    ]

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="",
        suffix=".txt",
        dir=OUTPUT_DIR,
        delete=False
    ) as input_file:
        input_file.write(text)
        input_path = Path(input_file.name)

    try:
        subprocess.run(
            command + ["--input_file", str(input_path)],
            check=True
        )
    finally:
        input_path.unlink(missing_ok=True)

    return output_path