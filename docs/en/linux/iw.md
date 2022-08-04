---
layout: page
title: linux/iw (English)
description: "Show and manipulate wireless devices."
content_hash: 8c483ce331e418a42040923a01a9b11314c65079
---
# iw

Show and manipulate wireless devices.
More information: <https://manned.org/iw>.

- Scan for available wireless networks:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` scan`

- Join an open wireless network:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSID</span>

- Close the current connection:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` disconnect`

- Show information about the current connection:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` link`
