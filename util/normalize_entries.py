from normalization.normalization import (
    normalize_ref,
    normalize_electrolyte_concentration,
    normalize_scan_rate,
)

def normalize_entries(entries, ref_electrode=None, c_ref=None, ion=None, ref_scan_rate=None):
    normalized_entries = []
    for entry in entries:
        copied_df = entry.df.copy()
        if ref_electrode:
            delta_ref = normalize_ref(entry, ref_electrode)
            copied_df["E"] = copied_df["E"] + delta_ref
        if c_ref and ion is not None:
            try:
                delta_ref = normalize_electrolyte_concentration(entry, c_ref, ion)
                copied_df["E"] = copied_df["E"] + delta_ref
            except:
                print(f"No electrolyte entry found for {entry}")
                continue
        if ref_scan_rate is not None:
            delta_ref = normalize_scan_rate(entry, ref_scan_rate)
            copied_df["j"] = copied_df["j"] * delta_ref
        normalized_entries.append({"df": copied_df, "identifier": entry.identifier})
    return normalized_entries
