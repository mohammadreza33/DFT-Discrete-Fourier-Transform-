"""-------------------------------------------------------------
a program that calculate the DFT (Descrete Fourier Transform)---
author: mohammadreza mohammadi :)                            ---
9612325089                                                   ---
"""                                                         
# import necessary libraries
import simpleaudio as sa
import numpy as np
import matplotlib.pyplot as plt


frequency = 200     # Our played note will be 440 Hz
samplePerSec = 44100          # 44100 samples per second

# Generate a 440 Hz sine wave
t=np.arange(0 , 1 , 1/samplePerSec)  
note = np.sin(frequency * t * 2 * np.pi)

# Start playback for 2 or 3 seconds
play_obj = sa.play_buffer(note, 1, 2, samplePerSec)

# Wait for playback to finish
play_obj.wait_done()

# Generate a 440 Hz sine wave to check DFT algorithm
t=np.arange(0 , 0.01 , 1/samplePerSec)  
s = np.sin(frequency * t * 2 * np.pi) #  input signal   
N = len(s)  # N show the length of signal

# (S show the DFT points)
S = [0 for _ in range(N)]   # Initialization the S with 0

# DFT calculation
for i in range(N):
    for j in range(N):
        tmp = [((0-1j)*(2*np.pi*i*j)) / N]
        S[i] += s[j] * np.exp(tmp)

"--------------------------------------------------------------------"
# DFT diagrams
plt.figure("Descrete fourier transform")
plt.subplot(3, 1, 1)
plt.scatter([i for i in range(N)], [j for j in s])
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.title('input signal  ')
plt.grid(True)

plt.subplot(3, 1, 2)
mag_S = [np.sqrt(i.real**2 + i.imag**2) for i in S]
plt.scatter([i for i in range(N)], mag_S)
plt.title('magnetude response')
plt.xlabel('frequency')
plt.ylabel('|x[k]|')
plt.grid(True)

plt.subplot(3, 1, 3)
phase_S = np.angle(S)
plt.scatter([i for i in range(N)], phase_S)
plt.title('phase response ')
plt.xlabel('frequency')
plt.ylabel('phase')
plt.grid(True)

plt.tight_layout()
plt.show()
"----------------------------------------------------"
# FFT diagrams
plt.figure("Fast Fourier Transform")
plt.subplot(3, 1, 1)
plt.scatter([i for i in range(N)], [j for j in s])
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.title('input signal ')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.scatter([i for i in range(N)], np.abs(np.fft.fft(s)))
plt.title('magnetude response')
plt.xlabel('frequency')
plt.ylabel('|x[k]|')
plt.grid(True)

plt.subplot(3, 1, 3)
phase_S = np.angle(np.fft.fft(s))
plt.scatter([i for i in range(N)], phase_S)
plt.title('phase response ')
plt.xlabel('frequency')
plt.ylabel('phase')
plt.grid(True)

plt.tight_layout()
plt.show()
"----------------------------------------------------------"