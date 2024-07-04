# Licensed under a 3-clause BSD style license - see LICENSE.rst
from mpl_animators.base import BaseFuncAnimator, ArrayAnimator
from mpl_animators.image import ImageAnimator
from mpl_animators.line import LineAnimator
from mpl_animators.wcs import ArrayAnimatorWCS

from .version import __version__

__all__ = ["ArrayAnimator", "BaseFuncAnimator", "LineAnimator", "ArrayAnimatorWCS", "ImageAnimator", "__version__"]
