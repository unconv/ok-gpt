from multiprocessing import Process, Queue
from pocketsphinx import LiveSpeech
import json
import sys
import os

def listen_word(word, queue):
    speech = LiveSpeech(keyphrase=word, kws_threshold=1e-10)
    for phrase in speech:
        queue.put(f"Detected: {phrase.segments(detailed=True)}")

def listen_words(words, queue):
    processes: list[Process] = []
    for word in words:
        processes.append(Process(target=listen_word, args=(word,queue)))

    for process in processes:
        process.start()

    while True:
        detection = queue.get()
        print(detection)

    for process in processes:
        process.join()

if not os.path.exists("phrases.json"):
    print("You must run init.py first!")
    sys.exit(1)

with open("phrases.json", "r") as f:
    phrases = json.load(f)

print("Detecting keyphrase...")

queue = Queue()

listen_words(phrases, queue)
