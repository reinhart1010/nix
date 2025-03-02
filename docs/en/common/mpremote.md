---
layout: page
title: common/mpremote (English)
description: "Remotely control MicroPython devices."
content_hash: 6300fec6d861a2d7e7cec7c3c91c93517c8c6c1d
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/mpremote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpremote

Remotely control MicroPython devices.
More information: <https://docs.micropython.org/en/latest/reference/mpremote.html>.

- List all connected MicroPython devices:

`mpremote connect list`

- Open an interactive REPL session with a connected device:

`mpremote connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Run a local script on a connected device:

`mpremote run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>

- Mount a local directory to the device:

`mpremote mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Install a mip package on the device:

`mpremote mip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
