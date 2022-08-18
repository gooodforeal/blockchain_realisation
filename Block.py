import datetime
import hashlib
from binascii import unhexlify, hexlify


class Block:
    def __init__(self, prev_hash, transaction, amount, number):
        self.next = None
        self.__data = {
            "prev_hash": prev_hash,
            "transaction": transaction,
            "amount": amount,
            "hash": "",
            "time": str(datetime.datetime.now()),
            "number": number
        }

        self.__data["hash"] = self.make_hash()

    def get_data(self):
        return self.__data

    def make_hash(self):
        hash = hexlify(hashlib.sha256(unhexlify(self.get_data()["prev_hash"])).digest()).decode("utf-8")
        while hash[:2] != "00":
            hash = hexlify(hashlib.sha256(unhexlify(hash)).digest()).decode("utf-8")
        return hash

    def append(self, transaction, amount):
        i = self
        while  i.next:
            i = i.next
        prev_hash = i.get_data()["hash"]
        prev_number = i.get_data()["number"]
        end = Block(prev_hash, transaction, amount, prev_number + 1)
        i.next = end