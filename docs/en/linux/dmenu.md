---
layout: page
title: linux/dmenu (English)
description: "Dynamic menu."
content_hash: 958f476d88f41d2ceb4f51e0f804bb3e3d466687
last_modified_at: 2024-04-18
related_topics:
  - title: 中文 version
    url: /zh/linux/dmenu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmenu

Dynamic menu.
Create a menu from a text input with each item on a new line.
More information: <https://manned.org/dmenu>.

- Display a menu of the output of the `ls` command:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | dmenu`

- Display a menu with custom items separated by a new line (`\n`):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`" | dmenu`

- Let the user choose between multiple items and save the selected one to a file:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`" | dmenu > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color.txt</span>

- Launch dmenu on a specific monitor:

`ls | dmenu -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Display dmenu at the bottom of the screen:

`ls | dmenu -b`
