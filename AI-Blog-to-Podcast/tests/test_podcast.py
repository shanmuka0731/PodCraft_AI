from src.agent.podcast_agent import generate_podcast_script


article = """
Artificial intelligence is changing software development.
Developers use AI tools to generate code, explain errors,
write tests and improve productivity. However, developers
still need to understand and verify the generated code.
"""


script = generate_podcast_script(article)

print("\n================ PODCAST SCRIPT ================\n")
print(script)