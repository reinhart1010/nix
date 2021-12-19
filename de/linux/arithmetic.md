---
layout: page
title: linux/arithmetic (Deutsch)
description: "Quiz über simple arithmetische Probleme."
content_hash: 38fc3ee3f0fa9b6a9753ff76db7cd9248e2cf154
related_topics:
  - title: English version
    url: /en/linux/arithmetic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arithmetic.html
    icon: bi bi-globe
---
# arithmetic

Quiz über simple arithmetische Probleme.
Mehr Informationen: <https://manpages.debian.org/bsdgames/arithmetic.6.en.html>.

- Starte ein arithmetisches Quiz:

`arithmetic`

- Spezifiziere einen oder mehr arithemtische [O]peratoren um Probleme mit ihnen zu bekommen:

`arithmetic -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|x|/</span>

- Gib eine Reichweite. Additions- und Multiplikationsprobleme werden Zahlen zwischen 0 und der gegebenen Reichweite enthalten. Subtraktionen und Divisionen werden Zahlen zwischen -1 und der gegebenen Reichweite enthalten.

`arithmetic -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
