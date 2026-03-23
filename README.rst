``mpl-animators``
=================

An interactive animation framework for matplotlib.

It is designed to handle N-dimensional data, and can be used to create animations.

This package has been spun out of ``sunpy`` to be more generally useful.

Testing and CI Notes
--------------------

Because this repo is heavily dependent on figure tests, most of the CI jobs
(other than publish, and one windows and one macos build) run on Circle CI,
there are no test runs on GH Actions. The `-figure` test tox jobs run all tests,
figure and non-figure.

Usage of Generative AI
----------------------

We expect authentic engagement in our community.
**Do not post the output from Large Language Models or similar generative AI as code, issues or comments on GitHub or any other platform.**
If you use generative AI tools as an aid in developing code or documentation changes, ensure that you fully understand the proposed changes and can explain why they are the correct approach and an improvement to the current state.
For more information see our documentation on fair and appropriate `AI usage <https://docs.sunpy.org/en/latest/dev_guide/contents/ai_usage.html>`__.

Contributing
------------

We love contributions! mpl-animators is open source,
built on open source, and we'd love to have you hang out in our community.

If you would like to get involved, check out the `Developers Guide`_ section of the SunPy docs.
Stop by our chat room `#sunpy:openastronomy.org`_ if you have any questions.
Help is always welcome so let us know what you like to work on, or check out the `issues page`_ for the list of known outstanding items.

For more information on contributing to SunPy, please read our `Newcomers' guide`_.

.. _Developers Guide: https://docs.sunpy.org/en/latest/dev_guide/index.html
.. _`#sunpy:openastronomy.org`: https://app.element.io/#/room/#sunpy:openastronomy.org
.. _issues page: https://github.com/sunpy/mpl-animators/issues
.. _Newcomers' guide: https://docs.sunpy.org/en/latest/dev_guide/contents/newcomers.html

When you are interacting with the SunPy community you are asked at to follow our `code of conduct <https://sunpy.org/coc>`__.
