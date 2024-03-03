---
layout: page
title: common/btop (English)
description: "A resource monitor that shows information about the CPU, memory, disks, network and processes."
content_hash: 1a36621f076957ccf379d93c50e73673bd8b31fc
last_modified_at: 2024-03-03
related_topics:
  - title: español version
    url: /es/common/btop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/btop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btop

A resource monitor that shows information about the CPU, memory, disks, network and processes.
A C++ version of `bpytop`.
More information: <https://github.com/aristocratos/btop>.

- Start `btop`:

`btop`

- Start `btop` with the specified settings preset:

`btop --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>

- Start `btop` in TTY mode using 16 colors and TTY-friendly graph symbols:

`btop --tty_on`

- Start `btop` in 256-color mode instead of 24-bit color mode:

`btop --low-color`
