---
layout: page
title: linux/radeontop (English)
description: "Show utilisation of AMD GPUs."
content_hash: 2bdbe1d3838582f9d0a9fe37d59940512ac5299e
related_topics:
  - title: italiano version
    url: /it/linux/radeontop.html
    icon: bi bi-globe
---
# radeontop

Show utilisation of AMD GPUs.
May require root privileges depending on your system.
More information: <https://github.com/clbr/radeontop>.

- Show the utilisation of the default AMD GPU:

`radeontop`

- Enable colored output:

`radeontop --color`

- Select a specific GPU (the bus number is the first number in the output of `lspci`):

`radeontop --bus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus_number</span>

- Specify the display refresh rate (higher means more GPU overhead):

`radeontop --ticks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">samples_per_second</span>
