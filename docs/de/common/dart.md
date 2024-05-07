---
layout: page
title: common/dart (Deutsch)
description: "Das Werkzeug zur Verwaltung von Dart-Projekten."
content_hash: 2c15c86811b76349bcd7ed4ceb01391b74ae6059
last_modified_at: 2024-05-07
related_topics:
  - title: English version
    url: /en/common/dart.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dart.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dart

Das Werkzeug zur Verwaltung von Dart-Projekten.
Weitere Informationen: <https://dart.dev/tools/dart-tool>.

- Initialisiere ein neues Dart-Projekt in einem Verzeichnis mit demselben Namen:

`dart create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">projekt_name</span>

- Ausführen einer Dart-Datei:

`dart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.dart</span>

- Herunterladen der Abhängigkeiten für das aktuelle Projekt:

`dart pub get`

- Ausführen von Unit-Tests für das aktuelle Projekt:

`dart test`

- Aktualisieren veralteter Projektabhängigkeiten, um Null-Sicherheit zu unterstützen:

`dart pub upgrade --null-safety`

- Kompilieren einer Dart-Datei in eine native Binärdatei:

`dart compile exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.dart</span>
