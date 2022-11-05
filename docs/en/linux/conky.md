---
layout: page
title: linux/conky (English)
description: "Light-weight system monitor for X."
content_hash: 9b98033f6018a534e7d84272d131aaa51ba6bbae
related_topics:
  - title: català version
    url: /ca/linux/conky.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/conky.html
    icon: bi bi-globe
---
# conky

Light-weight system monitor for X.
More information: <https://github.com/brndnmtthws/conky>.

- Launch with default, built-in config:

`conky`

- Create a new default config:

`conky -C > ~/.conkyrc`

- Launch Conky with a given config file:

`conky -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config</span>

- Start in the background (daemonize):

`conky -d`

- Align Conky on the desktop:

`conky -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|bottom|middle</span>`_`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left|right|middle</span>

- Pause for 5 seconds at startup before launching:

`conky -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
