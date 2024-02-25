---
layout: page
title: linux/minicom (English)
description: "Communicate with the serial interface of a device."
content_hash: dae12ad879d493a50ab5cb8d58077f9258afd5f5
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# minicom

Communicate with the serial interface of a device.
More information: <https://manned.org/minicom>.

- Open a given serial port:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>

- Open a given serial port with a given baud rate:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --baudrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- Enter the configuration menu before communicating with a given serial port:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --setup`
