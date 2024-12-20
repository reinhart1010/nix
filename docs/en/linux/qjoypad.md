---
layout: page
title: linux/qjoypad (English)
description: "Translate input from gamepads or joysticks into keyboard strokes or mouse actions."
content_hash: 712bc28105a2273b22eb244108a3148359d15044
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# qjoypad

Translate input from gamepads or joysticks into keyboard strokes or mouse actions.
More information: <https://qjoypad.sourceforge.net/>.

- Start QJoyPad:

`qjoypad`

- Start QJoyPad and look for devices in a specific directory:

`qjoypad --device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Start QJoyPad but don't show a system tray icon:

`qjoypad --notray`

- Start QJoyPad and force the window manager to use a system tray icon:

`qjoypad --force-tray`

- Force a running instance of QJoyPad to update its list of devices and layouts:

`qjoypad --update`

- Load the given layout in an already running instance of QJoyPad, or start QJoyPad using the given layout:

`qjoypad "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layout</span>`"`
