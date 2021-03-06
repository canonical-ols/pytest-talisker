from setuptools import setup

setup(
    version = '0.2.0',
    name="pytest-talisker",
    packages=["pytest_talisker"],
    url="https://github.com/canonical-ols/pytest-talisker",
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["talisker = pytest_talisker.pluginmodule"]},
    install_requires=["talisker", ],
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)
