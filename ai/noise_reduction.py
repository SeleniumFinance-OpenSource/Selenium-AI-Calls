import torch
from rnnoise import RNNoise

class NoiseReduction:
    def __init__(self, config):
        self.config = config
        self.model = RNNoise()

    def process(self, audio):
        # Apply RNNoise neural network for noise suppression
        return self.model.denoise(audio)
