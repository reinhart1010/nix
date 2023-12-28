---
layout: page
title: common/find (français)
description: "Trouve récursivement des fichiers ou des dossiers dans l'arborescence spécifiée."
content_hash: a7e724804d7c5d061d87dc541bee355a5504d0b0
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

Trouve récursivement des fichiers ou des dossiers dans l'arborescence spécifiée.
Plus d'informations : <https://manned.org/find>.

- Trouve des fichiers par extension :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">racine</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- Trouve des fichiers correspondant à plusieurs chemins ou motifs :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">racine</span>` -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/chemin/**/*.ext</span>`' -or -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*motif*</span>`'`

- Trouve des dossiers correspondant à un nom donné sans vérifier la casse :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">racine</span>` -type d -iname '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*lib*</span>`'`

- Trouve des fichiers correspondant à un motif donné en excluant certains chemins de la recherche :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">racine</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.py</span>`' -not -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/site-packages/*</span>`'`

- Trouve des fichiers dans une fourchette de tailles et limite la profondeur récursive à "1" :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">racine</span>` -maxdepth 1 -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+500k</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10M</span>

- Exécute une commande pour chaque fichier (utiliser `{}` dans la commande pour utiliser le nom des fichiers) :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">racine</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`' -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l {} </span>`\;`

- Trouve les fichiers modifiés dans les 7 derniers jours :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">racine</span>` -daystart -mtime -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Trouve les fichiers vides (de taille nulle) et les supprimer :

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">racine</span>` -type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f</span>` -empty -delete`
