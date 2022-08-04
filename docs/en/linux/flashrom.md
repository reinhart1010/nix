---
layout: page
title: linux/flashrom (English)
description: "Read, write, verify and erase flash chips."
content_hash: c9deaa661806596bea1e475a55828537bc130027
---
# flashrom

Read, write, verify and erase flash chips.
More information: <https://manned.org/flashrom>.

- Probe the chip, ensuring the wiring is correct:

`flashrom --programmer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>

- Read flash and save it to a file:

`flashrom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>` --read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Write a file to the flash:

`flashrom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Verify the flash against a file:

`flashrom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>` --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Probe the chip using Raspberry Pi:

`flashrom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux_spi:dev=/dev/spidev0.0</span>
