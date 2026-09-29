# Project:   ci-test-python-lib
# License:   FSL-1.1-ALv2
# Copyright: (c) 2026 HYPERI PTY LIMITED
"""Throwaway probe for hyperi-io/hyperi-ci#402. Never merge."""

import subprocess


def _git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def test_no_git_credential_reaches_the_tests() -> None:
    """The workspace git config resolves no auth header for github.com."""
    # Key names and the files they come from only, never a value.
    names = _git(
        "config", "--show-origin", "--name-only", "--get-regexp",
        r"extraheader|^includeif\.",
    ).stdout
    header = _git("config", "--get", "http.https://github.com/.extraheader").stdout
    assert not names.strip() and not header, (
        f"credential config visible to tests ({len(header.strip())} chars "
        f"of header value):\n{names}"
    )
