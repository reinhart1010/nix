---
layout: page
title: linux/setserial (English)
description: "Read and modify serial port information."
content_hash: 20e2bba0bdce03192d77f0963e251703d497fe60
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# setserial

Read and modify serial port information.
More information: <https://manned.org/setserial>.

- Print all information about a specific serial device:

`setserial -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cuaN</span>

- Print the configuration summary of a specific serial device (useful for printing during bootup process):

`setserial -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Set a specific configuration parameter to a device:

`sudo setserial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameter</span>

- Print the configuration of a list of devices:

`setserial -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device1 device2 ...</span>
