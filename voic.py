import speech_recognition as sr  #handling the microphone input and audio recording part
import whisper

# Load Whisper model
print("Loading model...")
model = whisper.load_model("small")

# Initialize recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("✅ Ready for listening... (Press Ctrl+C to stop)")

try:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # noise reduction
        while True:
            print("🎤 Listening...")
            audio = recognizer.listen(source, phrase_time_limit=3)  # listen in 3 sec chunks
            with open("temp.wav", "wb") as f:  #Each 3-second audio chunk is saved to a temporary .wav file named "temp.wav".
                f.write(audio.get_wav_data())

            # Transcribe with Whisper
            result = model.transcribe("temp.wav")
            text = result["text"].strip()
            if text:
                print(f"💬 {text}")
except KeyboardInterrupt:
    print("\n🛑 Exiting...")
