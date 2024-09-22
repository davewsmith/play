# oui2csv

with open('standards-oui.ieee.org.txt', 'r') as standard:
    with open('oui.csv', 'w') as csv:
        for line in standard:
            if '(base 16)' in line:
                parts = line.strip().split(maxsplit=3)
                # print(repr(parts))
                if '"' in parts[3]:
                    assert False, "org name has a double-quote"
                csv.write(f'{parts[0]},"{parts[3]}"\n')
                    


