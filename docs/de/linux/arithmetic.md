---
layout: page
title: linux/arithmetic (Deutsch)
description: "Quiz über simple arithmetische Probleme."
content_hash: 6c0544f6e3d61435b7f70200eff440cd572127a2
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/arithmetic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arithmetic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arithmetic

Quiz über simple arithmetische Probleme.
Weitere Informationen: <https://manned.org/arithmetic.6>.

- Starte ein arithmetisches Quiz:

`arithmetic`

- Spezifiziere einen oder mehr arithmetische [O]peratoren um Probleme mit ihnen zu bekommen:

`arithmetic -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|x|/</span>

- Gib eine Reichweite. Additions- und Multiplikationsprobleme werden Zahlen zwischen 0 und der gegebenen Reichweite enthalten. Subtraktionen und Divisionen werden Zahlen zwischen -1 und der gegebenen Reichweite enthalten:

`arithmetic -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
