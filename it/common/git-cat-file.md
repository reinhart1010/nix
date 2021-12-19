---
layout: page
title: common/git-cat-file (italiano)
description: "Visualizza il contenuto di un oggetto Git nel repository o mostrane dimensione e tipo."
content_hash: acd679264c8339a4e9c212001c5e4bdd46a9197e
related_topics:
  - title: English version
    url: /en/common/git-cat-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cat-file.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cat-file.html
    icon: bi bi-globe
---
# git cat-file

Visualizza il contenuto di un oggetto Git nel repository o mostrane dimensione e tipo.
Maggiori informazioni: <https://git-scm.com/docs/git-cat-file>.

- Mostra la dimen[s]ione del commit HEAD in byte:

`git cat-file -s HEAD`

- Mostra il [t]ipo (blob, albero, commit, tag) di un oggetto Git:

`git cat-file -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8c442dc3</span>

- Stam[p]a il contenuto di un oggetto Git, formattato in base al tipo:

`git cat-file -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>
