from pyrsistent import pdeque
import attr


@attr.s(hash=True, init=False)
class Command(object):
    """
    A command.

    Inspired by Rust's :rust:`std::process::Command
    <std/process/struct.Command.html>`.

    """

    argv = attr.ib()
    cwd = attr.ib()

    def __init__(self, *argv, **kwargs):
        self.cwd = kwargs.pop("cwd", None)
        if kwargs:
            object(**kwargs)

        self.argv = pdeque(argv)

    def extended(self, *argv, **kwargs):
        fields = attr.asdict(self)
        fields.update(kwargs)
        argv = fields.pop("argv").extend(argv)
        return self.__class__(*argv, **fields)

    def prepended(self, *argv, **kwargs):
        fields = attr.asdict(self)
        fields.update(kwargs)
        argv = fields.pop("argv").extendleft(reversed(argv))
        return self.__class__(*argv, **fields)
