# Project:      ci-test-python-package
# License:      FSL-1.1-ALv2
# Copyright:    (c) 2026 HYPERI PTY LIMITED

"""Utility functions for the ci-test-package library."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    Performs a straightforward addition of the two provided values.

    Args:
        a: The first integer operand.
        b: The second integer operand.

    Returns:
        The sum of ``a`` and ``b``.
    """
    return a + b


def greet(name: str) -> str:
    """Return a personalised greeting string.

    Constructs a greeting message addressed to the given name.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string in the form ``Hello, <name>!``.
    """
    return f"Hello, {name}!"


def is_palindrome(text: str) -> bool:
    """Check whether the given text is a palindrome.

    The comparison is case-insensitive and ignores spaces so that phrases
    such as "Race Car" are recognised as palindromes.

    Args:
        text: The string to check.

    Returns:
        ``True`` if ``text`` is a palindrome, ``False`` otherwise.
    """
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]
