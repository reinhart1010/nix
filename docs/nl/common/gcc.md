---
layout: page
title: common/gcc (Nederlands)
description: "Preprocess en compileer C en C++ bronbestanden, monteer en koppel ze vervolgens samen."
content_hash: 476b787cfaf79ac9badf07a881748f11d34d05b2
last_modified_at: 2023-12-03
related_topics:
  - title: Deutsch version
    url: /de/common/gcc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gcc.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gcc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gcc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/gcc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gcc

Preprocess en compileer C en C++ bronbestanden, monteer en koppel ze vervolgens samen.
Meer informatie: <https://gcc.gnu.org>.

- Meerdere bronbestanden compileren in een uitvoerbaar bestand:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/source1.c pad/naar/source2.c ...</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/output_executable</span>

- Toon gemeenschappelijke waarschuwingen, foutopsporingssymbolen in output en optimaliseer zonder debuggen te beïnvloeden:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>` -Wall -g -Og -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/output_executable</span>

- Neem bibliotheken op vanuit een ander pad:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/output_executable</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/header</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/library</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library_name</span>

- Compileer broncode naar Assembler instructies:

`gcc -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>

- Compileer broncode naar een objectbestand zonder te koppelen:

`gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>
