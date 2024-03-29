Pytest-Talisker - a pytest plugin for talisker
----------------------------------------------

This pytest plugin will ensure an early initialisation of talisker, ensuring
similar behaviour as when using in a regular runtime flow.

Early initialisation, at least before test related loggers are initialized, is
needed, as the logger class will be replaced by a talisker specific one,
providing additional functionality.

Usage
-----

To use this plugin, simply install it next to pytest.

```
pip install pytest-talisker
```

And in the tests, talisker.testing functionality will be available to use.

See also
--------

* https://talisker.readthedocs.io
* https://github.com/canonical-ols/talisker
