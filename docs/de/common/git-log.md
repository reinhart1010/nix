---
layout: page
title: common/git-log (Deutsch)
description: "Zeigt die Commit-Historie an."
content_hash: cb2e7b17d96d89f92ece081d467c92c914c08c4b
related_topics:
  - title: English version
    url: /en/common/git-log.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-log.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-log.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-log.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-log.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-log.html
    icon: bi bi-globe
---
# git log

Zeigt die Commit-Historie an.
Weitere Informationen: <https://git-scm.com/docs/git-log>.

- Zeige die Sequenz der Commits des Git-Repository im aktuellen Verzeichnis, beginnend mit dem aktuellen, an:

`git log`

- Zeige die Historie einer bestimmten Datei oder eines Verzeichnisses, inklusive Unterschiede, an:

`git log -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Zeige einen Überblick der Commits an und welche Dateien jeweils verändert wurden:

`git log --stat`

- Zeige einen Graphen von Commits im aktuellen Branch, wobei jeweils nur die erste Zeile der Commit-Nachricht angezeigt wird:

`git log --oneline --graph`

- Zeige einen Graphen von allen Commits, Tags und Branches im gesamten Repository:

`git log --oneline --decorate --all --graph`

- Zeige nur Commits, deren Commit-Nachricht einen bestimmten Text enthalten (Ohne Beachtung von Groß- und Kleinschreibung):

`git log -i --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Zeige die letzten N Commits eines bestimmten Autors:

`git log -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl</span>` --author=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autor</span>

- Zeige alle Commits zwischen zwei Zeitpunkten an (yyyy-mm-dd):

`git log --before="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-29</span>`" --after="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-17</span>`"`
