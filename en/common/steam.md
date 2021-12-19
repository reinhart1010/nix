---
layout: page
title: common/steam (English)
description: "Video game platform by Valve."
content_hash: a401791310d83558824589f0b3da68bf3a4f42d6
---
# steam

Video game platform by Valve.
More information: <https://developer.valvesoftware.com/wiki/Command_Line_Options#Steam_.28Windows.29>.

- Launch Steam, printing debug messages to stdout:

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
