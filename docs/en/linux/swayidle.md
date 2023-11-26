---
layout: page
title: linux/swayidle (English)
description: "Idle management daemon for Wayland."
content_hash: 28c0e5dfaaf6e5daae25580c22c8488239fe4999
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# swayidle

Idle management daemon for Wayland.
Note: the configuration options are documented in its man page.
More information: <https://github.com/swaywm/swayidle/blob/master/swayidle.1.scd>.

- Listen for idle activity using the configuration in `$XDG_CONFIG_HOME/swayidle/config` or `$HOME/swayidle/config`:

`swayidle`

- Specify an alternative path to the configuration file:

`swayidle -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
