---
layout: page
title: linux/betterlockscreen (English)
description: "Simple, minimal lock screen."
content_hash: 3dfc87218fcc7a506b1dd2f03d64249da84326e8
related_topics:
  - title: 中文 version
    url: /zh/linux/betterlockscreen.html
    icon: bi bi-globe
---
# betterlockscreen

Simple, minimal lock screen.
More information: <https://github.com/pavanjadhaw/betterlockscreen>.

- Lock the screen:

`betterlockscreen --lock`

- Change the lock screen background:

`betterlockscreen -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>

- Lock the screen, showing some custom text:

`betterlockscreen -l pixel -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom lock screen text</span>`"`

- Lock the screen, with a custom monitor off timeout in seconds:

`betterlockscreen --off `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l`
