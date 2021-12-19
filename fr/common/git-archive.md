---
layout: page
title: common/git-archive (français)
description: "Crée une archive de fichiers depuis un branche donnée."
content_hash: de37ec2378b3c890f65554b70fb6ed444a7eea63
related_topics:
  - title: Deutsch version
    url: /de/common/git-archive.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-archive.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-archive.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-archive.html
    icon: bi bi-globe
---
# git archive

Crée une archive de fichiers depuis un branche donnée.
Plus d'informations : <https://git-scm.com/docs/git-archive>.

- Crée une archive `.tar` avec le contenu de la HEAD et l'affiche sur la sortie standard :

`git archive --verbose HEAD`

- Crée une archive `.zip` avec le contenu de la HEAD et l'affiche sur la sortie standard :

`git archive --verbose --format=zip HEAD`

- Pareil que ci-dessus mais écrit dans l'archive spécifiée :

`git archive --verbose --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.zip</span>` HEAD`

- Crée une archive depuis le dernier commit de la branche spécifiée :

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Crée une archive avec le contenu d'un répertoire donné :

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/repertoire</span>

- Ajoutez un chemin d'accès à chaque fichier pour l'archiver dans un répertoire spécifique :

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/cible</span>`/ HEAD`
