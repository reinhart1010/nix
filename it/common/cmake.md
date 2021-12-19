---
layout: page
title: common/cmake (italiano)
description: "Generatore di ambienti di compilazione multipiattaforma."
content_hash: 888d2a7edd4cc80b25a3b42a26d7ccffaf0cdf9c
related_topics:
  - title: Deutsch version
    url: /de/common/cmake.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cmake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cmake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmake.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cmake.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cmake.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cmake

Generatore di ambienti di compilazione multipiattaforma.
Genera Makefile, progetti Visual Studio o altro, in base al sistema operativo.
Maggiori informazioni: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Genera un Makefile ed usalo per compilare un progetto nella stessa directory dei sorgenti:

`cmake && make`

- Genera un makefile ed usalo per compilare un progetto in una directory "build" separata (out-of-source build):

`cmake -H. -B`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build</span>` && make -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build</span>

- Esegui cmake in modalità interattiva (chiederà i valori di ogni variabile invece di usare i predefiniti):

`cmake -i`
