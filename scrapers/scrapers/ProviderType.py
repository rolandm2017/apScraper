class ProviderType:
    def __init__(self, source):
        self.provider = source  # the only place this should really need to be defined.

    def get_type(self):
        return self.provider