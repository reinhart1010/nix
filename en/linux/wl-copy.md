---
layout: page
title: linux/wl-copy (English)
description: "Wayland clipboard manipulation tool."
content_hash: 4066ca067620abe72b0e18093be375772c2b18f0
---
# wl-copy

Wayland clipboard manipulation tool.
See also: `wl-paste`.
More information: <https://github.com/bugaevc/wl-clipboard>.

- Copy text to the clipboard:

`wl-copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Copy the output of a command to the clipboard:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | wl-copy`

- Copy for only one paste and then clear it:

`wl-copy --paste-once`

- Clear the clipboard:

`wl-copy --clear`
