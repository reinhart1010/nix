---
layout: page
title: linux/cu (English)
description: "Call Up another system and act as a dial-in/serial terminal or perform file transfers with no error checking."
content_hash: fee71a29bd7addb675b1dfe04a8c434eb360cbf5
last_modified_at: 2024-08-12
tldri18n_status: 2
---
# cu

Call Up another system and act as a dial-in/serial terminal or perform file transfers with no error checking.
More information: <https://manned.org/cu>.

- Open a given serial port:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>

- Open a given serial port with a given baud rate:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- Open a given serial port with a given baud rate and echo characters locally (half-duplex mode):

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>` --halfduplex`

- Open a given serial port with a given baud rate, parity, and no hardware or software flow control:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>` --parity=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">even|odd|none</span>` --nortscts --nostop`

- Exit the `cu` session when in connection:

`~.`
