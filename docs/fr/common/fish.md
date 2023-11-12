---
layout: page
title: common/fish (français)
description: "Friendly Interactive SHell, un interpréteur de ligne de commande, conçu pour être facile à utiliser."
content_hash: e01394b90b64b2ecf9879480c13b18dbb152e365
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/fish.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/fish.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fish

Friendly Interactive SHell, un interpréteur de ligne de commande, conçu pour être facile à utiliser.
Plus d'informations : <https://fishshell.com>.

- Démarre une session shell interactive :

`fish`

- Exécute une commande, puis termine la session :

`fish -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>`"`

- Exécute un script :

`fish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.fish</span>

- Vérifie les erreurs de syntaxe dans un script :

`fish --no-execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.fish</span>

- Démarre une session shell interactive en mode privé, dans laquelle le shell n'a pas accès à l'historique et n'y écrit rien :

`fish --private`

- Affiche les informations de version :

`fish --version`

- Ajoute et exporte une variable d'environnement, qui persiste entre les redémarrages du shell (à exécuter depuis le shell uniquement) :

`set -Ux `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_variable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur_de_la_variable</span>
