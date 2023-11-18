from pocketsphinx import LiveSpeech
from collections import defaultdict

phrases = defaultdict(int)

for i in range(10):
    print("Please say 'OK, GPT'")
    for phrase in LiveSpeech():
        print(f"Heard '{str(phrase)}'")
        phrases[str(phrase)] += 1
        break

    sorted_phrases = sorted(phrases.items(), key=lambda x: x[1], reverse=True)
    if sorted_phrases[0][1] >= 2:
        break

print("Recognition finished")

frequent_phrase = sorted_phrases[0][0]
print(f"Now, speak! ({frequent_phrase})")

#for heard in LiveSpeech():
#    for phrase, _ in sorted_phrases:
#        if phrase in str(heard):
#            print(f"Detected '{str(heard)}'")

speech = LiveSpeech(keyphrase=frequent_phrase, kws_threshold=1e-10)
for phrase in speech:
    print(phrase.segments(detailed=True))
