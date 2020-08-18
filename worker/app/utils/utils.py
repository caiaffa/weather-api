import base64


def hash_dict(data: dict) -> str:
    key = ""
    for k, v in data.items():
        key += str(v).lower()
    return base64.b64encode(key.encode()).decode()
