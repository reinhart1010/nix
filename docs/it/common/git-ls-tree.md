---
layout: page
title: common/git-ls-tree (italiano)
description: "Elenca il contenuto di un oggetto albero."
content_hash: a2443bcaa27e0addaf6da7091f3b97a0c0f4ebb4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-ls-tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-ls-tree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-ls-tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-ls-tree.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git ls-tree

Elenca il contenuto di un oggetto albero.
Maggiori informazioni: <https://git-scm.com/docs/git-ls-tree>.

- Mostra il contenuto dell'albero su un ramo:

`git ls-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Mostra il contenuto dell'albero su un commit, procedendo ricorsivamente nei sotto-alberi:

`git ls-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_commit</span>

- Mostra solo il nome dei file dell'albero su un commit:

`git ls-tree --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_commit</span>
