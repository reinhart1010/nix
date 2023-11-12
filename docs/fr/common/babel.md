---
layout: page
title: common/babel (français)
description: "Un transpilateur qui convertit du code JavaScript avec la syntaxe ES6/ES7 en syntaxe ES5."
content_hash: e69d59a3044b067e875509d8ad67d31bc03927c3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/babel.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/babel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/babel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/babel.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/babel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/babel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# babel

Un transpilateur qui convertit du code JavaScript avec la syntaxe ES6/ES7 en syntaxe ES5.
Plus d'informations : <https://babeljs.io/>.

- Transpile une fichier spécifié et affiche le résultat dans la sortie standard :

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Transpile un fichier spécifié et enregistre le résultat dans un autre fichier :

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier/d_entrée</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier/de/sortie</span>

- Transpile un fichier d'entrée à chaque fois qu'il est modifié :

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier/d_entrée</span>` --watch`

- Transpile tout un dossier et ses fichiers :

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Ignore des fichiers (séparés par une virgule) dans un dossier :

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichiers_ignorés</span>

- Transpile et minifie la sortie :

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier/d_entrée</span>` --minified`

- Sélectionne un lot de pré-configuration pour le formatage de sortie :

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier/d_entrée</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pré-configurations</span>

- Affiche toutes les options disponibles :

`babel --help`
