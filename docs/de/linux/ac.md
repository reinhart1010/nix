---
layout: page
title: linux/ac (Deutsch)
description: "Zeigt an, wie lange Benutzer verbunden waren."
content_hash: bf925a15414cae1dc3168cd77b105c273d4cafbf
related_topics:
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
---
# ac

Zeigt an, wie lange Benutzer verbunden waren.
Weitere Informationen: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Zeigt wie viele Stunden der aktuelle Benutzer verbunden war:

`ac`

- Zeigt wie viele Stunden jeder Benutzer verbunden war:

`ac --individual-totals`

- Zeigt wie viele Stunden ein bestimmter Benutzer verbunden war:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nutzername</span>

- Zeigt wie viele Stunden ein bestimmter Benutzer pro Tag verbunden war:

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nutzername</span>

- Zeigt zusätzliche Details:

`ac --compatibility`
