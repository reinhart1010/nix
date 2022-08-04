---
layout: page
title: common/git-diff (français)
description: "Afficher les changements sur les fichiers suivis."
content_hash: 2a12bb0e2944dba81834d9cc21c210dd0ac3ac2f
related_topics:
  - title: English version
    url: /en/common/git-diff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-diff.html
    icon: bi bi-globe
---
# git diff

Afficher les changements sur les fichiers suivis.
Plus d'informations : <https://git-scm.com/docs/git-diff>.

- Afficher les changements sur les fichiers suivis :

`git diff`

- Afficher tous les changements sur les fichiers par rapport à la tête de branche :

`git diff HEAD`

- Afficher tous les changements sur les fichiers ajoutés mais pas encore commités :

`git diff --staged`

- Afficher les changements de tous les commits à partir d'une date / heure donnée (expression de dates, ex : "1 week 2 days" pour 1 semaine et 2 jours ou une date ISO) :

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Afficher seulement les noms des fichiers modifiés depuis un commit donné :

`git diff --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Afficher un résumé des créations de fichiers, renommages ou changements de droits depuis un commit :

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Comparer un fichier entre deux branches ou commits :

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Comparer plusieurs fichiers de la branche courante avec une autre branche :

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
