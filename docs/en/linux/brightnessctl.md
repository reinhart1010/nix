---
layout: page
title: linux/brightnessctl (English)
description: "Utility for reading and controlling device brightness for Linux operating systems."
content_hash: 42bcba4fe9cc4954b4eeb83ff623b1abd54c1471
last_modified_at: 2024-01-30
related_topics:
  - title: മലയാളം version
    url: /ml/linux/brightnessctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/brightnessctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brightnessctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brightnessctl

Utility for reading and controlling device brightness for Linux operating systems.
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

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
