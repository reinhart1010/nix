---
layout: page
title: linux/wl-paste (English)
description: "Paste content in Wayland clipboard."
content_hash: dfd6f87ee59743ac084b3ecd6a94383d5be24321
last_modified_at: 2024-11-13
related_topics:
  - title: 한국어 version
    url: /ko/linux/wl-paste.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/wl-paste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wl-paste

Paste content in Wayland clipboard.
See also: `wl-copy`, `xclip`.
More information: <https://github.com/bugaevc/wl-clipboard>.

- Paste the contents of the clipboard:

`wl-paste`

- Paste the contents of the primary clipboard (highlighted text):

`wl-paste --primary`

- Write the contents of the clipboard to a file:

`wl-paste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Pipe the contents of the clipboard to a command:

`wl-paste | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
