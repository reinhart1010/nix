---
layout: page
title: common/solo (English)
description: "Interact with Solo hardware security keys."
content_hash: e55656597c4f249642af429a46703f46d464d9d9
---
# solo

Interact with Solo hardware security keys.
More information: <https://github.com/solokeys/solo-python>.

- List connected Solos:

`solo ls`

- Update the currently connected Solo's firmware to the latest version:

`solo key update`

- Blink the LED of a specific Solo:

`solo key wink --serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serial_number</span>

- Generate random bytes using the currently connected Solo's secure random number generator:

`solo key rng raw`

- Monitor the serial output of a Solo:

`solo monitor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/serial_port</span>
