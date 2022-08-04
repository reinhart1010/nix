---
layout: page
title: common/git-config (italiano)
description: "Configura le impostazioni di uno o piu repository Git."
content_hash: 806c85948ebdd795d186e4a582e8faee0ed78b8b
related_topics:
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
