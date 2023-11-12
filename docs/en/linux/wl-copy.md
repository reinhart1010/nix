---
layout: page
title: linux/wl-copy (English)
description: "Wayland clipboard manipulation tool."
content_hash: 42a9b5c0a967dbce00620fc7517e0feff98ff4c6
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/linux/wl-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wl-copy

Wayland clipboard manipulation tool.
See also: `wl-paste`.
More information: <https://github.com/bugaevc/wl-clipboard>.

- Copy the text to the clipboard:

`wl-copy "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`"`

- Pipe the command (`ls`) output to the clipboard:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | wl-copy`

- Copy for only one paste and then clear it:

`wl-copy --paste-once "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`"`

- Copy an image:

`wl-copy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Clear the clipboard:

`wl-copy --clear`
