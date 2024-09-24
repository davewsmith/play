from sqlite_utils import Database

db = Database(memory=True)
dogs = db.table("dogs", pk="id")
humans = db.table("humans", pk="id")

print("---- after defining tables ----")
print(db.schema)
assert db.schema == ""

dogs.insert({"id": 1, "name": "Cleo"}).m2m(
    humans, [
        {"id": 1, "name": "Natalie"},
        {"id": 2, "name": "Simon"}
    ]
)

print("---- after first insert ----")
print(db.schema)

print("---- reseting ----")

db = Database(memory=True)

db["dogs"].create({
    "id": int,
    "name": str,
}, pk="id")

db["humans"].create({
    "id": int,
    "name": str,
}, pk="id")

db["dogs_humans"].create({
    "dogs_id": int,
    "humans_id": int},
    pk=[
        "dogs_id", "humans_id"
    ],
    foreign_keys=[
        ("dogs_id", "dogs"),
        ("humans_id", "humans")
    ],
)

print("---- after manual create ---")
print(db.schema)

dog_id = db["dogs"].insert({"name": "Gosby"}).last_pk
human_id = db["humans"].insert({"name": "Dave"}).last_pk
composite_id = db["dogs_humans"].insert({"dogs_id": dog_id, "humans_id": human_id}).last_pk
print(composite_id)
composite_id = db["dogs_humans"].insert({"dogs_id": dog_id, "humans_id": human_id}).last_pk
