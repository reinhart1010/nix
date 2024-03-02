---
layout: page
title: common/exa (français)
description: "Une alternative moderne à `ls` (pour lister le contenu de répertoires)."
content_hash: 02de303bd393339cf224f2990d4e9a84e2581c5e
last_modified_at: 2024-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/exa.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/exa.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/exa.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/exa.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/exa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># exa

Une alternative moderne à `ls` (pour lister le contenu de répertoires).
Plus d'information : <https://the.exa.website>.

- Liste les fichiers, un par ligne :

`exa --oneline`

- Liste tous les fichiers, y compris les fichiers cachés :

`exa --all`

- Liste au format long (autorisations, propriété, taille et date de modification) de tous les fichiers :

`exa --long --all`

- Liste les fichiers avec le plus volumineux en haut :

`exa --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taille</span>

- Affiche une arborescence de fichiers, sur trois niveaux de profondeur :

`exa --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Liste des fichiers triés par date de modification (le plus ancien en premier) :

`exa --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modifié</span>

- Liste les fichiers avec leur en-tête, leur icône et leur statut Git :

`exa --long --header --icons --git`

- Liste les fichiers sauf ceux mentionnés dans `.gitignore` :

`exa --git-ignore`
