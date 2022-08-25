import pytest

import talisker

@pytest.fixture(scope="session", autouse=True)
def talisker_ctx():
    """Ensure that all tests run under a clean talisker test context & environment"""
    talisker.testing.clear_all()
    talisker.get_config.update()
    with talisker.testing.TestContext() as ctx:
        yield ctx
