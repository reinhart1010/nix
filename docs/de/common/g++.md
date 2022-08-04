---
layout: page
title: common/g++ (Deutsch)
description: "Kompiliere C++ Quelldateien."
content_hash: de87dcbf96ad09fa749044daace16c30683da846
related_topics:
  - title: English version
    url: /en/common/g++.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/g++.html
    icon: bi bi-globe
---
# gplusplus

Kompiliere C++ Quelldateien.
Teil der GCC (GNU Compiler Collection).
Weitere Informationen: <https://gcc.gnu.org>.

- Kompiliere eine Quelldatei in eine ausführbare Binärdatei:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_datei</span>

- Zeige (fast) alle Fehler und Warnungen an:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.cpp</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_datei</span>

- Wähle einen Sprachstandard für das Kompilieren:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.cpp</span>` -std=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C++98|C++11|C++14|C++17</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_datei</span>

- Binde Bibliotheken, die sich an einem anderen Pfad als die Quelldatei befinden mit ein:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_datei</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">header_pfad</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bibliotheks_pfad</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bibliotheks_name</span>
