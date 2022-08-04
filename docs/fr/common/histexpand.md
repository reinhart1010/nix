---
layout: page
title: common/histexpand (français)
description: "Réutiliser et développer l'historique des commandes shell dans `sh`, `bash`, `zsh`, `rbash` et `ksh`."
content_hash: 6526e1acbc80d6c2e178f8734cfe21a2ba804641
related_topics:
  - title: English version
    url: /en/common/histexpand.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/histexpand.html
    icon: bi bi-globe
---
# history expansion

Réutiliser et développer l'historique des commandes shell dans `sh`, `bash`, `zsh`, `rbash` et `ksh`.
Plus d'informations : <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Exécute de nouveau la commande précédente en tant que root (`!!` est remplacé par la commande précédente) :

`sudo !!`

- Exécute une commande avec le dernier argument de la commande précédente :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` !$`

- Exécute une commande avec le premier argument de la commande précédente :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` !^`

- Exécute la `n`-ème commande de l'historique, en partant de la plus ancienne :

`!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Exécute la `n`-ème commande de l'historique, en partant de la plus récente :

`!-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Exécute la commande contenant `string` la plus récente :

`!?`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`?`

- Exécute la commande précédente, en remplaçant `string1` par `string2` :

`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string1</span>`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string2</span>`^`

- Effectue une expansion de l'historique, mais affiche la commande qui aurait du être exécutée au lieu de l'exécuter  :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">!-n</span>`:p`
