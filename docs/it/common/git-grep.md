---
layout: page
title: common/git-grep (italiano)
description: "Cerca stringhe nello storico dei file tracciati nel repository."
content_hash: 5a967f30885eb27a63e2433520b7e6314206f027
related_topics:
  - title: English version
    url: /en/common/git-grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-grep.html
    icon: bi bi-globe
---
# git-grep

Cerca stringhe nello storico dei file tracciati nel repository.
Supporta molti degli stessi parametri accettati dal comando `grep` tradizionale.
Maggiori informazioni: <https://git-scm.com/docs/git-grep>.

- Cerca una stringa nei file tracciati:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stringa_ricercata</span>

- Cerca una stringa nei file tracciati che soddisfano un dato pattern:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stringa_ricercata</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_glob_pattern</span>

- Cerca una stringa nei file tracciati, sottomoduli inclusi:

`git grep --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stringa_ricercata</span>

- Cerca una stringa in uno dato momento della cronologia del repository:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stringa_ricercata</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>

- Cerca una stringa in tutti i rami:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stringa_ricercata</span>` $(git rev-list --all)`
