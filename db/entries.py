from unitpackage.cv.cv_entry import CVEntry as Entry
from unitpackage.cv.cv_collection import CVCollection
from db.filter import filter_material
import os

_db = None


def get_db():
    global _db
    entries_path = os.path.join(os.getcwd(), "entries")
    if _db is None:
        _db = CVCollection.from_local(entries_path)
        return _db
    else:
        return _db


def get_entries(filter):
    db = get_db()
    db_filtered = db.filter(lambda entry: filter(entry))
    return db_filtered


def get_entries_with_material(material):
    db = get_db()
    return db.filter(lambda entry: filter_material(entry, material))
