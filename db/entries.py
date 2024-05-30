from unitpackage.cv.cv_entry import CVEntry as Entry
from unitpackage.cv.cv_collection import CVCollection
import os

_db = None


def get_db():
    entries_path = os.path.join(os.getcwd(), "entries")
    print(entries_path)
    return CVCollection.from_local(entries_path)
    if _db is None:
        _db = CVCollection.from_local(entries_path)
        return _db
    else:
        return _db


def get_entries(filter):
    db = get_db()
    db_filtered = db.filter(lambda entry: filter(entry))
    return db_filtered


def filter_Ag100Br(entry):
    """
    Example function which returns all CVEntries that have a
    silver ("Ag") working electrode, with the '100' hkl index,
    and with an electrolyte containing the atom "Br".
    """
    ### WE = "working electrode"
    we = entry.get_electrode("WE")
    mat_prop = we["material"] == "Ag"
    hkl_prop = we["crystallographic orientation"] == "100"
    prop3 = any(["Br" in c.name for c in entry.system.electrolyte.components])
    return all([mat_prop, hkl_prop, prop3])
