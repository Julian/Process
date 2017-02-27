from pyrsistent import pdeque
import attr


@attr.s(init=False)
class Command(object):
    """
    A command.

    """

    argv = attr.ib()
    cwd = attr.ib()

    def __init__(self, *argv, **kwargs):
        self.cwd = kwargs.pop("cwd", None)
        if kwargs:
            object(**kwargs)

        self.argv = pdeque(argv)

    def arguments(self, *argv, **kwargs):
        fields = attr.asdict(self)
        fields.update(kwargs)
        argv = fields.pop("argv").extend(argv)
        return self.__class__(*argv, **fields)

    def prepended_arguments(self, *argv, **kwargs):
        fields = attr.asdict(self)
        fields.update(kwargs)
        argv = fields.pop("argv").extendleft(reversed(argv))
        return self.__class__(*argv, **fields)
