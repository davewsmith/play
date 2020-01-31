# Redis experiments

Playing around with Redis

## LimitedHistory

Maintain an ordered, finite-sized list of items.
Items are added to the front of the list, and excess
items are silently discarded from the end, within
a Redis transaction.

