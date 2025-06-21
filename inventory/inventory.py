from datetime import datetime
import hashlib
import os
from stat import ST_CTIME, ST_SIZE
from time import localtime, strftime

SKIP_DIRS = (
    '__pycache__',
    '.git',
    '.vagrant',
    'venv',
    'venv.ansible',
    'node_modules')


def cull(dirs):
    for skip in SKIP_DIRS:
        try:
            i = dirs.index(skip)
            del dirs[i]
        except ValueError:
            pass

def calc_md5(path):
    try:
        with open(path, "rb") as f:
            return hashlib.file_digest(f, "md5").hexdigest()
    except:
        return "X"

def ext_if_any(filename):
    if filename and filename[0] == ".":
        # special case `.git` et al.
        return ""
    parts = filename.split(".")
    return parts[-1] if len(parts) > 1 else ""

def timestamp(epochtime):
    return datetime.fromtimestamp(epochtime).strftime('%Y-%m-%d %H:%M:%S')

def inventory_header():
    print("md5,prefix,fullpath,filename,ext,size,created")

def inventory(path):
    for (prefix, dirs, files) in os.walk(path):
        if len(files):
            cull(dirs)
            for filename in files:
                full_path = os.path.join(prefix, filename)
                stat = os.stat(full_path)
                created = timestamp(stat[ST_CTIME])
                size = stat[ST_SIZE]
                md5 = calc_md5(full_path)
                ext = ext_if_any(filename)
                print(f'{md5},"{prefix}","{full_path}","{filename}","{ext}",{size},{created}')

if __name__ == '__main__':
    inventory_header()
    inventory('.')
