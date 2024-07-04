# NOTE: First try _dev.scm_version if it exists and setuptools_scm is installed
# This file is not included in sunpy wheels/tarballs, so otherwise it will
# fall back on the generated _version module.
try:
    try:
        from ._dev.scm_version import version as __version__
    except ImportError:
        from ._version import version as __version__
except Exception:
    import warnings

    warnings.warn(
        f'could not determine {__name__.split(".")[0]} package version; this indicates a broken installation'
    )
    del warnings

    __version__ = '0.0.0'


__all__ = ['__version__']
