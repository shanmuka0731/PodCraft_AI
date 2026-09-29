from pathlib import Path

from src.podcast.speaker import split_speakers
from src.podcast.tts import generate_audio
from src.podcast.audio_assembler import combine_audio


HOST_VOICE = Path(
    "voices/en_US-amy-medium.onnx"
)

EXPERT_VOICE = Path(
    "voices/en_US-lessac-medium.onnx"
)


def generate_podcast_audio(script):

    conversations = split_speakers(script)

    print("\n========== SPEAKER PARSER ==========")

    print(
        f"Total speaker segments: {len(conversations)}"
    )

    for index, conversation in enumerate(conversations):

        print(
            f"{index}: "
            f"{conversation['speaker']} → "
            f"{conversation['text'][:80]}"
        )

    print("====================================\n")

    # Prevent the mysterious "list index out of range"
    if not conversations:

        raise ValueError(
            "No HOST or EXPERT speaker lines were found in the generated script."
        )

    audio_files = []

    for index, conversation in enumerate(conversations):

        speaker = conversation["speaker"]
        text = conversation["text"]

        if speaker == "HOST":

            voice = HOST_VOICE

        elif speaker == "EXPERT":

            voice = EXPERT_VOICE

        else:

            continue

        output_filename = f"segment_{index}.wav"

        audio_path = generate_audio(
            text,
            voice,
            output_filename
        )

        audio_files.append(audio_path)

    if not audio_files:

        raise ValueError(
            "No audio segments were generated."
        )

    final_audio = combine_audio(
        audio_files,
        "podcast.wav"
    )

    return final_audio