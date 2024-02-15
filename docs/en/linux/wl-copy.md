---
layout: page
title: linux/wl-copy (English)
description: "Clear and copy to Wayland clipboard."
content_hash: 8e5736e7d4f7ce7a9ca813eab2123a3cdd5fa286
last_modified_at: 2024-02-15
related_topics:
  - title: Türkçe version
    url: /tr/linux/wl-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wl-copy

Clear and copy to Wayland clipboard.
See also: `wl-paste`, `xclip`.
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
