whatisthis
==========

UI for manual image classification

Installation
------------

.. code:: bash

    pip install whatisthis

Usage
-----

.. code:: python

    from whatisthis import create_server

    def emitter(image, tag):
        print(image, tag)

    create_server(
        emitter=emitter,
        images=images,
        categories=categories
        port=8081)
