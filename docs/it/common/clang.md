---
layout: page
title: common/clang (italiano)
description: "Compilatore per sorgenti C, C++ ed Objective-C. Può essere usato come alternativa a GCC."
content_hash: ec58c949f07ac8ef4977b9d42c48fbf2363359be
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/clang.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clang.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clang.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># clang

Compilatore per sorgenti C, C++ ed Objective-C. Può essere usato come alternativa a GCC.
Maggiori informazioni: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compila un file sorgente in un binario eseguibile:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente_input.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eseguibile_output</span>

- Attiva l'output di tutti gli errori ed i warning:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente_input.c</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eseguibile_output</span>

- Includi librerie contenute in un percorso differente da quello del file di sorgente:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente_input.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eseguibile_output</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso_header</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso_librerie</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_libreria</span>

- Compila codice sorgente in IR LLVM (Intermediate Representation):

`clang -S -emit-llvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ll</span>
