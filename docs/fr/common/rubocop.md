---
layout: page
title: common/rubocop (français)
description: "Lint les fichiers Ruby."
content_hash: 2e640603c81fa3390283fa6f95f41f22c6afd17e
last_modified_at: 2023-10-11
related_topics:
  - title: English version
    url: /en/common/rubocop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rubocop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rubocop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rubocop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rubocop

Lint les fichiers Ruby.
Plus d'informations : <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Vérifie tous les fichiers du répertoire actuel (y compris les sous-répertoires) :

`rubocop`

- Vérifie un ou plusieurs fichiers ou répertoires spécifiques :

`rubocop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Écrit la sortie dans un fichier :

`rubocop --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche la liste des cops (règles de lint) :

`rubocop --show-cops`

- Exclue un cop :

`rubocop --except `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_2</span>

- Exécute uniquement les cops spécifiés :

`rubocop --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_2</span>

- Corrige automatiquement les fichiers (expérimental) :

`rubocop --auto-correct`
