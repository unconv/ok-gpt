import audioop
import whisper
import pyaudio
import wave
import os

whisper_model = whisper.load_model("base")
ambient_detected = False
speech_volume = 100

def live_speech(wait_time=10):
    global ambient_detected
    global speech_volume

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    frames = []
    recording = False
    frames_recorded = 0

    while True:
        frames_recorded += 1
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)

        if not ambient_detected:
            if frames_recorded < 40:
                if frames_recorded == 1:
                    print("Detecting ambient noise...")
                if frames_recorded > 5:
                    if speech_volume < rms:
                        speech_volume = rms
                continue
            elif frames_recorded == 40:
                print("Listening...")
                speech_volume = speech_volume * 3
                ambient_detected = True

        if rms > speech_volume:
            recording = True
            frames_recorded = 0
        elif recording and frames_recorded > wait_time:
            recording = False

            wf = wave.open("audio.wav", 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            result = whisper_model.transcribe(
                "audio.wav",
                fp16=False
            )

            os.remove("audio.wav")

            yield result["text"].strip()

            frames = []

        if recording:
            frames.append(data)

    # TODO: do these when breaking from generator
    stream.stop_stream()
    stream.close()
    audio.terminate()
