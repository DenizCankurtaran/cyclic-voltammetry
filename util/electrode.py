def create_ce_electrode(ce):
    ce_electrode = dict()
    ce_electrode["name"] = ce["name"]
    ce_electrode["function"] = ce["function"]
    ce_electrode["material"] = ce["material"]
    if "crystallographic orientation" in ce:
        ce_electrode["crystallographicOrientation"] = ce["crystallographic orientation"]
    if "supplier" in ce:
        ce_electrode["supplier"] = ce["supplier"]
    if "shape" in ce:
        ce_electrode["shape"] = ce["shape"]
    return ce_electrode


def create_ref_electrode(ref):
    ref_electrode = dict()
    ref_electrode["name"] = ref["name"]
    ref_electrode["function"] = ref["function"]
    if "source" in ref:
        if "supplier" in ref["source"]:
            ref_electrode["source"] = ref["source"]["supplier"]
        else:
            ref_electrode["source"] = ref["source"]
    if "supplier" in ref:
        ref_electrode["supplier"] = ref["supplier"]
    if "type" in ref:
        ref_electrode["type"] = ref["type"]
    return ref_electrode


def create_we_electrode(we):
    we_electrode = dict()
    we_electrode["name"] = we["name"]
    we_electrode["function"] = we["function"]
    we_electrode["material"] = we["material"]
    we_electrode["crystallographicOrientation"] = we["crystallographic orientation"]
    if "geometric electrolyte contact area" in we:
        we_electrode["geometricElectrolyteContactArea"] = we[
            "geometric electrolyte contact area"
        ]["unit"]
    if "shape" in we:
        we_electrode["shape"] = we["shape"]
    if "source" in we:
        we_electrode["source"] = we["source"]
    return we_electrode


# move to better folder?
def get_electrolyte_composition(electrolyte):
    composition = []
    for component in electrolyte["components"]:

        concentration = ""
        if "concentration" in component:
            if "value" in component["concentration"]:
                concentration = component["concentration"]["value"]
            else:
                # TODO: concentraion value does not have to be defined
                concentration = ""
        if component["name"] == "water":
            composition.append(f"{concentration} H2O")
        else:
            composition.append(f"{concentration} {component['name']}")

    return " + ".join(composition)
