---
layout: page
title: common/git-mergetool (français)
description: "Executer un utilitaire de différences pour résoudre les conflits de merge."
content_hash: ff21539e89bf45e9c0092f2bbbe858ec8ec687fa
related_topics:
  - title: English version
    url: /en/common/git-mergetool.html
    icon: bi bi-globe
---
# git mergetool

Executer un utilitaire de différences pour résoudre les conflits de merge.
Plus d'informations : <https://git-scm.com/docs/git-mergetool>.

- Démarrer l'outil de différences par défaut :

`git mergetool`

- Lister les outils de différences valides :

`git mergetool --tool-help`

- Démarrer l'outil de différences en précisant son nom :

`git mergetool --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tool_name</span>

- Démarrer l'outil de différences sans dialogues :

`git mergetool --no-prompt`

- Utiliser explicitement l'outil de différences graphique (voir la variable de config `merge.guitool`) :

`git mergetool --gui`

- Utiliser explicitement l'outil de différences classique (voir la variable de config `merge.tool`) :

`git mergetool --no-gui`
