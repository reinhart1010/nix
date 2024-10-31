---
layout: page
title: common/iproxy (English)
description: "A proxy that binds local TCP ports to be forwarded to the specified ports on a usbmux device."
content_hash: 9e95041d4842e3b13f2080e1cd03bdd40f7f78bd
last_modified_at: 2024-10-31
tldri18n_status: 2
---
# iproxy

A proxy that binds local TCP ports to be forwarded to the specified ports on a usbmux device.
More information: <https://manned.org/iproxy>.

- Bind a local TCP port and forward it to a port on the connected USB device:

`iproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_port</span>

- Bind multiple local TCP ports and forward them to the respective ports on the connected USB device:

`iproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_port1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_port2</span>

- Bind a local port and forward it to a specific device by UDID:

`iproxy --udid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_udid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_port</span>

- Bind a local port and forward it to a network-connected device with WiFi sync enabled:

`iproxy --network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_port</span>
