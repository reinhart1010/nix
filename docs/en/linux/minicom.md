---
layout: page
title: linux/minicom (English)
description: "A program to communicate with the serial interface of a device."
content_hash: 9fdae2f8db1956451b48237b67d2a01d5f3d4c1a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# minicom

A program to communicate with the serial interface of a device.
More information: <https://manned.org/minicom>.

- Open a given serial port:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>

- Open a given serial port with a given baud rate:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --baudrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- Enter the configuration menu before communicating with a given serial port:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --setup`
