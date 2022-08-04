---
layout: page
title: linux/vncserver (English)
description: "Launches a VNC (Virtual Network Computing) desktop."
content_hash: 87119361e28ee6e348a2a814505ab68b86589e42
---
# vncserver

Launches a VNC (Virtual Network Computing) desktop.
More information: <https://manned.org/vncserver.1x>.

- Launch a VNC Server on next available display:

`vncserver`

- Launch a VNC Server with specific screen geometry:

`vncserver --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>

- Kill an instance of VNC Server running on a specific display:

`vncserver --kill :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display_number</span>
