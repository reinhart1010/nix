---
layout: page
title: common/lsd (français)
description: "Liste le contenu d'un répertoire."
content_hash: b5c25f02f2f571c6217162f470f59cc1bc0c111e
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/common/lsd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lsd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lsd

Liste le contenu d'un répertoire.
Commande `ls` de nouvelle génération, écris en Rust.
Plus d'informations : <https://github.com/Peltoche/lsd>.

- Liste les fichiers et les répertoires, un par ligne :

`lsd -1`

- Liste tous les fichiers et les répertoires, ainsi que ceux cachés, du répertoire courant :

`lsd -a`

- Liste les fichiers et les répertoires en ajoutant `/` après le nom des répertoires :

`lsd -F`

- Liste tous les fichiers et les répertoires dans le format long (permissions, propriétaire, taille dans un format lisible, et date de modification) :

`lsd -lha`

- Liste les fichiers et les répertoires dans le format long, triés par taille (descendent) :

`lsd -lS`

- Liste les fichiers et les répertoires dans le format long, triés par date de modification (plus vieux en premier) :

`lsd -ltr`

- Liste seulement les répertoires :

`lsd -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/</span>

- Liste récursivement tous les répertoires dans un format arborescent :

`lsd --tree -d`
