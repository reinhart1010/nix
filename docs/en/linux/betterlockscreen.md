---
layout: page
title: linux/betterlockscreen (English)
description: "Simple, minimal lock screen."
content_hash: c62465c723a105c33331e509bfbf63074c95d877
last_modified_at: 2024-10-13
related_topics:
  - title: 中文 version
    url: /zh/linux/betterlockscreen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# betterlockscreen

Simple, minimal lock screen.
More information: <https://github.com/betterlockscreen/betterlockscreen>.

- Lock the screen:

`betterlockscreen --lock`

- Change the lock screen background:

`betterlockscreen -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>

- Lock the screen, showing some custom text:

`betterlockscreen -l pixel -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom lock screen text</span>`"`

- Lock the screen, with a custom monitor off timeout in seconds:

`betterlockscreen --off `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l`
