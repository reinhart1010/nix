---
layout: page
title: common/f3probe (English)
description: "Probe a block device (e.g. a flash drive or a microSD card) for counterfeit flash memory."
content_hash: 1c523bb87678b0c106b620af1af23848c37162a6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# f3probe

Probe a block device (e.g. a flash drive or a microSD card) for counterfeit flash memory.
See also `f3read`, `f3write`, `f3fix`.
More information: <https://github.com/AltraMayor/f3>.

- Probe a block device:

`sudo f3probe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/block_device</span>

- Use the minimum about of RAM possible:

`sudo f3probe --min-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/block_device</span>

- Time disk operations:

`sudo f3probe --time-ops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/block_device</span>
