---
layout: page
title: common/crystal (français)
description: "Outil de gestion du code source de Crystal."
content_hash: a290aa68d6321a2143df40d26cbdb3f6a5ee4a80
last_modified_at: 2023-10-08
related_topics:
  - title: English version
    url: /en/common/crystal.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/crystal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crystal.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># crystal

Outil de gestion du code source de Crystal.
Plus d'informations : <https://crystal-lang.org/reference/using_the_compiler>.

- Exécute un fichier Crystal :

`crystal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.cr</span>

- Compile un fichier et toutes ses dépendances en un seul exécutable :

`crystal build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.cr</span>

- Lit le code source Crystal à partir de la ligne de commande ou de `stdin`, et l'exécute :

`crystal eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`'`

- Génère la documentation de l'API à partir commentaires dans les fichiers Crystal :

`crystal docs`

- Compile et exécute une suite de spécifications Crystal :

`crystal spec`

- Démarre un serveur interactif local pour tester le langage :

`crystal play`

- Crée un répertoire de projet pour une application Crystal :

`crystal init app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_application</span>

- Affiche toutes les options d'aide :

`crystal help`
