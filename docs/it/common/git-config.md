---
layout: page
title: common/git-config (italiano)
description: "Configura le impostazioni di uno o piu repository Git."
content_hash: 806c85948ebdd795d186e4a582e8faee0ed78b8b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git config

Configura le impostazioni di uno o piu repository Git.
Le configurazioni possono essere sia locali (per il repository corrente) che globali (per l'utente corrente).
Maggiori informazioni: <https://git-scm.com/docs/git-config>.

- Elenca solo le opzioni di configurazione locali (salvate in `.git/config` nel repository corrente):

`git config --list --local`

- Elenca solo le opzioni di configurazione globali (salvate in `~/.gitconfig`):

`git config --list --global`

- Elenca tutte le opzioni di configurazione impostate, sia locali che globali:

`git config --list`

- Mostra il valore di una data opzione di configurazione:

`git config alias.unstage`

- Imposta il valore globale di una data opzione di configurazione:

`git config --global alias.unstage "reset HEAD --"`

- Ripristina una opzione di configurazione globale al suo valore di default:

`git config --global --unset alias.unstage`
