---
layout: page
title: netbsd/cal (Nederlands)
description: "Toon een kalender."
content_hash: 7ea8be9ee11f03997afe4af44dbabd943f0321f7
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/netbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/netbsd/cal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cal

Toon een kalender.
Meer informatie: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Toon een kalender voor de huidige maand:

`cal`

- Toon een kalender voor een specifiek jaar:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon een kalender voor een specifieke maand en jaar:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon de volledige kalender voor het huidige jaar door gebruik te maken van [j]ulian dagen  (beginnend vanaf één, genummerd vanaf 1 januari):

`cal -y -j`

- Markeer ([h]) vandaag en toon [3] maanden rondom de datum::

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon de 2 maanden voor ([B]) en 3 maanden na ([A]) een specifieke [m]aand van het huidige jaar:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>

- Toon een specifiek aantal maanden voor en na (Context) de opgegeven maand:

`cal -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maanden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>

- Specificeer de startdag van de week (0: Zondag, 1: Maandag, ..., 6: Zaterdag):

`cal -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..6</span>
