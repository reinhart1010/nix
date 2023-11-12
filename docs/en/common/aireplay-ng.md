---
layout: page
title: common/aireplay-ng (English)
description: "Inject packets into a wireless network."
content_hash: 092adbb30ebf937a5a8fbbee335907c9fc953fe7
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aireplay-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aireplay-ng.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aireplay-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aireplay-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aireplay-ng

Inject packets into a wireless network.
Part of `aircrack-ng`.
More information: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Send a specific number of disassociate packets given an access point's MAC address, a client's MAC address and an interface:

`sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
