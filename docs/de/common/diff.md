---
layout: page
title: common/diff (Deutsch)
description: "Vergleiche Dateien und Verzeichnisse."
content_hash: 9255b47c5b30bff7c9ba268de0ff75e5ed32c951
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/diff.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/diff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/diff.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/diff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diff

Vergleiche Dateien und Verzeichnisse.
Weitere Informationen: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Vergleiche Dateien (Listet jene Veränderungen auf, mit denen `datei1` zu `datei2` wird):

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>

- Vergleiche Dateien und ignoriere Leerzeichen:

`diff --ignore-all-space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>

- Vergleiche Dateien und zeige Unterschiede nebeneinander:

`diff --side-by-side `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>

- Vergleiche Dateien und zeige Unterschiede in vereinheitlichtem Format (wie in `git diff`):

`diff --unified `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>

- Vergleiche Verzeichnisse rekursiv (zeigt sowohl Namen von unterschiedlichen Dateien/Verzeichnissen, als auch Unterschiede zwischen Dateien):

`diff --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">altes_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neues_verzeichnis</span>

- Vergleiche Verzeichnisse und zeige nur die Namen der Dateien, die unterschiedlich sind:

`diff --recursive --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">altes_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neues_verzeichnis</span>

- Erstelle ein patch-Datei für Git bestehend aus den Unterschieden zweier Dateien und behandle fehlende Dateien als leer:

`diff --text --unified --new-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diff.patch</span>
