---
layout: page
title: common/code (français)
description: "Éditeur de code multiplateforme et extensible."
content_hash: 74126a80f459111df211834d41be263a50e21d24
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/code.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/code.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/code.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/code.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/code.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/code.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/code.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/code.html
    icon: bi bi-globe
tldri18n_status: 2
---
# code

Éditeur de code multiplateforme et extensible.
Plus d'informations : <https://github.com/microsoft/vscode>.

- Démarre Visual Studio Code :

`code`

- Ouvre des fichiers/répertoires spécifiques :

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...</span>

- Compare deux fichiers spécifiques :

`code --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier2</span>

- Ouvre des fichiers/répertoires spécifiques dans une nouvelle fenêtre :

`code --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...</span>

- Installe/désinstalle une extension spécifique :

`code --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>`-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">éditeur.extension</span>

- Affiche les extensions installées :

`code --list-extensions`

- Affiche les extensions installées avec leurs versions :

`code --list-extensions --show-versions`

- Démarre l'éditeur en tant que super utilisateur (root) tout en stockant les données utilisateur dans un répertoire spécifique :

`sudo code --user-data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>
