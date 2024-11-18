---
layout: page
title: common/at (français)
description: "Planifie l'exécution d'une commande une fois à un moment donné."
content_hash: acafb212eab591eaa6f1464e3fa048acebcefd0a
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/at.html
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
tldri18n_status: 2
---
# at

Planifie l'exécution d'une commande une fois à un moment donné.
Le service atd (ou atrun) doit être actif pour l'exécution des commandes planifiées.
Plus d'informations : <https://manned.org/at>.

- Démarre `atd` comme un service (en tâche de fond) :

`systemctl start atd`

- Planifie l'exécution de la commande donnée dans l'entrée standard dans 5 minutes (Appuyer sur `Ctrl + D` une fois la commande inscrite) :

`at now + 5 minutes`

- Crée des commandes de manière interactive et les exécute à un moment précis :

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Planifie l'exécution d'une commande depuis l'entrée standard (impression echo redirigée dans un tube) aujourd'hui à 10h00 :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>`" | at 1000`

- Planifie l'exécution des commandes inclues dans un [f]ichier pour mardi prochain 21h30 :

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` 9:30 PM Tue`
