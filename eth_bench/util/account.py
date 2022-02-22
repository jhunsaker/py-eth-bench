import random

from coincurve import PublicKey
from sha3 import keccak_256


def create_account():

    input = random.randbytes(32)
    private_key = keccak_256(input).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(
        compressed=False
    )[1:]
    address = keccak_256(public_key).digest()[-20:]
    return private_key, address
