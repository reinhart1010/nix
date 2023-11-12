---
layout: page
title: linux/xbacklight (English)
description: "Utility to adjust backlight brightness using the RandR extension."
content_hash: 5de7c1fa2a65a56fa23e00ac1d512f94b9e88a8a
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/xbacklight.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbacklight

Utility to adjust backlight brightness using the RandR extension.
More information: <https://gitlab.freedesktop.org/xorg/app/xbacklight>.

- Get the current screen brightness as a percentage:

`xbacklight`

- Set the screen brightness to 40%:

`xbacklight -set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>

- Increase current brightness by 25%:

`xbacklight -inc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- Decrease current brightness by 75%:

`xbacklight -dec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>

- Increase backlight to 100%, over 60 seconds (value given in ms), using 60 steps:

`xbacklight -set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60000</span>` -steps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>
