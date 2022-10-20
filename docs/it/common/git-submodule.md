---
layout: page
title: common/git-submodule (italiano)
description: "Ispeziona, aggiorna e gestisce moduli secondari (submodule)."
content_hash: 7feca13d1f23cf5aeade1aa0bf043e937131d897
related_topics:
  - title: English version
    url: /en/common/git-submodule.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-submodule.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-submodule.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-submodule.html
    icon: bi bi-globe
---
# git submodule

Ispeziona, aggiorna e gestisce moduli secondari (submodule).
Maggiori informazioni: <https://git-scm.com/docs/git-submodule>.

- Installa specifici moduli secondari di un repository:

`git submodule update --init --recursive`

- Aggiungi un repository Git come modulo secondario:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>

- Aggiungi un repository Git come modulo secondario alla directory specificata:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Aggiorna tutti i moduli secondari al loro commit più recente:

`git submodule foreach git pull`
