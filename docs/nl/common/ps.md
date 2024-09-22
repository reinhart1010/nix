---
layout: page
title: common/ps (Nederlands)
description: "Informatie over actieve processen."
content_hash: 2b6cb6dd6c610203fb36e79c4bb41537931faf61
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ps.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

Informatie over actieve processen.
Meer informatie: <https://manned.org/ps>.

- Toon alle actieve processen:

`ps aux`

- Toon alle actieve processen inclusief de volledige commandoregel:

`ps auxww`

- Zoek naar een proces dat overeenkomt met een string (de vierkante haken voorkomen dat `grep` zichzelf vindt):

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[s]tring</span>

- Toon alle processen van de huidige gebruiker in extra volledig formaat:

`ps --user $(id -u) -F`

- Toon alle processen van de huidige gebruiker als een boomstructuur:

`ps --user $(id -u) f`

- Verkrijg de parent PID van een proces:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Sorteer processen op geheugengebruik:

`ps --sort size`
