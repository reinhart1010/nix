---
layout: page
title: common/airodump-ng (Nederlands)
description: "Leg pakketten vast en geef informatie over draadloze netwerken weer."
content_hash: 15e7d187cfa047e43fad8d317ec7b4cf41d63f38
last_modified_at: 2024-03-08
related_topics:
  - title: Deutsch version
    url: /de/common/airodump-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airodump-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airodump-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airodump-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airodump-ng.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airodump-ng

Leg pakketten vast en geef informatie over draadloze netwerken weer.
Deel van `aircrack-ng`.
Meer informatie: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Leg pakketten vast en geef informatie weer over draadloze netwerken op de 2.4GHz band:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Leg pakketten vast en geef informatie weer over draadloze netwerken op de 5GHz band:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` --band a`

- Leg pakketten vast en geef informatie weer over draadloze netwerken op de 2.4GHz en de 5GHz band:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` --band abg`

- Leg pakketten vast en geef informatie weer over een draadloos netwerk met het MAC-adres en kanaal, en sla de uitvoer op in een bestand:

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kanaal</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
