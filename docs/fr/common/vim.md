---
layout: page
title: common/vim (français)
description: "Vim (Vi IMproved), un éditeur de texte en ligne de commandes, fournit plusieurs modes pour différentes manipulations de texte."
content_hash: fd21fda67493d70f001b027ae76a96b0775b4708
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
---
# vim

Vim (Vi IMproved), un éditeur de texte en ligne de commandes, fournit plusieurs modes pour différentes manipulations de texte.
Pressez `i` pour passer en mode édition. `<Esc>` revient au mode normal, qui ne permet pas l insertion de code.
Plus d'informations : <https://www.vim.org>.

- Ouvrir un fichier :

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Ouvrir un fichier à une ligne spécifiée :

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_ligne</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Consulter le manuel utilisateur :

`:help<Entrée>`

- Sauvegarder et fermer :

`:wq<Entrée>`

- Annuler la dernière opération :

`u`

- Rechercher un motif dans un fichier (appuyez `n`/`N` pour aller à la prochaine / précédente occurrence) :

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_recherché</span>`<Entrée>`

- Effectuer une substitution par expression régulière dans tout le fichier :

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remplacement</span>`/g<Entrée>`

- Afficher les numéros de ligne :

`:set nu<Entrée>`
