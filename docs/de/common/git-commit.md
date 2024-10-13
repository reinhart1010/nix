---
layout: page
title: common/git-commit (Deutsch)
description: "Committe Dateien in ein Repository."
content_hash: cae462e04b6e2375636d49a4ba162eba53aedab3
last_modified_at: 2024-10-13
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
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit

Committe Dateien in ein Repository.
Weitere Informationen: <https://git-scm.com/docs/git-commit>.

- Committe die gestagten Dateien mit einer Nachricht in das Repository:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`"`

- Committe alle gestagten Dateien zum Repository mit einer Nachricht aus einer Datei:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/commit_nachricht_datei</span>

- Stage alle modifizierten Dateien und committe sie mit einer Nachricht:

`git commit --all --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`"`

- Committe gestagten Dateien und signiere sie mit dem definierten GPG Schlüssel (oder mit dem in der Konfigurationsdatei definierten, wenn kein Argument angegeben ist):

`git commit --gpg-sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_id</span>` --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`"`

- Ersetze den letzten Commit mit den gerade auf dem Stage liegenden Änderungen:

`git commit --amend`

- Comitte nur spezifische Dateien (die Dateien müssen schon auf dem Stage liegen):

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1 pfad/zu/datei2 ...</span>

- Erzeuge einen Commit, auch wenn keine Dateien auf dem Stage liegen:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`" --allow-empty`
