---
layout: page
title: linux/cbatticon (English)
description: "A lightweight and fast battery icon that sits in your system tray."
content_hash: c79e1ac114bf98ff038e4019fa9c7819dac50fa7
last_modified_at: 2023-11-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cbatticon

A lightweight and fast battery icon that sits in your system tray.
More information: <https://github.com/valr/cbatticon>.

- Show the battery icon in the system tray:

`cbatticon`

- Show the battery icon and set the update interval to 20 seconds:

`cbatticon --update-interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- List available icon types:

`cbatticon --list-icon-types`

- Show the battery icon with a specific icon type:

`cbatticon --icon-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard|notification|symbolic</span>

- List available power supplies:

`cbatticon --list-power-supplies`

- Show the battery icon for a specific battery:

`cbatticon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BAT0</span>

- Show the battery icon and which command to execute when the battery level reaches the set critical level:

`cbatticon --critical-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` --command-critical-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poweroff</span>
