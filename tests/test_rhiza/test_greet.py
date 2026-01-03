"""Tests for the greet function in rhiza.eg module."""

from rhiza.eg import greet


class TestGreet:
    """Tests for the greet function."""

    def test_greet_default(self):
        """Greet should return 'Hello, World!' when called without arguments."""
        assert greet() == "Hello, World!"

    def test_greet_with_name(self):
        """Greet should return personalized greeting when given a name."""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_with_different_names(self):
        """Greet should work with various names."""
        assert greet("Bob") == "Hello, Bob!"
        assert greet("Charlie") == "Hello, Charlie!"
        assert greet("Python") == "Hello, Python!"
