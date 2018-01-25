from filesystems import Path
from mate import TestCase
from process import Command
from testtools.matchers import Equals


class TestCommand(TestCase):
    def test_extended(self):
        command = Command("foo", "bar")
        self.assertThat(
            command.extended("--baz", "quux"),
            Equals(Command("foo", "bar", "--baz", "quux")),
        )

    def test_extended_override(self):
        command = Command("foo", "bar", cwd=Path("tmp", "foo"))
        self.assertThat(
            command.extended("baz", cwd=Path("tmp", "bar")),
            Equals(Command("foo", "bar", "baz", cwd=Path("tmp", "bar"))),
        )

    def test_prepended(self):
        command = Command("foo", "bar")
        self.assertThat(
            command.prepended("baz", "quux"),
            Equals(Command("baz", "quux", "foo", "bar")),
        )

    def test_prepended_override(self):
        command = Command("foo", "bar", cwd=Path("tmp", "foo"))
        self.assertThat(
            command.prepended("baz", cwd=Path("tmp", "bar")),
            Equals(Command("baz", "foo", "bar", cwd=Path("tmp", "bar"))),
        )

    def test_random_extra_kwargs(self):
        with self.assertRaises(TypeError):
            Command("foo", bar=123)

    def test_it_is_hashable(self):
        self.assertThat(len({Command("foo"), Command("bar")}), Equals(2))

    def test_extra_nonsense(self):
        with self.assertRaises(TypeError):
            Command("foo", bar=12)
