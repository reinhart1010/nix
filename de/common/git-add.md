---
layout: page
title: common/git-add (Deutsch)
description: "Füge Dateien zum Index/Stage hinzu."
content_hash: 9025180f6e5c2a5a2dc9b5d2126bdd30599b3a0a
related_topics:
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-add.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-add.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-add.html
    icon: bi bi-globe
---
# git add

Füge Dateien zum Index/Stage hinzu.
Weitere Informationen: <https://git-scm.com/docs/git-add>.

- Füge eine bestimmte Datei zum Index hinzu:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Füge alle Dateien zum Index hinzu (nachverfolgte und nicht nachverfolgte):

`git add -A`

- Füge nur nachverfolgte Dateien zum Index hinzu (Updaten des Index):

`git add -u`

- Füge auch Dateien, welche ignoriert werden (`.gitignore`) hinzu:

`git add -f`

- Füge Teile von Dateien zum Index interaktiv hinzu:

`git add -p`

- Füge Teile einer bestimmten Datei interaktiv hinzu:

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Füge Dateien zum Index interaktiv hinzu:

`git add -i`
