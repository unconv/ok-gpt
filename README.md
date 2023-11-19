# Ok, GPT!

This is an ongoing project where I'm building my own Google Home / Alexa style device that can be interacted with via voice commands.

Currently only the wakeup keyphrase detection and subsequent voice command detection is done, using OpenAI Whisper (local, not API). You need to initialize it with the `init.py` script by saying the keyphrase you want to wake up the device with 10 times. After that you can run `recognize.py` and it will recognize when you say the keyphrase and after saying the keyphrase it will recognize the next speech as the command.

Video: https://www.youtube.com/watch?v=_vLKWNv4d5E
