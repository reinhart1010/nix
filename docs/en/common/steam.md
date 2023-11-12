---
layout: page
title: common/steam (English)
description: "Video game platform by Valve."
content_hash: c8c088241c66fdd59beb3517acca600a11c36fc9
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/steam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# steam

Video game platform by Valve.
More information: <https://developer.valvesoftware.com/wiki/Command_Line_Options>.

- Launch Steam, printing debug messages to `stdout`:

`steam`

- Launch Steam and enable its in-app debug console tab:

`steam -console`

- Enable and open the Steam console tab in a running Steam instance:

`steam steam://open/console`

- Log into Steam with the specified credentials:

`steam -login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Launch Steam in Big Picture Mode:

`steam -tenfoot`

- Exit Steam:

`steam -shutdown`
