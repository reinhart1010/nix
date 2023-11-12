---
layout: page
title: common/clang++ (Deutsch)
description: "Kompiliert C++ Quelldateien."
content_hash: 65f95c3ab462eebd371e826e4315abcdd4f5250a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/clang++.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clang++.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clang++

Kompiliert C++ Quelldateien.
Teil von LLVM.
Weitere Informationen: <https://clang.llvm.org>.

- Kompiliere eine Quelldatei in eine ausführbare Binärdatei:

`clang++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Zeige geläufige Fehler und Warnungen an:

`clang++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Wähle einen Sprachstandard für die Kompilation aus:

`clang++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -std=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c++20</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Binde Bibliotheken, die sich an einem anderen Pfad als die Quelldatei befinden, ein:

`clang++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/qelldatei.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/headerdatei</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bibliothek</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bibliotheksname</span>

- Kompiliere eine Quelldatei zu LLVM Intermediate Representation (IR):

`clang++ -S -emit-llvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ir_datei.ll</span>
