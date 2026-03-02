# Project:      ci-test-python-package
# License:      FSL-1.1-ALv2
# Copyright:    (c) 2026 HYPERI PTY LIMITED

"""Tests for ci_test_package.utils."""

from ci_test_package.utils import add, greet, is_palindrome


class TestAdd:
    """Tests for the add() function."""

    def test_add_positive_numbers(self) -> None:
        """Verify addition of two positive integers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self) -> None:
        """Verify addition of two negative integers."""
        assert add(-1, -1) == -2

    def test_add_zero(self) -> None:
        """Verify addition with zero returns the other operand."""
        assert add(0, 5) == 5

    def test_add_mixed_sign(self) -> None:
        """Verify addition of a positive and a negative integer."""
        assert add(10, -3) == 7


class TestGreet:
    """Tests for the greet() function."""

    def test_greet_simple_name(self) -> None:
        """Verify greeting with a simple name."""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_empty_string(self) -> None:
        """Verify greeting with an empty string."""
        assert greet("") == "Hello, !"

    def test_greet_with_spaces(self) -> None:
        """Verify greeting with a name that contains spaces."""
        assert greet("Bob Smith") == "Hello, Bob Smith!"


class TestIsPalindrome:
    """Tests for the is_palindrome() function."""

    def test_simple_palindrome(self) -> None:
        """Verify a simple lowercase palindrome is recognised."""
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self) -> None:
        """Verify a non-palindrome returns False."""
        assert is_palindrome("hello") is False

    def test_mixed_case_palindrome(self) -> None:
        """Verify palindrome detection is case-insensitive."""
        assert is_palindrome("Madam") is True

    def test_palindrome_with_spaces(self) -> None:
        """Verify palindrome detection ignores spaces."""
        assert is_palindrome("Race Car") is True

    def test_single_character(self) -> None:
        """Verify a single character is a palindrome."""
        assert is_palindrome("a") is True

    def test_empty_string(self) -> None:
        """Verify an empty string is considered a palindrome."""
        assert is_palindrome("") is True
