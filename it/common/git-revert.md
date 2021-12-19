---
layout: page
title: common/git-revert (italiano)
description: "Crea nuovi commit che invertano i risultati dei commit precedenti."
content_hash: 322ee01e37cae60cf3a8d3716a7c039dd20c56fa
related_topics:
  - title: English version
    url: /en/common/git-revert.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-revert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-revert.html
    icon: bi bi-globe
---
# git revert

Crea nuovi commit che invertano i risultati dei commit precedenti.
Maggiori informazioni: <https://git-scm.com/docs/git-revert>.

- Inverti il commit più recente:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Inverti il quintùltimo commit:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Inverti più commit:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo~5..nome_ramo~2</span>

- Inverti senza creare nuovi commit, ma modificando l'albero di lavoro:

`git revert -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
