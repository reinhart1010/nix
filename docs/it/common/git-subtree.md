---
layout: page
title: common/git-subtree (italiano)
description: "Strumento per gestire le dipendenze di un progetto come progetti secondari."
content_hash: b929f0979755f3a3e282a78d51b43655e41edb2e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-subtree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-subtree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-subtree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git subtree

Strumento per gestire le dipendenze di un progetto come progetti secondari.
Maggiori informazioni: <https://manpages.debian.org/latest/git-man/git-subtree.1.html>.

- Aggiungi un repository Git come albero secondario:

`git subtree add --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory/</span>` --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Aggiorna l'albero secondario di un repository al suo commit più recente:

`git subtree pull --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Unisci un albero secondario al ramo principale (master):

`git subtree merge --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory/</span>` --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Invia commit all'albero secondario di un repository:

`git subtree push --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Estrai la cronologia di un nuovo progetto dalla cronologia di un albero secondario:

`git subtree split --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>
