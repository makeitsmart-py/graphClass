from .forward_reference import FwdReference


class __DEFAULT__:
    pass


class DataModelEntity:
    def getter(self):
        pass

    def __init_subclass__(cls, **kwargs):
        FwdReference.resolve_all_references_to_class(cls)
        cls._class_get_all_children()
        super().__init_subclass__(**kwargs)

    @staticmethod
    def _class_get_class_children(cls, output, remove=False):
        to_delete = []
        for n, v in cls.__dict__.items():
            if (isinstance(v, type) and issubclass(v, DataModelEntity)) or isinstance(v, (
                    DataModelEntity, FwdReference)):
                output[n] = v
                if remove:
                    to_delete.append(n)

        if to_delete:
            for n in to_delete:
                delattr(cls, n)

        if cls._children:
            output.update(cls._childs)

    @classmethod
    def _class_get_all_children(cls):
        cls._children = {}
        for subclass in cls.__bases__:
            elements_value = getattr(subclass, '_children', __DEFAULT__)
            if elements_value is __DEFAULT__:
                continue
            if elements_value is None:
                cls._class_get_class_children(subclass, cls._children)
            else:
                cls._children.update(elements_value)
        for n, v in cls._children.items():
            if isinstance(v, FwdReference):
                cls._children[n] = v.clone(cls)
        cls._class_get_class_children(cls, cls._children, remove=True)
        return cls._children