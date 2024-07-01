from unitpackage.cv.cv_entry import CVEntry as Entry
from unitpackage.cv.cv_collection import CVCollection
from db.filter import filter_materials_and_system_type
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


def get_all_entries():
    db = get_db()
    return db


def get_entries(filter):
    db = get_db()
    db_filtered = db.filter(lambda entry: filter(entry))
    return db_filtered


def get_entries_with_materials_and_system_type(materials, system_type):
    db = get_db()
    return db.filter(lambda entry: filter_materials_and_system_type(entry, materials, system_type))


def get_entry_by_name(name):
    db = get_db()

    db_filtered = [entry for entry in db if name == entry.identifier]
    return db_filtered