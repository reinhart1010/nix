---
layout: page
title: common/airodump-ng (Deutsch)
description: "Erfasst Pakete und zeigt Informationen über drahtlose Netzwerke an."
content_hash: 3f8d850fc85652fbe1003e8cc2579eb99d46503b
last_modified_at: 2023-04-23
related_topics:
  - title: English version
    url: /en/common/airodump-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airodump-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airodump-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airodump-ng

Erfasst Pakete und zeigt Informationen über drahtlose Netzwerke an.
Teil von `aircrack-ng`.
Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Erfasse Pakete und zeige Informationen über ein drahtloses Netzwerk an:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Erfasse Pakete und zeige Informationen über ein drahtloses Netzwerk anhand der MAC-Adresse und des Kanals an, und schreibe diese in eine Datei:

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kanal</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
