class __DEFAULT__:
    pass


class FwdReference:
    target_class_name = None
    args = None
    kwargs = None
    name = None
    owner = None
    _unresolved_references = {}

    def __init__(self, class_name: str, *args, **kwargs):
        bucket = self._unresolved_references.get(class_name, None)
        if bucket is None:
            bucket = self._unresolved_references[class_name] = []
        bucket.append(self)
        self.target_class_name = class_name
        self.args = args
        self.kwargs = kwargs

    @classmethod
    def resolve_all_references_to_class(cls, target_class: type):
        bucket = cls._unresolved_references.get(target_class.__name__, __DEFAULT__)
        if bucket is __DEFAULT__:
            return
        for reference in bucket:
            reference.resolve(target_class)
        del cls._unresolved_references[target_class.__name__]

    def resolve(self, target_class):
        setattr(self.owner, self.name, target_class)

    def clone(self, new_target_class):
        instance = self.__class__(class_name=self.target_class_name, *self.args, **self.kwargs)
        instance.__set_name__(new_target_class, self.name)
        return instance

    def __get__(self, instance, owner):
        raise RuntimeError(
             f"{self.owner}.{self.name}: Can't resolve forward reference for {self.target_class_name}")

    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name
