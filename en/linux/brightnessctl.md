---
layout: page
title: linux/brightnessctl (English)
description: "Utility for reading and controlling device brightness for GNU/Linux operating systems."
content_hash: ff9a9f7a3d642fd690bdd5ee4d4a09851f0adcb1
related_topics:
  - title: 中文 version
    url: /zh/linux/brightnessctl.html
    icon: bi bi-globe
---
# brightnessctl

Utility for reading and controlling device brightness for GNU/Linux operating systems.
More information: <https://github.com/Hummer12007/brightnessctl>.

- List devices with changeable brightness:

`brightnessctl --list`

- Print the current brightness of the display backlight:

`brightnessctl get`

- Set the brightness of the display backlight to a specified percentage within range:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>

- Increase brightness by a specified increment:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+10%</span>

- Decrease brightness by a specified decrement:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10%</span>
