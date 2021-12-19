---
layout: page
title: common/cmake (Deutsch)
description: "Plattformübergreifndes Build-Automatisierungs-System, das Vorlagen für native Build-Systeme erzeugt."
content_hash: 16768001fa6644e99db05b927f04547dc2451a7d
related_topics:
  - title: English version
    url: /en/common/cmake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cmake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmake.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cmake.html
    icon: bi bi-globe
---
# cmake

Plattformübergreifndes Build-Automatisierungs-System, das Vorlagen für native Build-Systeme erzeugt.
Weitere Informationen: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Erzeuge eine Build-Vorlage im aktuellen Verzeichnis mit `CMakeLists.txt` eines Projektordners:

`cmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/projektordner</span>

- Erzeuge eine Build-Vorlage mit der Build-Art `Release`:

`cmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/projektordner</span>` -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CMAKE_BUILD_TYPE=Release</span>

- Benutze eine generierte Vorlage, um Artifakte zu erzeugen:

`cmake --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/build_verzeichnis</span>

- Installiere die Build-Artifakte in `/usr/local/` und enferne Debugsymbole:

`cmake --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/build_verzeichnis</span>` --strip`

- Installiere die Build-Artifakte mit einem eigenen Präfix für Pfade:

`cmake --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/build_verzeichnis</span>` --strip --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Führe ein bestimmtes Build-Ziel aus:

`cmake --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/build_verzeichnis</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zielname</span>
