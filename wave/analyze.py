import time

class Bookkeeper():
    def __init__(self):
        self.samples = 0

        self.sum_avg = 0.0
        self.smallest_avg = 0.0
        self.largest_avg = 0.0

        self.sum_stddev = 0.0
        self.smallest_stddev = 0.0
        self.largest_stddev = 0.0

        self.sum_mx = 0
        self.smallest_mx = 0
        self.largest_mx = 0

        self.bins = [0] * 16

    def injest(self, t, avg, stddev, mx):
        if self.samples == 0:
            self.smallest_avg = avg ; self.largest_avg = avg
            self.smallest_stddev = stddev ; self.largest_stddev = stddev
            self.smallest_mx = mx ; self.largest_mx = mx
        else:
            if avg < self.smallest_avg: self.smallest_avg = avg
            if avg > self.largest_avg: self.largest_avg = avg
            if stddev < self.smallest_stddev: self.smallest_stddev = stddev
            if stddev > self.largest_stddev: self.largest_stddev = stddev
            if mx < self.smallest_mx: self.smallest_mx = mx
            if mx > self.largest_mx: self.largest_mx = mx
      
        self.sum_avg += avg
        self.sum_stddev += stddev
        self.sum_mx += mx
        self.samples += 1

        for i in range(16):
            if mx >= (1 << i): self.bins[i] += 1

    def summarize(self):
        print(f"Out of {self.samples} samples...")
        print(f"  avg {self.smallest_avg:.2f} < {self.sum_avg / self.samples:.2f} < {self.largest_avg:.2f}")
        print(f"  stddev {self.smallest_stddev:.2f} < {self.sum_stddev / self.samples:.2f} < {self.largest_stddev:.2f}")
        print(f"  max {self.smallest_mx}.00 < {self.sum_mx / self.samples:.2f} < {self.largest_mx}.00")

        print("bins:")
        for i in range(16):
            print(f"2^{i}: {self.bins[i]}")

class Trigger:
    def __init__(self, threshhold, standoff):
        self.threshhold = threshhold
        self.standoff = standoff
        self.mute_until = 0

    def injest(self, t, avg, stddev, mx):
        if mx >= self.threshhold:
            if t >= self.mute_until:
                self.mute_until = t + self.standoff
                result = "triggered"
            else:
                result = "muted"

            lt = time.localtime(t)
            print(f"{t} {lt.tm_hour:02d}:{lt.tm_min:02d}:{lt.tm_sec:02d} {result}")

    def summarize(self):
        pass


def analyze(path, analyzer):
    with open(path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            t = int(parts[0])
            avg = float(parts[1])
            stddev = float(parts[2])
            mx = int(parts[3])
            analyzer.injest(t, avg, stddev, mx)
    analyzer.summarize()


if __name__ == '__main__':
    # analyze('overnight.log', Trigger(1 << 13, 5))
    # analyze('overnight.log', Trigger(1 << 12, 60))
    analyze('onehour.log', Trigger(1 << 12, 60))
