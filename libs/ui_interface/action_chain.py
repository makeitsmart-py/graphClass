class __DEFAULT__:
    pass


class ActionChain:
    def __init__(self, instance):
        self.instance = instance
        self.original_instance = instance
        self.fn = None

    def __getattr__(self, item):
        self.instance = getattr(self.instance, item)
        return self

    def __call__(self, *args, **kwargs):
        if not callable(self.instance):
            raise TypeError(f"'{self.instance}' object is not callable")
        self.result = self.instance(*args, **kwargs)
        self.instance = self.original_instance
        return self