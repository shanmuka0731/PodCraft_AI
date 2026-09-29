def split_speakers(script):

    conversations = []

    current_speaker = None
    current_text = []

    for line in script.splitlines():

        line = line.strip()

        if not line:
            continue

        # Remove Markdown formatting
        clean_line = line.replace("*", "").strip()

        # --------------------------------
        # New HOST speaker
        # --------------------------------

        if clean_line.startswith("HOST:"):

            # Save previous speaker
            if current_speaker and current_text:

                conversations.append({
                    "speaker": current_speaker,
                    "text": " ".join(current_text).strip()
                })

            current_speaker = "HOST"

            text = clean_line[len("HOST:"):].strip()

            current_text = []

            if text:
                current_text.append(text)

        # --------------------------------
        # New EXPERT speaker
        # --------------------------------

        elif clean_line.startswith("EXPERT:"):

            # Save previous speaker
            if current_speaker and current_text:

                conversations.append({
                    "speaker": current_speaker,
                    "text": " ".join(current_text).strip()
                })

            current_speaker = "EXPERT"

            text = clean_line[len("EXPERT:"):].strip()

            current_text = []

            if text:
                current_text.append(text)

        # --------------------------------
        # Continuation of current speaker
        # --------------------------------

        elif current_speaker:

            # Ignore markdown headings
            if clean_line.startswith("#"):
                continue

            if clean_line == "---":
                continue

            current_text.append(clean_line)

    # --------------------------------
    # Save final speaker
    # --------------------------------

    if current_speaker and current_text:

        conversations.append({
            "speaker": current_speaker,
            "text": " ".join(current_text).strip()
        })

    return conversations