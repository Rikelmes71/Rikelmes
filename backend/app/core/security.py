import base64
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def _get_key() -> bytes:
    raw = os.getenv("ENCRYPTION_KEY_BASE64", "")
    if not raw:
        raise ValueError("ENCRYPTION_KEY_BASE64 não configurada")
    return base64.b64decode(raw)


def encrypt_value(value: str) -> str:
    key = _get_key()
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, value.encode("utf-8"), None)
    return base64.b64encode(nonce + ciphertext).decode("utf-8")


def decrypt_value(token: str) -> str:
    key = _get_key()
    blob = base64.b64decode(token)
    nonce = blob[:12]
    ciphertext = blob[12:]
    aesgcm = AESGCM(key)
    plain = aesgcm.decrypt(nonce, ciphertext, None)
    return plain.decode("utf-8")
