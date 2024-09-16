Rally Tally
===========

A table-tennis score taker.

Key Generation
--------------

Bootloader keys are generated with:

.. code-block:: bash

    nrfutil keys generate priv.pem
    nrfutil keys display --key pk --format code priv.pem --out_file bootloader/src/dfu_public_key.c
