from filesystems import Path
from mate import TestCase
from process import Command
from testtools.matchers import Equals


class TestCommand(TestCase):
    def test_arguments(self):
        command = Command("foo", "bar")
        self.assertThat(
            command.arguments("--baz", "quux"),
            Equals(Command("foo", "bar", "--baz", "quux")),
        )

    def test_arguments_override(self):
        command = Command("foo", "bar", cwd=Path("tmp", "foo"))
        self.assertThat(
            command.arguments("baz", cwd=Path("tmp", "bar")),
            Equals(Command("foo", "bar", "baz", cwd=Path("tmp", "bar"))),
        )

    def test_prepended_arguments(self):
        command = Command("foo", "bar")
        self.assertThat(
            command.prepended_arguments("baz", "quux"),
            Equals(Command("baz", "quux", "foo", "bar")),
        )

    def test_prepended_arguments_override(self):
        command = Command("foo", "bar", cwd=Path("tmp", "foo"))
        self.assertThat(
            command.prepended_arguments("baz", cwd=Path("tmp", "bar")),
            Equals(Command("baz", "foo", "bar", cwd=Path("tmp", "bar"))),
        )

    def test_random_extra_kwargs(self):
        with self.assertRaises(TypeError):
            Command("foo", bar=123)
