from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("contributors-test")
except PackageNotFoundError:
    # package is not installed
    pass
