---
layout: page
title: linux/flameshot (English)
description: "Screenshot utility with a GUI."
content_hash: 3da9c3b3823c06f32ff4fd61dcef6ad25a39aa27
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/flameshot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flameshot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flameshot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flameshot

Screenshot utility with a GUI.
Supports basic image editing, such as text, shapes, colors, and imgur.
More information: <https://flameshot.org>.

- Create a fullscreen screenshot:

`flameshot full`

- Create a screenshot interactively:

`flameshot gui`

- Create a screenshot and save it to a specific path:

`flameshot gui --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create a screenshot interactively in a simplified mode:

`flameshot launcher`

- Create a screenshot from a specific monitor:

`flameshot screen --number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Create a screenshot and print it to `stdout`:

`flameshot gui --raw`

- Create a screenshot and copy it to the clipboard:

`flameshot gui --clipboard`

- Create a screenshot with a specific delay in milliseconds:

`flameshot full --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>
