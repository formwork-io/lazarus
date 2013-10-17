=======
lazarus
=======

.. image:: https://badge.fury.io/py/lazarus.png
    :target: http://badge.fury.io/py/lazarus

.. image:: https://travis-ci.org/nbargnesi/lazarus.png?branch=master
        :target: https://travis-ci.org/nbargnesi/lazarus

.. image:: https://pypip.in/d/lazarus/badge.png
        :target: https://crate.io/packages/lazarus?version=latest


A Python library to restart a process when source code changes.

* Free software: Apache License, Version 2.0
* Documentation: http://lazarus.rtfd.org.

Features
--------

* Automatically restart when things change
* Customize when, why, and how restarts happen

Example
-------

Restart when any Python module rooted at ``PYTHONPATH`` changes:

.. sourcecode:: python

    >>> import lazarus
    >>> lazarus.default()
