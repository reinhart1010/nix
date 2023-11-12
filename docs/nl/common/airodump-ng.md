---
layout: page
title: common/airodump-ng (Nederlands)
description: "Leg pakketten vast en geef informatie over draadloze netwerken weer."
content_hash: 82abd4458705d4532c3824eab752285384ba651b
last_modified_at: 2023-11-12
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
  - title: 中文 version
    url: /zh/common/airodump-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airodump-ng

Leg pakketten vast en geef informatie over draadloze netwerken weer.
Deel van `aircrack-ng`.
Meer informatie: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Leg pakketten vast en geef informatie weer over een draadloos netwerk:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Leg pakketten vast en geef informatie weer over een draadloos netwerk met het MAC-adres en kanaal, en sla de uitvoer op in een bestand:

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kanaal</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
