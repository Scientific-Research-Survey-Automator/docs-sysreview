Documentation for SysReview
===========================
.. |build_icon| image:: https://readthedocs.org/projects/sysreview/badge/?version=latest
Build status |build_icon|

Project for maintaining sphinx-docs configuration to generate end-user documentation.
Read the documentation `here <https://docs.readthedocs.io/en/stable/tutorial/>`_


How to build this project?
==========================

Command to build the project:

``sphinx-build -M html docs/source docs/_build/``

To autobuild this project, i.e. auto-reload while making change to the project/files:

``sphinx-autobuild docs/source docs/_build/html``
