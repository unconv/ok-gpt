# Ok, GPT!

This is an ongoing project where I'm building my own Google Home / Alexa style device that can be interacted with via voice commands.

Currently it can detect a wakeup keyphrase, such as "Ok, GPT!" and then listen to a voice command. Speech recognition is done with OpenAI Whisper, locally. The command is then sent to the ChatGPT API and the response is spoken via the OpenAI Text-to-Speech API.

You need to initialize it with the `init.py` script by saying the keyphrase you want to wake up the device with 10 times. After that you can run `recognize.py` and it will recognize when you say the keyphrase and then listen for the command.

## Quick Start

```shell
$ export OPENAI_API_KEY=YOUR_API_KEY
$ pip install -r requirements.txt
$ python3 init.py
$ python3 recognize.py
```

## Videos

The building of this project is documented on my YouTube channel.

- Video 1: https://www.youtube.com/watch?v=_vLKWNv4d5E
- Video 2: https://www.youtube.com/watch?v=xQdLiyCxyWQ
