import ujson
import hashlib


def hash_dict(data: dict) -> str:
    return hashlib.md5(ujson.dumps(data).encode()).hexdigest()
