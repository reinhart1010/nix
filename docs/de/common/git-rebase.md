---
layout: page
title: common/git-rebase (Deutsch)
description: "Wende Commits von einem Branch auf einen anderen Branch an."
content_hash: aabf7e8c9634c035c1c1788831a8c6c80cae8218
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-rebase.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rebase.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rebase.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rebase.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-rebase.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rebase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rebase.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-rebase.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-rebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rebase

Wende Commits von einem Branch auf einen anderen Branch an.
Die Änderungen eines Branches werden auf einen bestehenden Branch "übertragen" und am Ende der Historie als neue Commits eingefügt.
Weitere Informationen: <https://git-scm.com/docs/git-rebase>.

- Verwende einen anderen, angegebenen Branch als Basis für den aktuellen Branch:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neuer_basisbranch</span>

- Starte einen interaktiven Rebase, bei dem Commits umsortiert, weggelassen, kombiniert oder verändert werden können:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel_basisbranch_oder_commithash</span>

- Setze einen Rebase fort, der durch einen Mergefehler unterbrochen wurde, nachdem die Konflikte aufgelöst wurden:

`git rebase --continue`

- Setze einen Rebase fort, der durch einen Mergefehler unterbrochen wurde, durch Auslassen des in Konflikt stehenden Commits:

`git rebase --skip`

- Brich einen laufenden Rebase ab (z.B. wenn er durch Mergekonflikte unterbrochen wurde):

`git rebase --abort`

- Verschiebe einen Teil des aktuellen Branches auf eine neue Basis und gib die alte Basis an, ab der die Änderungen verwendet werden sollen:

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neue_basis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alte_basis</span>

- Bearbeite die 5 letzten Commits der aktuellen Basis um diese neu zu ordnen, auszulassen, kombinieren oder zu bearbeiten:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Löse Konflikte automatisch auf, indem der aktuelle Branch bevorzugt wird (das Schlüsselwort `theirs` hat in diesem Fall eine umgekehrte Bedeutung):

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-X|--strategy-option</span>` theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
