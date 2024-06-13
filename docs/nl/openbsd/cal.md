---
layout: page
title: openbsd/cal (Nederlands)
description: "Toon een kalender met de huidige dag gemarkeerd."
content_hash: 5712b1fca13829d77e34a6a313af1263143b9ed0
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/openbsd/cal.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

Toon een kalender met de huidige dag gemarkeerd.
Meer informatie: <https://man.openbsd.org/cal>.

- Toon een kalender voor de huidige maand:

`cal`

- Toon een kalender voor een specifiek jaar:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon een kalender voor een specifieke maand en jaar:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon de volledige kalender voor het huidige jaar ([y]):

`cal -y`

- Toon [j]ulian dagen (beginnend vanaf één, genummerd vanaf 1 januari):

`cal -j`

- Gebruik [m]aandag als week start in plaats van zondag:

`cal -m`

- Toon [w]eeknummers (niet compatibel met `-j`):

`cal -w`
