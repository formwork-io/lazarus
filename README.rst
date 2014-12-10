=======
Lazarus
=======

.. image:: https://img.shields.io/pypi/v/lazarus.svg
    :target: https://pypi.python.org/pypi/lazarus

.. image:: https://img.shields.io/pypi/l/lazarus.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0.txt

.. image:: https://scrutinizer-ci.com/g/formwork-io/lazarus/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com

.. image:: https://img.shields.io/travis/formwork-io/lazarus.svg
    :target: https://travis-ci.org/formwork-io/lazarus

A Python library to restart the process when source code changes.

* Free software: Apache License, Version 2.0
* Documentation: http://lazarus.rtfd.org.

Features
--------

* Automatically restart when source changes
* Customize when, why, and how restarts happen
* Runs on Linux and Mac

Examples
--------

Restart when any Python module rooted at ``PYTHONPATH`` changes:

.. sourcecode:: python

    >>> import lazarus
    >>> lazarus.default()


Same thing, but within a uWSGI container:

.. sourcecode:: python

    >>> import lazarus
    >>> lazarus.default(restart_func=lambda: uwsgi.reload(), close_fds=False)

