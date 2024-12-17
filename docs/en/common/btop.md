---
layout: page
title: common/btop (English)
description: "A resource monitor that shows information about the CPU, memory, disks, network and processes."
content_hash: cc78528d566d55fc3a5489a363c7fcd5d0ad63a9
last_modified_at: 2024-12-17
related_topics:
  - title: español version
    url: /es/common/btop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/btop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/btop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/btop.html
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

- Set the update rate to 500 milliseconds:

`btop --update 500`
