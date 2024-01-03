# Redis Playground

Playing around with Redis

## References

  * https://redis.io/docs/data-types/
  * https://redis.io/commands/
  * https://redis.readthedocs.io/en/latest/

## LimitedHistory

Maintain an ordered, finite-sized list of items.
Items are added to the front of the list, and excess
items are silently discarded from the end, within
a Redis transaction.

