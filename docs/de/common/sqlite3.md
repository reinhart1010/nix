---
layout: page
title: common/sqlite3 (Deutsch)
description: "Das Kommandozeileninterface für SQLite 3, welches eine eigenständige dateibasierte eingebettete SQL-Engine ist."
content_hash: 0846c1ea7207200458f573b6ed6f274301195d8b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sqlite3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sqlite3

Das Kommandozeileninterface für SQLite 3, welches eine eigenständige dateibasierte eingebettete SQL-Engine ist.
Weitere Informationen: <https://sqlite.org>.

- Starte eine interaktive Shell mit einer neuen Datenbank:

`sqlite3`

- Öffne eine interaktive Shell mit einer existierenden Datenbank:

`sqlite3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datenbank.sqlite3</span>

- Führe ein SQL Statement auf einer existierenden Datenbank aus und beende die Ausführung danach:

`sqlite3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datenbank.sqlite3</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SELECT * FROM einer_tabelle;</span>`'`
