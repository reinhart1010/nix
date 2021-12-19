---
layout: page
title: linux/flameshot (English)
description: "Screenshot utility with a GUI."
content_hash: 6b1d1ae2274baf5c8124de9180a6bba4910fee52
related_topics:
  - title: français version
    url: /fr/linux/flameshot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flameshot.html
    icon: bi bi-globe
---
# flameshot

Screenshot utility with a GUI.
Supports basic image editing, such as text, shapes, colors, and imgur.
More information: <https://flameshot.org>.

- Launch flameshot with a simpler interactive mode:

`flameshot launcher`

- Launch flameshot and immediately start interactively annotating parts of the screen to screenshot:

`flameshot gui`

- Take a full screenshot (all monitors):

`flameshot full`

- Take a screenshot from monitor 1:

`flameshot screen --number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Set the save path to write screenshots to:

`flameshot full --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Delay the screenshot for N milliseconds and output to clipboard:

`flameshot full --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2000</span>` --clipboard`

- Take a screenshot and export it to standard-output:

`flameshot gui --raw`
