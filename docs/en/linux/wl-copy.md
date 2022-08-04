---
layout: page
title: linux/wl-copy (English)
description: "Wayland clipboard manipulation tool."
content_hash: 9acd7ef7ce26cb08a9007599647f806592749a80
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

- Clear the clipboard:

`wl-copy --clear`
