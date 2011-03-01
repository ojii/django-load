class Pool(dict):
    """
    Dummy pool for tests
    """
    def register(self, key, value):
        if key not in self:
            self[key] = []
        self[key].append(value)

pool = Pool()