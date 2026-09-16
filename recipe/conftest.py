"""Configuration for running the pyspharm test suite in conda-forge CI.

Hypothesis' default 200 ms deadline is regularly exceeded by the
property-based tests in ``tests/test_hypothesis.py`` on the shared CI
machines (macOS in particular), which makes them fail with
``DeadlineExceeded``/``FlakyFailure`` even though the package is fine.  We
are testing the package, not how fast the CI machine happens to be, so turn
deadlines off.
"""

from hypothesis import settings

settings.register_profile("conda-forge", deadline=None)
settings.load_profile("conda-forge")
