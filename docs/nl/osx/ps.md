---
layout: page
title: osx/ps (Nederlands)
description: "Informatie over actieve processen."
content_hash: 75374f58c4ce66951c3c5e735b15e496569ee9f2
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/osx/ps.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

Informatie over actieve processen.
Meer informatie: <https://keith.github.io/xcode-man-pages/ps.1.html>.

- Toon alle actieve processen:

`ps aux`

- Toon alle actieve processen inclusief de volledige opdrachtregel:

`ps auxww`

- Zoek naar een proces dat overeenkomt met een string:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Verkrijg de parent PID van een proces:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Sorteer processen op geheugengebruik:

`ps -m`

- Sorteer processen op CPU-gebruik:

`ps -r`
