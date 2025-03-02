---
layout: page
title: common/picotool (English)
description: "Manage Raspberry Pi Pico boards."
content_hash: 8b6f00d848cb542178b8c7513a22c578eddb8362
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/picotool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# picotool

Manage Raspberry Pi Pico boards.
More information: <https://github.com/raspberrypi/picotool>.

- Display information about the currently loaded program on a Pico:

`picotool info`

- Load a binary onto a Pico:

`picotool load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Convert an ELF or BIN file to UF2:

`picotool uf2 convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/elf_or_bin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>

- Reboot a Pico:

`picotool reboot`

- List all known registers:

`picotool otp list`

- Display version:

`picotool version`

- Display help:

`picotool help`
