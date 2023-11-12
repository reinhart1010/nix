---
layout: page
title: linux/ac (Deutsch)
description: "Zeigt an, wie lange Benutzer verbunden waren."
content_hash: 3d87b369a16af4f6e357ecd61af968f084856642
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ac

Zeigt an, wie lange Benutzer verbunden waren.
Weitere Informationen: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Zeige, wie viele Stunden der aktuelle Benutzer verbunden war:

`ac`

- Zeige, wie viele Stunden jeder Benutzer verbunden war:

`ac --individual-totals`

- Zeige, wie viele Stunden ein bestimmter Benutzer verbunden war:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nutzername</span>

- Zeige, wie viele Stunden ein bestimmter Benutzer pro Tag verbunden war:

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nutzername</span>

- Zeige zusätzliche Details:

`ac --compatibility`
