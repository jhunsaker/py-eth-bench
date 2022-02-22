import random

from .util.account import create_account


class BenchAccounts:
    def __init__(self, count: int, seed: int = 1337):

        self._count = count
        self._seed = seed
        random.seed(seed)
        private_keys = []
        addresses = []
        for _ in range(count):
            private_key, address = create_account()
            private_keys.append(private_key)
            addresses.append(address)
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
