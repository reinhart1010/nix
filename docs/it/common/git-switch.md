---
layout: page
title: common/git-switch (italiano)
description: "Passa ad altri rami. Richiede versioni di Git successive alla 2.23."
content_hash: a87822801ad5351150f066da8aadfa65732858aa
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-switch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-switch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-switch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-switch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-switch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-switch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git switch

Passa ad altri rami. Richiede versioni di Git successive alla 2.23.
Vedi anche `git checkout`.
Maggiori informazioni: <https://git-scm.com/docs/git-switch>.

- Passa ad un altro ramo esistente:

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Crea un nuovo ramo e passa a quel ramo:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Crea un nuovo ramo a partire da un commit esistente e passa a quel ramo:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Torna al ramo precedente:

`git switch -`

- Passa ad un ramo ed aggiorna tutti i moduli secondari associati:

`git switch --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Passa ad un ramo e uniscilo automaticamente al ramo corrente, include le modifiche non committate:

`git switch --merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>
