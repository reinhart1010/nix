---
layout: page
title: common/git-show (français)
description: "Affiche différents types d'objets Git (commits, tags, etc.)."
content_hash: 208d6d89042aa389781ed268da7fbd65fee6eef4
related_topics:
  - title: English version
    url: /en/common/git-show.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-show.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-show.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git show

Affiche différents types d'objets Git (commits, tags, etc.).
Plus d'informations : <https://git-scm.com/docs/git-show>.

- Afficher des informations sur le dernier commit (hachage, message, modifications et autres métadonnées) :

`git show`

- Affiche les informations du dernier commit :

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Affiche les informations associés au tag spécifié :

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiquette</span>

- Affiche les informations à propos du 3ème commit en partant du sommet de la branche :

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche</span>`~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Afficher le message d'un commit sur une seule ligne, en supprimant la sortie diff :

`git show --oneline -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Affiche uniquement la liste des fichiers changés dans un commit :

`git show --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Afficher le contenu d'un fichier tel qu'il était à une révision donnée (par exemple, branche, tag ou commit) :

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
