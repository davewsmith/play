# Record a brief sound snippet

import subprocess
import wave


SAMPLES = 44100 // 4
BYTES_PER_SAMPLE = 2
SECONDS = 5

tool = [
    "arecord",
    "-c", "1",
    f"--duration={SECONDS}",
    f"--rate={SAMPLES}",
    "--format=U8" if BYTES_PER_SAMPLE == 1 else "--format=S16_LE",
]

buffers = [bytearray(SAMPLES * BYTES_PER_SAMPLE) for _ in range(SECONDS)]
next = 0

with subprocess.Popen(tool, stdout=subprocess.PIPE) as proc:
    # while True:
    for _ in range(SECONDS):
        count = proc.stdout.readinto(buffers[next])
        if not count:
            break
        next += 1

with wave.open(f'test-{SAMPLES}-{BYTES_PER_SAMPLE}.wav', 'wb') as w:
    w.setnchannels(1)
    w.setsampwidth(BYTES_PER_SAMPLE)
    w.setframerate(SAMPLES)
    w.setnframes(SECONDS)
    for i in range(SECONDS):
        w.writeframes(buffers[i])

