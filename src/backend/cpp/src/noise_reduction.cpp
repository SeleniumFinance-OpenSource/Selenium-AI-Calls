#include "noise_reduction.hpp"
#include <rnnoise.h>

NoiseReduction::NoiseReduction() {
    rnnoise_model = rnnoise_create(nullptr);
}

std::vector<float> NoiseReduction::process(const std::vector<float>& audio) {
    std::vector<float> output(audio.size());
    for (size_t i = 0; i < audio.size(); i += 480) {
        float* frame = &output[i];
        rnnoise_process_frame(rnnoise_model, frame, frame);
    }
    return output;
}
