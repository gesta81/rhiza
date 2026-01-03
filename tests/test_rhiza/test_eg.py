"""Tests for the eg module."""

from rhiza.eg import x


def test_x():
    """Test that function x returns 1."""
    result = x()
    assert result == 1
