from src.podcast.podcast_generator import generate_podcast_audio


script = """
HOST: Welcome to today's podcast.

EXPERT: Today we are discussing artificial intelligence.

HOST: What exactly is artificial intelligence?

EXPERT: Artificial intelligence allows computers to perform tasks that normally require human intelligence.

HOST: That sounds interesting!

EXPERT: It is already being used in many areas of technology.
"""


audio = generate_podcast_audio(script)

print("Podcast generated:")
print(audio)