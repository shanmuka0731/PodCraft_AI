from src.llm.groq_client import generate_response

from src.agent.prompts import (
    create_analysis_prompt,
    create_outline_prompt,
    create_script_prompt,
    create_validation_prompt
)


def generate_podcast_script(article_text):

    # --------------------------------
    # Step 1: Analyze article
    # --------------------------------

    analysis_prompt = create_analysis_prompt(article_text)

    analysis = generate_response(analysis_prompt)


    # --------------------------------
    # Step 2: Create podcast outline
    # --------------------------------

    outline_prompt = create_outline_prompt(analysis)

    outline = generate_response(outline_prompt)


    # --------------------------------
    # Step 3: Generate podcast script
    # --------------------------------

    script_prompt = create_script_prompt(
        analysis,
        outline
    )

    script = generate_response(script_prompt)


    # --------------------------------
    # Step 4: Validate and improve
    # --------------------------------

    validation_prompt = create_validation_prompt(script)

    final_script = generate_response(
        validation_prompt
    )


    return final_script