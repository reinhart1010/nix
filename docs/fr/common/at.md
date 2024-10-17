---
layout: page
title: common/at (français)
description: "Planifie l'exécution d'une commande une fois à un moment donné."
content_hash: dec31a7085c77ba969d49b9636e94c370b30fe1d
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># at

Planifie l'exécution d'une commande une fois à un moment donné.
Le service atd (ou atrun) doit être actif pour l'exécution des commandes planifiées.
Plus d'informations : <https://manned.org/at>.

- Planifie l'exécution de la commande donnée dans l'entrée standard dans 5 minutes (Appuyer sur `Ctrl + D` une fois la commande inscrite) :

`at now + 5 minutes`

- Planifie l'exécution d'une commande depuis l'entrée standard (impression echo redirigée dans un tube) aujourd'hui à 10h00 :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./ma_commande.sh</span>`" | at 1000`

- Planifie l'exécution des commandes inclues dans un [f]ichier pour mardi prochain 21h30 :

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` 9:30 PM Tue`
