---
layout: page
title: common/git-subtree (italiano)
description: "Strumento per gestire le dipendenze di un progetto come progetti secondari."
content_hash: 440685a3231514ef1ad91e3c27d0254b90e1c7bd
related_topics:
  - title: English version
    url: /en/common/git-subtree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-subtree.html
    icon: bi bi-globe
---
# git subtree

Strumento per gestire le dipendenze di un progetto come progetti secondari.
Maggiori informazioni: <https://manpages.debian.org/testing/git-man/git-subtree.1.en.html>.

- Aggiungi un repository Git come albero secondario:

`git subtree add --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella/</span>` --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Aggiorna l'albero secondario di un repository al suo commit più recente:

`git subtree pull --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Unisci un albero secondario al ramo principale (master):

`git subtree merge --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella/</span>` --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Invia commit all'albero secondario di un repository:

`git subtree push --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Estrai la cronologia di un nuovo progetto dalla cronologia di un albero secondario:

`git subtree split --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>
