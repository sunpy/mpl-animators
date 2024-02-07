# Configuration file for the Sphinx documentation builder.
import datetime
from pathlib import Path

from sunpy_sphinx_theme import PNG_ICON

# -- Project information -----------------------------------------------------
project = "mpl-animators"
author = "The SunPy Community"
copyright = f"{datetime.datetime.now(datetime.timezone.utc).year}, {author}"  # NOQA: A001
author = "The SunPy Developers"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_gallery.gen_gallery",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"
master_doc = "index"
default_role = "obj"
html_theme = "sunpy"

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {
    "python": (
        "https://docs.python.org/3/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/python3.inv"),
    ),
    "numpy": (
        "https://numpy.org/doc/stable/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/numpy.inv"),
    ),
    "matplotlib": (
        "https://matplotlib.org/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/matplotlib.inv"),
    ),
    "astropy": ("https://docs.astropy.org/en/stable/", None),
}

# -- Sphinx Gallery ------------------------------------------------------------
sphinx_gallery_conf = {
    "backreferences_dir": (Path("generated") / "modules").absolute(),
    "filename_pattern": "^((?!skip_).)*$",
    "examples_dirs": (Path("..") / "examples").absolute(),
    "gallery_dirs": (Path("generated") / "gallery").absolute(),
    "matplotlib_animations": True,
    "default_thumb_file": PNG_ICON,
    "abort_on_example_error": False,
    "plot_gallery": "True",
    "remove_config_comments": True,
    "doc_module": ("mpl_animators"),
    "only_warn_on_example_error": True,
}
