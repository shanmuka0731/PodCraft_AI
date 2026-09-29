from src.podcast.speaker import split_speakers


script = """
### Introduction

**HOST:**

Welcome to today's podcast.

Today we are discussing artificial intelligence.

**EXPERT:**

Artificial intelligence allows computers to perform tasks
that normally require human intelligence.

**HOST:**

That's interesting. Can you give us an example?

**EXPERT:**

Sure. AI can help developers write code and explain errors.

---

### Key Takeaways

**HOST:**

Let's recap.

**EXPERT:**

AI is becoming an important tool in modern software development.
"""


result = split_speakers(script)


print("\n========== RESULT ==========\n")

print("Total segments:", len(result))

for index, item in enumerate(result):

    print(
        f"{index}: {item['speaker']} → {item['text']}"
    )