---
layout: page
title: linux/beep (Deutsch)
description: "Ein Befehl, um den PC-Lautsprecher zu steuern."
content_hash: ef6117602403fa12f4338efccb306a81494dfae5
related_topics:
  - title: English version
    url: /en/linux/beep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/beep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/beep.html
    icon: bi bi-globe
---
# beep

Ein Befehl, um den PC-Lautsprecher zu steuern.
Weitere Informationen: <https://github.com/spkr-beep/beep>.

- Gib einen Ton aus:

`beep`

- Gib einen Ton mehrmals aus:

`beep -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wiederholungen</span>

- Gib einen Ton mit einer bestimmten Frequenz (Hz) und Länge (Millisekunden) aus:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequenz</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">länge</span>

- Spiele jede neue Frequenz und Länge als einen eigenen Ton:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequenz</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">länge</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequenz</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">länge</span>

- Spiele die C-Dur-Tonleiter:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">262</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">294</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">330</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">349</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">392</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">440</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">494</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">523</span>
