---
layout: page
title: freebsd/cal (Nederlands)
description: "Toon een kalender met de huidige dag gemarkeerd."
content_hash: 3d0c4d97b0781b10b63301449a3cd8f59d03915f
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/freebsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

Toon een kalender met de huidige dag gemarkeerd.
Meer informatie: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Toon een kalender voor de huidige maand:

`cal`

- Toon een kalender voor een specifiek jaar:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon een kalender voor een specifieke maand en jaar:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon de volledige kalender voor het huidige jaar:

`cal -y`

- Markeer ([h]) vandaag niet en toon [3] maanden rondom de datum:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon de 2 maanden voor ([B]) en 3 maanden na ([A]) een specifieke [m]aand van het huidige jaar:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>

- Toon [j]ulian dagen (beginnend vanaf één, genummerd vanaf 1 januari):

`cal -j`
