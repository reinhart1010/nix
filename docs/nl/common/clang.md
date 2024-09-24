---
layout: page
title: common/clang (Nederlands)
description: "Compiler voor C, C++, en Objective-C bronbestanden. Kan gebruikt worden als een vervanger van GCC."
content_hash: a1eb1d3c863da25fb5f83ceab758913f283c4a04
last_modified_at: 2024-09-24
related_topics:
  - title: Deutsch version
    url: /de/common/clang.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clang.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clang.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clang.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clang.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># clang

Compiler voor C, C++, en Objective-C bronbestanden. Kan gebruikt worden als een vervanger van GCC.
Meer informatie: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compileer een broncodebestand naar een uitvoerbaar binair bestand:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invoer_bron.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaar_bestand</span>

- Toon alle fouten en waarschuwingen:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invoer_bron.c</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaar_bestand</span>

- Voeg bibliotheken toe die zich op een ander pad bevinden dan het bronbestand:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invoer_bron.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaarbestand</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">header_pad</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bibliotheek_ad</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bibliotheek_naam</span>

- Compileer broncode naar LLVM Intermediate Representation (IR):

`clang -S -emit-llvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.ll</span>

- Compileer broncode zonder deze te linken:

`clang -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invoer_bron.c</span>

- Optimaliseer het gecompileerde programma voor prestaties:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>` -O`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|fast</span>
