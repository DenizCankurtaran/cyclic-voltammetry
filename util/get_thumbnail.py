import base64


def get_thumbnail(entry):
    base64_image = base64.b64encode(entry.thumbnail()).decode("utf-8")
    return f"data:image/png;base64,{base64_image}"
