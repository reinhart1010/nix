---
layout: page
title: common/git-branch (Deutsch)
description: "Verwalte und Arbeite mit Git Branches."
content_hash: e359d11141e645bcb4696dde4889a796b816d6da
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-branch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-branch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-branch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-branch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-branch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git branch

Verwalte und Arbeite mit Git Branches.
Weitere Informationen: <https://git-scm.com/docs/git-branch>.

- Liste alle Branches auf (Lokal und Remote). Der momentan aktive (ausgecheckte) Branch wird mit `*` markiert:

`git branch --all`

- Liste alle Branches auf, welche einen spezifischen Git-Commit in ihrer Historie enthalten:

`git branch --all --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>

- Zeige den Namen des aktuellen Branches:

`git branch --show-current`

- Erstelle einen neuen Branch auf Basis des letzten Commits:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Erstelle einen neuen Branch auf Basis eines bestimmten Commits:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>

- Benenne einen Branches um (der Branch muss nicht ausgecheckt sein):

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--move</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alter_branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neuer_branch_name</span>

- Lösche einen lokalen Branch (der Branch muss nicht ausgecheckt sein):

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Lösche einen remote-Branch:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_branch_name</span>
