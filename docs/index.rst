***************************
mpl-animators Documentation
***************************

The ``mpl_animators`` package provides a set of classes which allow the easy construction of interactive `matplotlib` widget based animations.
"Out of the box" classes are provided for making line or image plots from numpy arrays, with sliders to control the animation automatically added for all dimensions not on the axes of the plot.
As well as this there is a specialised `.ArrayAnimatorWCS` class which can make line or image plots for a numpy array and associated World Coordinate System (WCS) object from `astropy`.
Finally, there are two base classes: `.BaseFuncAnimator` which can be extended to generate an interactive visualization from any data structure and set of functions to update the plot, and `.ArrayAnimator` which can be extended to generate any visualisation based on the axes of a numpy array.


.. automodapi:: mpl_animators

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
