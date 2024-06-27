def filter_material(entry, material):
    we = entry.get_electrode("WE")
    mat_prop = we["material"] == material
    return mat_prop


def filter_system_type(entry, system_type):
    return entry.system.electrolyte.type == system_type


def filter_materials_and_system_type(entry, materials, system_type):
    filter_material_matches = any(
        [filter_material(entry, material) for material in materials]
    )
    filter_system_type_matches = filter_system_type(entry, system_type)

    return all([filter_material_matches, filter_system_type_matches])


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
