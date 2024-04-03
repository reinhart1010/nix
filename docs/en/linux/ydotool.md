---
layout: page
title: linux/ydotool (English)
description: "Control keyboard and mouse inputs via commands in a way that is display server agnostic."
content_hash: 103e4d2ceab5133284641ffa2e4c3c936baa1bff
last_modified_at: 2024-04-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ydotool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ydotool

Control keyboard and mouse inputs via commands in a way that is display server agnostic.
More information: <https://github.com/ReimuNotMoe/ydotool>.

- Start the ydotool daemon in the background:

`ydotoold`

- Perform a left click input:

`ydotool click 0xC0`

- Perform a right click input:

`ydotool click 0xC1`

- Input Alt+F4:

`ydotool key 56:1 62:1 62:0 56:0`
