---
layout: page
title: common/gcc (Deutsch)
description: "Präprozessiert und kompiliert C und C++ Quellcodedateien und linkt diese anschließend zusammen."
content_hash: 3b84434c2068e72a86f085a19793e77b0f8227d2
related_topics:
  - title: English version
    url: /en/common/gcc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gcc.html
    icon: bi bi-globe
---
# gcc

Präprozessiert und kompiliert C und C++ Quellcodedateien und linkt diese anschließend zusammen.
Weitere Informationen: <https://gcc.gnu.org>.

- Kompiliere mehrere Quellcodedateien zu einer ausführbaren Datei:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2.c</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Erlaube Warnungen und debug-Symbole in der Ausgabedatei:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.c</span>` -Wall -Og --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>

- Inkludiere Bibliotheken aus anderen Verzeichnissen:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.c</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/binärdatei</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/headerdatei</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bibliothek1</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bibliothek2</span>

- Kompiliere Quellcodedateien zu Assemblerinstruktionen:

`gcc -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.c</span>

- Kompiliere eine oder mehrere Quellcodedateien ohne diese zu linken:

`gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.c</span>
