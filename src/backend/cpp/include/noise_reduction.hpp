#pragma once
#include <vector>

class NoiseReduction {
public:
    NoiseReduction();
    std::vector<float> process(const std::vector<float>& audio);
private:
    void* rnnoise_model; // RNNoise model pointer
};
