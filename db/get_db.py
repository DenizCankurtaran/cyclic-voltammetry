from unitpackage.collection import Collection

db = Collection.from_remote()
db.save_entries('entries')