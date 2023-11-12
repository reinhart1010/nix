---
layout: page
title: linux/radeontop (English)
description: "Show utilization of AMD GPUs."
content_hash: 20121c8fc8d66434b38cc474fa1159d15e17d6e3
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/radeontop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# radeontop

Show utilization of AMD GPUs.
May require root privileges depending on your system.
More information: <https://github.com/clbr/radeontop>.

- Show the utilization of the default AMD GPU:

`radeontop`

- Enable colored output:

`radeontop --color`

- Select a specific GPU (the bus number is the first number in the output of `lspci`):

`radeontop --bus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus_number</span>

- Specify the display refresh rate (higher means more GPU overhead):

`radeontop --ticks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">samples_per_second</span>
