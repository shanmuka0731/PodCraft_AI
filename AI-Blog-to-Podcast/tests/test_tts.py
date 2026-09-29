from src.podcast.tts import generate_audio


HOST_VOICE = "voices/en_US-amy-medium.onnx"
EXPERT_VOICE = "voices/en_US-lessac-medium.onnx"


host_audio = generate_audio(
    "Hello and welcome to today's podcast!",
    HOST_VOICE,
    "host_test.wav"
)


expert_audio = generate_audio(
    "Today we are going to discuss artificial intelligence.",
    EXPERT_VOICE,
    "expert_test.wav"
)


print("Host audio:", host_audio)
print("Expert audio:", expert_audio)