#!venv/bin/python

import redis
import uuid

class LimitedHistory:
    """A limited history of items

    A Redis-persistent list with a given max size. New items are added to the
    front of the list. When the maximum number of entries is exceeded, the
    oldest item is silently discarded.
    """

    def __init__(self, r, list_key, max_entries):
        self.r = r
        self.list_key = list_key
        self.max_entries = max_entries

        # Construct a sequence key and ensure that it exists
        self.list_seq_key = list_key + ".seq"
        self.r.setnx(self.list_seq_key, 0)

    def contents(self):
        return self.r.lrange(self.list_key, 0, self.max_entries)

    def add(self, item):
        """Add an item to the front of the list
        """
        def add_and_trim(pipe):
            seq = int(pipe.get(self.list_seq_key))
            pipe.lpush(self.list_key, item)
            pipe.ltrim(self.list_key, 0, self.max_entries - 1)
            pipe.multi()
            pipe.set(self.list_seq_key, seq + 1)
        self.r.transaction(add_and_trim, self.list_seq_key)

r = redis.Redis()

q = LimitedHistory(r, list_key='queue', max_entries=15)

for _ in range(10):
    u = str(uuid.uuid4())
    print("Adding {}".format(u))
    q.add(u)

print("")
for u in q.contents():
    print("       {}".format(u.decode('utf-8')))
