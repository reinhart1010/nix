---
layout: page
title: linux/vncserver (English)
description: "Launch a VNC (Virtual Network Computing) desktop."
content_hash: 2ab527ef9da68fd3545edd74fb80e406f16798d6
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# vncserver

Launch a VNC (Virtual Network Computing) desktop.
More information: <https://manned.org/vncserver.1x>.

- Launch a VNC Server on next available display:

`vncserver`

- Launch a VNC Server with specific screen geometry:

`vncserver --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>

- Kill an instance of VNC Server running on a specific display:

`vncserver --kill :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display_number</span>
