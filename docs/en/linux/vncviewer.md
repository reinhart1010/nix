---
layout: page
title: linux/vncviewer (English)
description: "Launches a VNC (Virtual Network Computing) client."
content_hash: a66f2ffc0deab43c82d15c8f36f4c0378c5a3848
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vncviewer

Launches a VNC (Virtual Network Computing) client.
More information: <https://manned.org/vncviewer>.

- Launch a VNC client which connects to a host on a given display:

`vncviewer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display_number</span>

- Launch in full-screen mode:

`vncviewer -FullScreen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display_number</span>

- Launch a VNC client with a specific screen geometry:

`vncviewer --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display_number</span>

- Launch a VNC client which connects to a host on a given port:

`vncviewer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>
