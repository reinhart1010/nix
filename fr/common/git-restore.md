---
layout: page
title: common/git-restore (français)
description: "Restaurez les fichiers de l'arborescence de travail. Nécessite la version 2.23+ de Git."
content_hash: d9c1907f319f5fee6507ce49b326aabb9a57ae39
related_topics:
  - title: English version
    url: /en/common/git-restore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-restore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-restore.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-restore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git restore

Restaurez les fichiers de l'arborescence de travail. Nécessite la version 2.23+ de Git.
Voir aussi `git checkout`.
Plus d'informations : <https://git-scm.com/docs/git-restore>.

- Restaurer un fichier supprimé à partir du contenu du commit actuel (HEAD) :

`git restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Restaurer un fichier a la version d'un commit spécifié :

`git restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Annulez toutes les modifications non validées des fichiers suivis, en revenant au HEAD :

`git restore .`
