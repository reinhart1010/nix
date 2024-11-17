---
layout: page
title: common/histexpand (français)
description: "Réutiliser et développer l'historique des commandes shell dans `sh`, `bash`, `zsh`, `rbash` et `ksh`."
content_hash: 8066c2081d04399f87d4ac90e3e538be36e2dd40
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/histexpand.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/histexpand.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/histexpand.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/histexpand.html
    icon: bi bi-globe
tldri18n_status: 2
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

- Effectue une expansion de l'historique, mais affiche la commande qui aurait du être exécutée au lieu de l'exécuter :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">!-n</span>`:p`
