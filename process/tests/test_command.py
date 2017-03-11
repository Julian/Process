from unittest import TestCase

from filesystems import Path
from process import Command


class TestCommand(TestCase):
    def test_arguments(self):
        command = Command("foo", "bar")
        self.assertEqual(
            command.arguments("--baz", "quux"),
            Command("foo", "bar", "--baz", "quux"),
        )

    def test_arguments_override(self):
        command = Command("foo", "bar", cwd=Path("tmp", "foo"))
        self.assertEqual(
            command.arguments("baz", cwd=Path("tmp", "bar")),
            Command("foo", "bar", "baz", cwd=Path("tmp", "bar")),
        )

    def test_prepended_arguments(self):
        command = Command("foo", "bar")
        self.assertEqual(
            command.prepended_arguments("baz", "quux"),
            Command("baz", "quux", "foo", "bar"),
        )

    def test_prepended_arguments_override(self):
        command = Command("foo", "bar", cwd=Path("tmp", "foo"))
        self.assertEqual(
            command.prepended_arguments("baz", cwd=Path("tmp", "bar")),
            Command("baz", "foo", "bar", cwd=Path("tmp", "bar")),
        )

    def test_random_extra_kwargs(self):
        with self.assertRaises(TypeError):
            Command("foo", bar=123)
