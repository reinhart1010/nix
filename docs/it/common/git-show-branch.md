---
layout: page
title: common/git-show-branch (italiano)
description: "Mostra rami e relativi commit."
content_hash: 31fe7f7b348db006af2908b926bc8bdf424fe160
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-show-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-show-branch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git show-branch

Mostra rami e relativi commit.
Maggiori informazioni: <https://git-scm.com/docs/git-show-branch>.

- Mostra un sommario degli ultimi commit in un ramo:

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo|riferimento|commit</span>

- Confronta commit nella cronologia di più commit o rami:

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo|riferimento|commit</span>

- Confronta tutti i rami remoti tracciati:

`git show-branch --remotes`

- Confronta i rami locali e remoti:

`git show-branch --all`

- Mostra gli ultimi commit di tutti i rami:

`git show-branch --all --list`

- Confronta un dato ramo con quello corrente:

`git show-branch --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|nome_ramo|riferimento</span>

- Mostra il nome del commit e non il nome relativo:

`git show-branch --sha1-name --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current|nome_ramo|riferimento</span>

- Mostra un numero aggiuntivo di commit oltre il predecessore comune:

`git show-branch --more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|nome_ramo|riferimento</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|nome_ramo|riferimento</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>
