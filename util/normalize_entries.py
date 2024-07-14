from normalization.normalization import (
    normalize_ref,
    normalize_electrolyte_concentration,
    normalize_scan_rate,
)

# Main funciton to normalize the entries. This function checks what normalization method
# was used by checking what variable(s) has content, and normalize the entries depending
# on that.
def normalize_entries(entries, ref_electrode=None, c_ref=None, ion=None, ref_scan_rate=None):
    normalized_entries = []
    for entry in entries:
        # Creates a copy of the entry to avoid normalized entries to get re-normalized
        # when for example a normalization method is used multiple times.
        copied_df = entry.df.copy()
        # Normalize Reference Electrode
        if ref_electrode:
            delta_ref = normalize_ref(entry, ref_electrode)
            copied_df["E"] = copied_df["E"] + delta_ref
        # Normalize Electrolyte Concentration
        if c_ref and ion is not None:
            try:
                delta_ref = normalize_electrolyte_concentration(entry, c_ref, ion)
                copied_df["E"] = copied_df["E"] + delta_ref
            except:
                print(f"No electrolyte entry found for {entry}")
                continue
        # Normalize Scan Rate
        if ref_scan_rate is not None:
            delta_ref = normalize_scan_rate(entry, ref_scan_rate)
            copied_df["j"] = copied_df["j"] * delta_ref
        normalized_entries.append({"df": copied_df, "identifier": entry.identifier})
    return normalized_entries
