def create_analysis_prompt(article_text):
    return f"""
Analyze the following article before creating a podcast.

Identify:

1. Main topic
2. Main objective of the article
3. Important concepts
4. Important facts
5. Supporting examples
6. Key takeaways
7. Concepts that should be explained to a general audience

Do not invent information.

Article:
--------------------
{article_text}
--------------------
"""


def create_outline_prompt(analysis):
    return f"""
You are planning an educational podcast.

Based on the article analysis below, create a podcast structure.

The podcast should contain:

1. Opening hook
2. Introduction to the topic
3. Main discussion points
4. Examples or analogies where appropriate
5. Important insights
6. Final summary

Create a logical conversation flow between:

HOST
and
EXPERT

Article analysis:
--------------------
{analysis}
--------------------
"""


def create_script_prompt(analysis, outline):
    return f"""
Create a natural podcast conversation using the analysis and
podcast outline below.

There are exactly two speakers:

HOST:
- Curious
- Asks natural questions
- Keeps the conversation flowing
- Helps the audience understand the topic

EXPERT:
- Explains concepts clearly
- Gives simple examples when useful
- Answers the host's questions

IMPORTANT OUTPUT FORMAT:

Every line MUST begin with either:

HOST:
or
EXPERT:

Example:

HOST: Welcome to today's podcast. Today we're going to talk about AI.

EXPERT: Absolutely. Artificial intelligence is changing the way we build software.

HOST: So how are developers actually using it?

EXPERT: Developers can use AI to generate code, explain errors, and write tests.

Rules:

1. Do not invent facts.
2. Stay faithful to the source material.
3. Do not simply read the article.
4. Make the conversation sound natural.
5. Avoid unnecessary repetition.
6. Explain technical concepts clearly.
7. Keep the conversation engaging.
8. End with the major takeaways.
9. Do NOT use any speaker names other than HOST and EXPERT.
10. Every spoken line must start with HOST: or EXPERT:.

ARTICLE ANALYSIS:
--------------------
{analysis}
--------------------

PODCAST OUTLINE:
--------------------
{outline}
--------------------

Generate the complete podcast script.
"""

def create_validation_prompt(script):
    return f"""
Review the following podcast script.

Check whether:

1. The script is coherent.
2. The conversation sounds natural.
3. The important information is covered.
4. The script contains unsupported claims.
5. There is unnecessary repetition.
6. The ending summarizes the important points.

If improvements are needed, rewrite the script.

Return ONLY the improved final podcast script.

Podcast script:
--------------------
{script}
--------------------
"""