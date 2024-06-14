def create_source(entry_source):
    source = dict()
    source['citationKey'] = entry_source['citation key']

    source['url'] = entry_source['url']
    if 'techniques' in entry_source:
        if isinstance(entry_source['techniques'], list):
            source['techniques'] = entry_source['techniques']
        else:
            source['techniques'] = entry_source['techniques'].split(", ")
    source['figure'] = entry_source['figure']
    source['curve'] = entry_source['curve']
    source['bibdata'] = entry_source['bibdata']
    return source