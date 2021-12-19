---
layout: page
title: common/circup (English)
description: "The CircuitPython library updater."
content_hash: 390837c78ca5089814a7306f7bdeeb86c167a53b
---
# circup

The CircuitPython library updater.
More information: <https://github.com/adafruit/circup>.

- Interactively update modules on a device:

`circup update`

- Install a new library:

`circup install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library_name</span>

- Search for a library:

`circup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partial_name</span>

- List all libraries on a connected device in `requirements.txt` format:

`circup freeze`

- Save all libraries on a connected device in the current directory:

`circup freeze -r`
