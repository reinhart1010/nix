---
layout: page
title: common/git-apply (français)
description: "Applique un correctif à un fichier et/ou à l index."
content_hash: ad505e1b325acfa192dc2352244b77a20810b8c1
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-apply.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-apply.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-apply.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-apply.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git apply

Applique un correctif à un fichier et/ou à l index.
Plus d'informations : <https://git-scm.com/docs/git-apply>.

- Afficher les messages à propos des fichiers corrigés :

`git apply --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Applique le correctif et ajoute les fichiers à l index :

`git apply --index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Applique un correctif depuis une source distante :

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file.patch</span>` | git apply`

- Affiche les différences résultantes et applique le correctif :

`git apply --stat --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Applique le correctif en ordre inverse :

`git apply --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Stocke le résultat du correctif dans l'index sans modifier la branche courante :

`git apply --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
