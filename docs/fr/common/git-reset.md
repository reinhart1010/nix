---
layout: page
title: common/git-reset (français)
description: "Enlève des commits ou des changements en réinitialisant la tête Git à l'état spécifié."
content_hash: 0bfd57ef99cf671478de58f4c29d8f66a8e58a13
last_modified_at: 2023-12-19
related_topics:
  - title: English version
    url: /en/common/git-reset.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reset.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reset.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-reset.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reset

Enlève des commits ou des changements en réinitialisant la tête Git à l'état spécifié.
Si un chemin est passé en paramètre, Git reset fonctionne comme «unstage».
Si un hash de commit est passé en paramètre, Git reset annule les commits jusqu'à ce dernier.
Plus d'informations : <https://git-scm.com/docs/git-reset>.

- Tout enlever de la zone de stage :

`git reset`

- Enlever des fichiers spécifiques de la zone de stage :

`git reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier(s)</span>

- Enlever, en mode interactif, des fichiers spécifiques de l’index :

`git reset --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Annuler le dernier commit, mais garder les changements effectués dans votre système de fichiers :

`git reset HEAD~`

- Défaire les deux derniers commits, et ajouter leurs changements à l'index (dans la zone de stage) :

`git reset --soft HEAD~2`

- Enlever tout les changements qui n'ont pas été commit, qu'ils soient dans la zone de stage ou non (pour enlever seulement les changements de la zone de stage, utiliser `git checkout`) :

`git reset --hard`

- Réinitialiser le dépôt à un commit spécifique en retirant tout les changements (ceci inclus les changements dans des commits entre la tête et le commit spécifié !) :

`git reset --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
