# Parse Access Point (AP) info from nmcli output

from dataclasses import dataclass, field


@dataclass
class AP:
    # at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    bssid: str = ""
    ssid: str = ""
    mode: str = ""
    chan: int = 0
    rate: str = ""
    signal: int = 0
    security: str = ""


class Parser:
    def __init__(self, nmcli_header):
        self.parse_header(nmcli_header)

    def parse_header(self, nmcli_header):
        # TBD use the header as a guide to parse the rest
        pass

    def parse(self, nmcli_line):
        return dict(
            # skip IN-USE
            BSSID=nmcli_line[8:27].strip(),
            SSID=nmcli_line[27:49].strip(),
            MODE=nmcli_line[49:56].strip(),
            CHAN=int(nmcli_line[56:62].strip()),
            RATE=nmcli_line[62:74].strip(),
            SIGNAL=int(nmcli_line[74:82].strip()),
            # skip BARS
            SECURITY=nmcli_line[88:96].strip())

    def ap(self, nmcli_line):
        parts = self.parse(nmcli_line)

        return AP(
            bssid=parts['BSSID'],
            ssid=parts['SSID'],
            mode=parts['MODE'],
            chan=parts['CHAN'],
            rate=parts['RATE'],
            signal=parts['SIGNAL'],
            security=parts['SECURITY'])


def aps(nmcli_output: str):

    lines = nmcli_output.splitlines()
    parser = Parser(lines.pop(0))
    for line in lines:
        yield parser.ap(line)

if __name__ == '__main__':

    with open('sample.txt', 'r') as f:
        nmcli_output = f.read()

    for ap in aps(nmcli_output):
        print(ap)
