---
layout: page
title: linux/bspc (English)
description: "Configure and control `bspwm`, managing nodes, desktops, monitors, and more."
content_hash: 002d18eba519a834f3e1cccb8b3f6c8afdbb5da2
last_modified_at: 2024-02-25
related_topics:
  - title: Nederlands version
    url: /nl/linux/bspc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bspc

Configure and control `bspwm`, managing nodes, desktops, monitors, and more.
See also: `bspwm`.
More information: <https://github.com/baskerville/bspwm>.

- Define two virtual desktops:

`bspc monitor --reset-desktops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">desktop_name1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">desktop_name2</span>

- Focus the given desktop:

`bspc desktop --focus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Close the windows rooted at the selected node:

`bspc node --close`

- Send the selected node to the given desktop:

`bspc node --to-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Toggle full screen mode for the selected node:

`bspc node --state ~fullscreen`

- Set the value of a specific setting:

`bspc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setting_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
