---
layout: page
title: common/ack (norsk bokmål (Norge))
description: "Et søkeverktøy som grep, optimalisert for utviklere."
content_hash: ecc6631ee39b4325a737d16bac89820fa355b790
related_topics:
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
---
# ack

Et søkeverktøy som grep, optimalisert for utviklere.
Se også: `rg`, som er mye raskere.
Mer informasjon: <https://beyondgrep.com/documentation>.

- Søk etter filer som inneholder en streng eller regulært uttrykk i gjeldende katalog rekursivt:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søkemønster</span>`"`

- Søk etter et mønster som ikke skiller mellom store og små bokstaver:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søkemønster</span>`"`

- Søk etter linjer som samsvarer med et mønster, skriv ut bare den samsvarende teksten og ikke resten av linjen:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søkemønster</span>`"`

- Begrens søket til filer av en bestemt type:

`ack --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søkemønster</span>`"`

- Ikke søk i filer av en bestemt type:

`ack --type=no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søkemønster</span>`"`

- Tell totalt antall treff funnet:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søkemønster</span>`"`

- Skriv ut filnavnene og antall treff kun for hver fil:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søkemønster</span>`"`

- List opp alle verdiene som kan brukes med  `--type`:

`ack --help-types`
