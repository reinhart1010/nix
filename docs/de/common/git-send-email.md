---
layout: page
title: common/git-send-email (Deutsch)
description: "Sende eine Menge von Patches als E-Mail. Patches können als Dateien, Ordner oder Liste von Revisionen spezifiziert werden."
content_hash: 1b4a197360bac549c5f97ee417cb5e665faa0035
last_modified_at: 2024-06-15
related_topics:
  - title: English version
    url: /en/common/git-send-email.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-send-email.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-send-email.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-send-email.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git send-email

Sende eine Menge von Patches als E-Mail. Patches können als Dateien, Ordner oder Liste von Revisionen spezifiziert werden.
Weitere Informationen: <https://git-scm.com/docs/git-send-email>.

- Sende den letzten Commit des aktuellen Branches:

`git send-email -1`

- Sende einen spezifischen Commit:

`git send-email -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Sende die letzten (z.B. 10) Commits des aktuellen Branches:

`git send-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10</span>

- Editiere eine E-Mail mit einer Reihe von Patches im Standardmailclienten:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_commits</span>` --compose`

- Bearbeite den E-Mail Text jedes der zu versendenden Patches:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl_an_commits</span>` --annotate`
