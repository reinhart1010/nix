---
layout: page
title: common/airodump-ng (English)
description: "Capture packets and display information about wireless networks."
content_hash: 74b82b9e3b9258a4dcb13bccccf103cd1993c59c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/airodump-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airodump-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airodump-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airodump-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airodump-ng

Capture packets and display information about wireless networks.
Part of `aircrack-ng`.
More information: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Capture packets and display information about a wireless network:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Capture packets and display information about a wireless network given the MAC address and channel, and save the output to a file:

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
