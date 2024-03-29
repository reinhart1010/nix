---
layout: page
title: common/pio-device (English)
description: "Manage and monitor PlatformIO devices."
content_hash: 04e7f90e6507926f7db4b5593a8bf8d0b9d41169
last_modified_at: 2023-12-29
related_topics:
  - title: Nederlands version
    url: /nl/common/pio-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio device

Manage and monitor PlatformIO devices.
More information: <https://docs.platformio.org/en/latest/core/userguide/device/>.

- List all available serial ports:

`pio device list`

- List all available logical devices:

`pio device list --logical`

- Start an interactive device monitor:

`pio device monitor`

- Start an interactive device monitor and listen to a specific port:

`pio device monitor --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSBX</span>

- Start an interactive device monitor and set a specific baud rate (defaults to 9600):

`pio device monitor --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">57600</span>

- Start an interactive device monitor and set a specific EOL character (defaults to `CRLF`):

`pio device monitor --eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CRLF|CR|LF</span>

- Go to the menu of the interactive device monitor:

`<Ctrl> + T`
