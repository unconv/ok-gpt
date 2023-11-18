from pocketsphinx import LiveSpeech
import json

phrases = []

for i in range(10):
    print("Please say the keyhprase")
    for phrase in LiveSpeech():
        print(f"Heard '{str(phrase)}'")
        phrases.append(str(phrase))
        break

with open("phrases.json", "w") as f:
    json.dump(phrases, f)

print("Recognition finished")

