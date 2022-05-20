import pytest

import talisker

@pytest.fixture(scope="session", autouse=True)
def talisker_ctx():
    """Ensure that all tests run under a talisker test context"""
    with talisker.testing.TestContext() as ctx:
        yield ctx
