---
layout: page
title: common/mkfifo (Nederlands)
description: "Maak FIFOs (benoemde pipes)."
content_hash: 14acf6d3951c7e1dbce403b0a500439a78185387
last_modified_at: 2024-10-10
related_topics:
  - title: bosanski version
    url: /bs/common/mkfifo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mkfifo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mkfifo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkfifo

Maak FIFOs (benoemde pipes).
Meer informatie: <https://www.gnu.org/software/coreutils/mkfifo>.

- Maak een benoemde pipe op een opgegeven pad:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>

- Stuur data naar een benoemde pipe en stuur het commando naar de achtergrond:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"Hello World"</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>` &`

- Ontvang data van benoemde pipe:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>

- Deel je terminal sessie in real-time:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>`; script -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>
