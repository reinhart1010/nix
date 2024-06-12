---
layout: page
title: linux/showkey (English)
description: "Display the keycode of pressed keys on the keyboard, helpful for debugging keyboard-related issues and key remapping."
content_hash: e24572aca932d0b81b96259ad851564f96d13fdb
last_modified_at: 2024-06-12
related_topics:
  - title: español version
    url: /es/linux/showkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# showkey

Display the keycode of pressed keys on the keyboard, helpful for debugging keyboard-related issues and key remapping.
More information: <https://manned.org/showkey>.

- View keycodes in decimal:

`sudo showkey`

- Display scancodes in hexadecimal:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--scancodes</span>

- Display keycodes in decimal (default):

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keycodes</span>

- Display keycodes in ASCII, decimal, and hexadecimal:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--ascii</span>

- Exit the program:

`Ctrl + d`
