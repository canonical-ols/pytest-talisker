from setuptools import setup

setup(
    name="pytest-talisker",
    packages=["pytest_talisker"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["talisker = pytest_talisker.pluginmodule"]},
    install_requires=["talisker", ],
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)
