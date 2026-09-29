import wave
from pathlib import Path


OUTPUT_DIR = Path("output")


def combine_audio(audio_files, output_filename="podcast.wav"):

    OUTPUT_DIR.mkdir(exist_ok=True)

    output_path = OUTPUT_DIR / output_filename

    if not audio_files:
        raise ValueError("No audio files were provided.")

    print("\n========== AUDIO ASSEMBLY ==========")

    # Read the first WAV file to get its audio format
    with wave.open(str(audio_files[0]), "rb") as first_audio:

        channels = first_audio.getnchannels()
        sample_width = first_audio.getsampwidth()
        frame_rate = first_audio.getframerate()
        compression = first_audio.getcomptype()
        compression_name = first_audio.getcompname()

        print("Channels:", channels)
        print("Sample width:", sample_width)
        print("Frame rate:", frame_rate)

        if channels == 0:
            raise ValueError(
                f"Invalid WAV file: {audio_files[0]} has 0 channels."
            )

        all_frames = [
            first_audio.readframes(
                first_audio.getnframes()
            )
        ]

    # Read remaining files
    for audio_file in audio_files[1:]:

        print("Adding:", audio_file)

        with wave.open(str(audio_file), "rb") as audio:

            # Make sure all WAV files use the same format
            if (
                audio.getnchannels() != channels
                or audio.getsampwidth() != sample_width
                or audio.getframerate() != frame_rate
            ):
                raise ValueError(
                    f"Audio format mismatch in {audio_file}"
                )

            all_frames.append(
                audio.readframes(
                    audio.getnframes()
                )
            )

    # Create final WAV
    with wave.open(str(output_path), "wb") as output:

        output.setnchannels(channels)
        output.setsampwidth(sample_width)
        output.setframerate(frame_rate)
        output.setcomptype(
            compression,
            compression_name
        )

        for frames in all_frames:
            output.writeframes(frames)

    print(
        "\nFinal podcast created:",
        output_path
    )

    print(
        "File size:",
        output_path.stat().st_size,
        "bytes"
    )

    return output_path