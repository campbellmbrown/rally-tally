Rally Tally
===========

A table-tennis score taker.

Build Bootloader
----------------

The bootloader can be built with Docker:

.. code-block:: bash

    docker run --rm -v .:/project arm-gcc-builder:latest make -j -C bootloader GNU_INSTALL_ROOT=""

Generate Bootloader Settings
----------------------------

Bootloader settings are generated with:

.. code-block:: bash

    nrfutil settings generate --family NRF52840 --bootloader-version 1 --bl-settings-version 1 bootloader/settings.hex

Merging Softdevice, Bootloader, and Bootloader Settings
-------------------------------------------------------

The Softdevice, Bootloader, and Bootloader Settings can be merged with:

.. code-block:: bash

    mergehex -m bootloader/_build/nrf52840_xxaa_s140.hex bootloader/settings.hex -o bootloader_merged.hex

Flashing the Bootloader
-----------------------

Flash the softdevice, bootloader, and bootloader settings with:

.. code-block:: bash

    nrfjprog -f nrf52 --eraseall
	nrfjprog -f nrf52 --program nrf5_sdk/components/softdevice/s140/hex/s140_nrf52_7.2.0_softdevice.hex --sectorerase
    nrfjprog -f nrf52 --program bootloader_merged.hex --sectorerase
    nrfjprog -f nrf52 --reset

Key Generation
--------------

Bootloader keys are generated with:

.. code-block:: bash

    nrfutil keys generate priv.pem
    nrfutil keys display --key pk --format code priv.pem --out_file bootloader/src/dfu_public_key.c
