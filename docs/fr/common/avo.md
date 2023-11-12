---
layout: page
title: common/avo (français)
description: "La ligne de commande officielle pour Avo."
content_hash: cb29cb54a003c9afa87bbc190c929cc863b6fc4c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/avo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/avo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# avo

La ligne de commande officielle pour Avo.
Plus d'informations : <https://www.avo.app/docs/implementation/cli>.

- Initialise un espace de travail dans le dossier courant :

`avo init`

- Connecte la cli à la plateforme Avo :

`avo login`

- Change de branche vers une branche existante Avo :

`avo checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Récupère les couvertures analytique pour le chemin courant :

`avo pull`

- Affiche le status de l'implémentation Avo :

`avo status`

- Résous les conflits Git dans les fichiers Avo :

`avo conflict`

- Ouvre l'espace de travail courant Avo dans le navigateur web par défaut :

`avo edit`

- Affiche l'aide pour une sous-commande :

`avo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sous_commande</span>` --help`
