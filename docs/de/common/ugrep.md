---
layout: page
title: common/ugrep (Deutsch)
description: "Ultraschnelles Suchtool mit Abfrage-TUI."
content_hash: c3515065925fe92dc4fc09d728165be811656daf
related_topics:
  - title: English version
    url: /en/common/ugrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ugrep.html
    icon: bi bi-globe
---
# ugrep

Ultraschnelles Suchtool mit Abfrage-TUI.
Weitere Informationen: <https://github.com/Genivia/ugrep>.

- Starte eine interaktive TUI um rekursiv nach Dateien im aktuellen Verzeichnis zu suchen (Strg-Z für Hilfe):

`ugrep --query`

- Suche im aktuellen Verzeichnis rekursiv nach Dateien, die einem bestimmten regulären Ausdruck entsprechen:

`ugrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`

- Suche in einer Datei oder in allen Dateien in einem bestimmten Verzeichnis und zeige die Zeilennummer jedes Treffers:

`ugrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Suche in allen Dateien im aktuellen Verzeichnis rekursiv und zeige den Dateinamen jeder passenden Datei:

`ugrep --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`

- Suche nach einem "fuzzy" regulären Ausdruck mit bis zu 3 zusätzlichen, fehlenden oder nicht übereinstimmenden Zeichen:

`ugrep --fuzzy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`

- Suche auch in allen komprimierten Dateien und `zip`- und `tar`-Archive:

`ugrep --decompress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`

- Suche nur in Dateien deren Dateinamen mit einem bestimmten glob-Muster übereinstimmen:

`ugrep --glob="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">glob_muster</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`

- Suche nur in C++ Quelldateien (verwende `--file-type=list`, um mögliche Optionen aufzulisten):

`ugrep --file-type=cpp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`
