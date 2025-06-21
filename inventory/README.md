A quick hack to inventory a huge collection of old files

This produces a CSV. To load it into sqlite3,

    python3 inventory.py | sqlite3 -csv inventory.db ".import '|cat -'" inventory

