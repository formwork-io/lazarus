=======
lazarus
=======

A Python library to restart a process when source code changes.

* Free software: Apache License, Version 2.0
* Documentation: http://lazarus.rtfd.org.

Features
--------

* Automatically restart when things change
* Customize when, why, and how restarts happen

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

