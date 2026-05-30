# Record a brief sound snippet

import math
import struct
import subprocess
import time
import wave

# DEVICE = "default"
DEVICE = "sysdefault:CARD=GoMic"

SAMPLES = 44100 // 4
BYTES_PER_SAMPLE = 2
SECONDS = 8 * 60 * 60

tool = [
    "arecord",
    "-D", DEVICE,
    "-c", "1",
    f"--duration={SECONDS}",
    f"--rate={SAMPLES}",
    "--format=U8" if BYTES_PER_SAMPLE == 1 else "--format=S16_LE",
]

buffers = [bytearray(SAMPLES * BYTES_PER_SAMPLE) for _ in range(SECONDS)]

def run():
    with subprocess.Popen(tool, stdout=subprocess.PIPE) as proc:
        next = 0
        while True:
        # for _ in range(SECONDS):
            count = proc.stdout.readinto(buffers[next])
            if not count:
                break
            process(buffers[next])
            next += 1
            if next == len(buffers):
                next = 0

def process(buffer):
    t = int(time.time())
    if BYTES_PER_SAMPLE == 1:
        max_int = max((int(b) for b in buffer))
        sum_ints = sum((int(b) for b in buffer))
        avg = sum_ints / SAMPLES
        sumdevs = sum((math.pow(int(b) - avg, 2) for b in buffer))
        stddev = math.sqrt(sumdevs / SAMPLES)
        print(f"{t},{avg:.2f},{stddev:.2f},{max_int}")
    elif BYTES_PER_SAMPLE == 2:
        ints = struct.unpack(f"<{SAMPLES}h", buffer)
        max_int = max((abs(i) for i in ints))
        sum_ints = sum((abs(i) for i in ints))
        avg = sum_ints / SAMPLES
        sumdevs = sum((math.pow(abs(i) - avg, 2) for i in ints))
        stddev = math.sqrt(sumdevs / SAMPLES)
        print(f"{t},{avg:.2f},{stddev:.2f},{max_int}")
    else:
        print("not yet")

if __name__ == '__main__':
    run()
