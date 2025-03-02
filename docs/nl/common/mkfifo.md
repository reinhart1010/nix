---
layout: page
title: common/mkfifo (Nederlands)
description: "Maak FIFOs (benoemde pipes)."
content_hash: ae003ef51650230a0947b59f49fcd75ce1dd1a2f
last_modified_at: 2025-03-02
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
  - title: 한국어 version
    url: /ko/common/mkfifo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfifo

Maak FIFOs (benoemde pipes).
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- Maak een benoemde pipe op een opgegeven pad:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>

- Stuur data naar een benoemde pipe en stuur het commando naar de achtergrond:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>` &`

- Ontvang data van benoemde pipe:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>

- Deel je terminal sessie in real-time:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>`; script -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pipe</span>
