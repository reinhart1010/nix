---
layout: page
title: common/yes (Nederlands)
description: "Iets herhaaldelijk uitvoeren."
content_hash: 9eb1cafe51233b7bbc01b57dc79f9c560a848826
last_modified_at: 2024-02-15
related_topics:
  - title: English version
    url: /en/common/yes.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/yes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/yes.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/yes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/yes.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/yes.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yes

Iets herhaaldelijk uitvoeren.
Deze opdracht wordt vaak gebruikt om ja te beantwoorden op elke prompt door installatieopdrachten (zoals apt-get).
Meer informatie: <https://www.gnu.org/software/coreutils/yes>.

- Print herhaaldelijk "bericht":

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bericht</span>

- Print herhaaldelijk "y":

`yes`

- Accepteer alles wat wordt gevraagd door het commando `apt-get`:

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Print herhaaldelijk een nieuwe regel om altijd de standaard optie van een vraag te accepteren:

`yes ''`
