from whisper import Whisper

class AutoTranslation:
    def __init__(self, config):
        self.config = config
        self.model = Whisper("base")

    def translate(self, audio, target_language):
        # Real-time speech translation
        transcription = self.model.transcribe(audio)
        return self.model.translate(transcription, target_language)
