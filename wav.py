import wave
import numpy as np
import scipy.io.wavfile as wavfile

def read_wav_file(file_path):
    samplerate, data = wavfile.read(file_path)
    return samplerate, data

def calculate_pitch(data, samplerate):
    spectrum = np.fft.fft(data)
    frequencies = np.fft.fftfreq(len(spectrum), d=1/samplerate)

    max_freq_index = np.argmax(np.abs(spectrum))
    pitch = frequencies[max_freq_index]

    return pitch

def main():
    file_path = 'your_audio.wav'
    user_min_pitch = 100

    samplerate, data = read_wav_file(file_path)
    pitch = calculate_pitch(data, samplerate)

    if pitch > user_min_pitch:
        print("The audio is harmful (high pitch).")
    else:
        print("The audio is not harmful (within pitch threshold).")

if __name__ == "__main__":
    main()
