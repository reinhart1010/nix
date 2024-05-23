---
layout: page
title: linux/xset (English)
description: "User preference utility for X."
content_hash: f59fad4a5d779b956d69f17c652175bbf61cf111
last_modified_at: 2024-05-23
tldri18n_status: 2
---
# xset

User preference utility for X.
More information: <https://manned.org/xset>.

- Disable the screensaver:

`xset s off`

- Disable the bell sound:

`xset b off`

- Set the screensaver to start after 60 minutes of inactivity:

`xset s 3600 3600`

- Disable DPMS (Energy Star) features:

`xset -dpms`

- Enable DPMS (Energy Star) features:

`xset +dpms`

- Query information on any X server:

`xset -display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` q`
