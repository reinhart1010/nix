---
layout: page
title: common/rubocop (français)
description: "Lint les fichiers Ruby."
content_hash: 3e2bdc681b5b4e04312228375beac09a8a747ed3
last_modified_at: 2024-10-13
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
tldri18n_status: 2
---
# rubocop

Lint les fichiers Ruby.
Plus d'informations : <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Vérifie tous les fichiers du répertoire actuel (y compris les sous-répertoires) :

`rubocop`

- Vérifie un ou plusieurs fichiers ou répertoires spécifiques :

`rubocop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier1 chemin/vers/fichier_ou_dossier2 ...</span>

- Écrit la sortie dans un fichier :

`rubocop --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche la liste des cops (règles de lint) :

`rubocop --show-cops`

- Exclue un cop :

`rubocop --except `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_1 cop_2 ...</span>

- Exécute uniquement les cops spécifiés :

`rubocop --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_1 cop_2 ...</span>

- Corrige automatiquement les fichiers (expérimental) :

`rubocop --auto-correct`
