---
layout: page
title: common/f3probe (English)
description: "Probe a block device (e.g. a flash drive or a microSD card) for counterfeit flash memory."
content_hash: 99b1355b7a3c35bcf1b079ecf6e237b00a52a6af
last_modified_at: 2023-11-23
tldri18n_status: 2
---
# f3probe

Probe a block device (e.g. a flash drive or a microSD card) for counterfeit flash memory.
See also: `f3read`, `f3write`, `f3fix`.
More information: <https://github.com/AltraMayor/f3>.

- Probe a block device:

`sudo f3probe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/block_device</span>

- Use the minimum about of RAM possible:

`sudo f3probe --min-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/block_device</span>

- Time disk operations:

`sudo f3probe --time-ops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/block_device</span>
