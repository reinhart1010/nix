---
layout: page
title: windows/del (Deutsch)
description: "Lösche eine oder mehrere Dateien."
content_hash: baf0060eaba2134da1d8d0675387848dd78c1004
related_topics:
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># del

Lösche eine oder mehrere Dateien.
Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Lösche eine oder mehrere durch Leerzeichen getrennte Dateien oder Dateimuster:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateimuster</span>

- Fordere vor dem Löschen jeder Datei zur Bestätigung auf:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateimuster</span>` /p`

- Erzwinge das Löschen von schreibgeschützten Dateien:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateimuster</span>` /f`

- Lösche alle Dateien die dem Muster entsprechen rekursiv in allen Unterordnern:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateimuster</span>` /s`

- Zeige keine Eingabeaufforderung wenn Dateien basierend auf einem globalen Platzhalter gelöscht werden sollen:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateimuster</span>` /q`

- Zeige Hilfe an und liste verfügbare Attribute auf:

`del /?`

- Lösche Dateien mit den gegebenen Attributen:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateimuster</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribut</span>
