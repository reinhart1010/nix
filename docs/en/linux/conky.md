---
layout: page
title: linux/conky (English)
description: "Light-weight system monitor for X."
content_hash: c3d81353d78cb50358bb0ce0b2bab64742009e69
last_modified_at: 2024-01-25
related_topics:
  - title: català version
    url: /ca/linux/conky.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/conky.html
    icon: bi bi-globe
tldri18n_status: 2
---
# conky

Light-weight system monitor for X.
More information: <https://github.com/brndnmtthws/conky>.

- Launch with default, built-in config:

`conky`

- Create a new default config:

`conky -C > ~/.conkyrc`

- Launch Conky with a given configuration file:

`conky -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config</span>

- Start in the background (daemonize):

`conky -d`

- Align Conky on the desktop:

`conky -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|bottom|middle</span>`_`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left|right|middle</span>

- Pause for 5 seconds at startup before launching:

`conky -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
