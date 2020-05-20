import mmh3, random


class CuckooBucket:
    def __init__(self, bucket_size):
        self.bucket_size = bucket_size
        self.bucket = []

    def __contains__(self, fingerprint):
        if fingerprint in self.bucket:
            return True
        else:
            return False

    def insert(self, fingerprint):
        if len(self.bucket) < self.bucket_size:
            self.bucket.append(fingerprint)
            return True
        else:
            return False

    def remove(self, fingerprint):
        try:
            index = self.bucket.index(fingerprint)
            del self.bucket[index]
            return True
        except ValueError:
            return False

    def swap_fingerprints(self, fingerprint):
        random_index = random.randrange(0, self.bucket)
        random_fingerprint = self.bucket[random_index]
        fingerprint, self.bucket[random_index] = random_fingerprint, fingerprint

        return fingerprint


class CuckooFilter:
    def __init__(
        self,
        table_size=10,
        bucket_size=5,
        fingerprint_size=10,
        hash_fn=mmh3.hash_bytes,
        max_swaps=100,
    ):
        self.table_size = table_size
        self.bucket_size = bucket_size
        self.fingerprint_size = fingerprint_size
        self.hash_fn = hash_fn
        self.max_swaps = max_swaps
        self.table = []
        self.item_count = 0

        for i in range(self.table_size):
            self.table.append(CuckooBucket(bucket_size=self.bucket_size))

    def get_fignerprint(self, item):
        hash_value = self.hash_fn(item)
        fingerprint = hash_value[: self.fingerprint_size]

        return fingerprint

    def get_index(self, item):
        hash_value = self.hash_fn(item)
        index = int.from_bytes(hash_value, byteorder="big")
        index = index % self.table_size

        return index

    def get_indices(self, item):
        index_1 = self.get_index(item)
        fingerprint = self.get_fignerprint(item)
        index_2 = index_1 ^ self.get_index(fingerprint)
        index_2 = index_2 % self.table_size

        return index_1, index_2

    def insert(self, item):
        if not isinstance(item, str):
            raise ValueError("Cuckoo Filter item being inserted not of type string!")

        index_1, index_2 = self.get_indices(item)
        fingerprint = self.get_fignerprint(item)

        if self.table[index_1].insert(fingerprint):
            self.item_count += 1
            return index_1

        if self.table[index_2].insert(fingerprint):
            self.item_count += 1
            return index_2

        random_index = random.choice(index_1, index_2)

        for swap in range(self.max_swaps):
            fingerprint = self.table[random_index].swap_fingerprints(fingerprint)
            random_index = random_index ^ self.get_index(fingerprint)
            random_index = random_index % self.table_size

            if self.table[random_index].insert(fingerprint):
                self.item_count += 1
                return random_index

        raise Exception("Cuckoo Filter hit the max swap limit, table must be rehashed!")

    def remove(self, item):
        index_1, index_2 = self.get_indices(item)
        fingerprint = self.get_fignerprint(item)

        if self.table[index_1].remove(fingerprint):
            self.item_count -= 1
            return index_1

        if self.table[index_2].remove(fingerprint):
            self.item_count -= 1
            return index_2

        raise Exception("Cuckoo Filter does not contain this item!")

    def __contains__(self, item):
        index_1, index_2 = self.get_indices(item)
        fingerprint = self.get_fignerprint(item)

        if fingerprint in self.table[index_1] or fingerprint in self.table[index_2]:
            return True

        return False

    def load_factor(self):
        return self.item_count / (self.table_size * self.bucket_size)
