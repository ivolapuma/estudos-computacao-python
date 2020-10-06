from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    # gera length bytes aleatorios
    tb: bytes = token_bytes(length)
    # converte esses bytes em uma cadeia de bits e a devolve
    print("random_key():  length={}  tb={}".format(length, tb))
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy  # XOR
    print("encrypt():  original={}  original_bytes={}".format(original, original_bytes))
    print("encrypt():  dummy={}  original_key={}  encrypted={}".format(dummy, original_key, encrypted))
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2  # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7) // 8, "big")
    print("decrypt():  key1={}  key2={}  decrypted={}".format(key1, key2, decrypted))
    print("decrypt():  temp={}  decrypted.bit_length()={}  ((decrypted.bit_length()+7) // 8)={}".format(temp, decrypted.bit_length(), ((decrypted.bit_length()+7) // 8)))
    return temp.decode()


if __name__ == "__main__":
    original: str = "Ivo La Puma"
    key1, key2 = encrypt(original)
    result: str = decrypt(key1, key2)
    print("main:  original={}  key1={}  key2={}".format(original, key1, key2))
    print("main:  result={}".format(result))
