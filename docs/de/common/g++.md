---
layout: page
title: common/g++ (Deutsch)
description: "Kompiliere C++ Quelldateien."
content_hash: a83315cfd03326450eab191e23fd7cb18a670ae9
related_topics:
  - title: English version
    url: /en/common/g++.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/g++.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/g++.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/g++.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/g++.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gplusplus

Kompiliere C++ Quelldateien.
Teil der GCC (GNU Compiler Collection).
Weitere Informationen: <https://gcc.gnu.org>.

- Kompiliere eine Quelldatei in eine ausführbare Binärdatei:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Zeige geläufige Fehler und Warnungen an:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Wähle einen Sprachstandard (C++98/C++11/C++14/C++17) für das Kompilieren:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -std=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C++98|C++11|C++14|C++17</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Binde Bibliotheken, die sich an einem anderen Pfad als die Quelldatei befinden, ein:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/headerdatei</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bibliothek</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bibliotheks_name</span>

- Kompiliere und linke mehrere Quelldateien in eine ausführbare Binärdatei:

`g++ -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei_1.cpp pfad/zu/quelldatei_2.cpp ...</span>` && g++ -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei_1.o pfad/zu/quelldatei_2.o ...</span>

- Gib die Version von `g++` aus:

`g++ --version`
