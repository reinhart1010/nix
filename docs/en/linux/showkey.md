---
layout: page
title: linux/showkey (English)
description: "Display the keycode of pressed keys on the keyboard, helpful for debugging keyboard-related issues and key remapping."
content_hash: e7f04298cb774c5cd925ceab756c40ffe178a402
last_modified_at: 2024-03-28
tldri18n_status: 2
---
# showkey

Display the keycode of pressed keys on the keyboard, helpful for debugging keyboard-related issues and key remapping.
More information: <https://manned.org/showkey>.

- View keycodes in decimal:

`sudo showkey`

- Display [s]cancodes in hexadecimal:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--scancodes</span>

- Display [k]eycodes in decimal (default):

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keycodes</span>

- Display keycodes in [a]SCII, decimal, and hexadecimal:

`sudo showkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--ascii</span>

- Exit the program:

`Ctrl + d`
