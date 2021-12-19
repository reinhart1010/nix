---
layout: page
title: common/at (français)
description: "Planifie l'exécution d'une commande une fois à un moment donné."
content_hash: 845a89b69616a4c4d7dc7c2346d48991397a6e86
related_topics:
  - title: English version
    url: /en/common/at.html
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
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
---
# at

Planifie l'exécution d'une commande une fois à un moment donné.
Le service atd (ou atrun) doit être actif pour l'exécution des commandes planifiées.
Plus d'informations : <https://man.archlinux.org/man/at.1>.

- Planifie l'exécution de la commande donnée dans l'entrée standard dans 5 minutes (Appuyer sur `Ctrl + D` une fois la commande inscrite) :

`at now + 5 minutes`

- Planifie l'exécution d'une commande depuis l'entrée standard (impression echo redirigée dans un tube) aujourd'hui à 10h00 :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./ma_commande.sh</span>`" | at 1000`

- Planifie l'exécution des commandes inclues dans un [f]ichier pour mardi prochain 21h30 :

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` 9:30 PM Tue`
