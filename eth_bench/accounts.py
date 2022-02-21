import random

from coincurve import PublicKey
from sha3 import keccak_256


class BenchAccounts:
    def __init__(self, count: int, seed: int = 1337):

        self._count = count
        self._seed = seed
        random.seed(seed)
        inputs = [random.randbytes(32) for _ in range(count)]
        private_keys = [keccak_256(input).digest() for input in inputs]
        public_keys = [
            PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
            for private_key in private_keys
        ]
        assert isinstance(public_keys[0], (bytes,))
        addresses = [
            keccak_256(public_key).digest()[-20:] for public_key in public_keys
        ]
        assert isinstance(addresses[0], (bytes,))
        self._private_keys = private_keys
        self._addresses = addresses

    @property
    def count(self):

        return self._count

    @property
    def seed(self):

        return self._seed

    def get_private_key(self, i: int) -> bytes:

        return self._private_keys[i]

    def get_address(self, i: int) -> bytes:

        return self._addresses[i]
