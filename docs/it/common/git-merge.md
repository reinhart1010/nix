---
layout: page
title: common/git-merge (italiano)
description: "Esegui un'unione (merge) tra due rami Git."
content_hash: 3a5cbf9282bb9536fde47a2135c1daae4b94f17e
related_topics:
  - title: English version
    url: /en/common/git-merge.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-merge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-merge.html
    icon: bi bi-globe
---
# git merge

Esegui un'unione (merge) tra due rami Git.
Maggiori informazioni: <https://git-scm.com/docs/git-merge>.

- Avvia un'unione con il tuo ramo corrente:

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_da_unire</span>

- Avvia un'unione e cambia il messaggio predefinito:

`git merge --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_da_unire</span>

- Avvia un'unione e committa l'operazione:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_da_unire</span>

- Interrompi un'unione in caso di conflitti:

`git merge --abort`
