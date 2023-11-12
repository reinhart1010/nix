---
layout: page
title: linux/localectl (English)
description: "Control the system locale and keyboard layout settings."
content_hash: c43969e25c30b2ad0ff1069960bef6df98faf1bd
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/localectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# localectl

Control the system locale and keyboard layout settings.
More information: <https://www.freedesktop.org/software/systemd/man/localectl.html>.

- Show the current settings of the system locale and keyboard mapping:

`localectl`

- List available locales:

`localectl list-locales`

- Set a system locale variable:

`localectl set-locale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LANG</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en_US.UTF-8</span>

- List available keymaps:

`localectl list-keymaps`

- Set the system keyboard mapping for the console and X11:

`localectl set-keymap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us</span>
