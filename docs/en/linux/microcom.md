---
layout: page
title: linux/microcom (English)
description: "A minimalistic terminal program, used to access remote devices via a serial, CAN or telnet connection from the console."
content_hash: da27873848b755717586acd1ac76a3ac489d3e2a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# microcom

A minimalistic terminal program, used to access remote devices via a serial, CAN or telnet connection from the console.
More information: <https://manned.org/microcom>.

- Open a serial port using the specified baud rate:

`microcom --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/serial_port</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baud_rate</span>

- Establish a telnet connection to the specified host:

`microcom --telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>
