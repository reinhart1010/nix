---
layout: page
title: common/git-commit (Deutsch)
description: "Committe Dateien in ein Repository."
content_hash: f144de247c652c1ac1e623708d5e95ef1996080c
related_topics:
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
---
# git commit

Committe Dateien in ein Repository.
Weitere Informationen: <https://git-scm.com/docs/git-commit>.

- Committe gestagten Dateien zum Repository mit einer Nachricht:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`"`

- Committe alle gestagten Dateien zum Repository mit einer Nachricht aus einer Datei:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/commit_nachricht_datei</span>

- Stage alle modifizierten Dateien und committe sie mit einer Nachricht:

`git commit -a -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`"`

- Committe alle gestagten Dateien und [S]igniere sie mit dem in `~/.gitconfig` definierten GPG Schlüssel:

`git commit -S -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`"`

- Ersetze den letzten Commit mit den gerade auf dem Stage liegenden Änderungen:

`git commit --amend`

- Comitte nur spezifische Dateien (die Dateien müssen schon auf dem Stage liegen):

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>

- Erzeuge einen Commit, auch wenn keine Dateien auf dem Stage liegen:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`" --allow-empty`
