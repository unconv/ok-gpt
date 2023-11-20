from openai import OpenAI

model = OpenAI()

voice = model.audio.speech.create(
    input="Yes?",
    model="tts-1",
    voice="alloy",
)

voice.stream_to_file("sounds/detected.mp3")

voice = model.audio.speech.create(
    input="Just a moment",
    model="tts-1",
    voice="alloy",
)

voice.stream_to_file("sounds/processing.mp3")