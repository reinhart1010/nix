---
layout: page
title: common/aireplay-ng (Deutsch)
description: "Pakete in ein WLAN injizieren."
content_hash: 92c07dc7a298a8a2bc41b69e110dc449b932b904
last_modified_at: 2023-04-23
related_topics:
  - title: English version
    url: /en/common/aireplay-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aireplay-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aireplay-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aireplay-ng

Pakete in ein WLAN injizieren.
Teil von `aircrack-ng`.
Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Sende eine bestimmten Anzahl an Dissoziation-Paketen mit der MAC-Adresse des Access Points, der MAC-Adresse des Clients und eines Interfaces:

`sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
