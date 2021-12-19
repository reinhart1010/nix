---
layout: page
title: linux/vncserver (English)
description: "Launches a VNC (Virtual Network Computing) desktop."
content_hash: 42652ecc585a7b295384a57f1220a2fabaa557d3
---
# vncserver

Launches a VNC (Virtual Network Computing) desktop.

- Launch a VNC Server on next available display:

`vncserver`

- Launch a VNC Server with specific screen geometry:

`vncserver --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>

- Kill an instance of VNC Server running on a specific display:

`vncserver --kill :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display_number</span>
