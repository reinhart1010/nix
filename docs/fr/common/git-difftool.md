---
layout: page
title: common/git-difftool (français)
description: "Afficher les modifications apportées aux fichiers à l'aide d'outils de comparaison externes. Accepte les mêmes options et arguments que Git diff."
content_hash: 53047e28e657887effcd59596c8a3954fe783387
related_topics:
  - title: English version
    url: /en/common/git-difftool.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-difftool.html
    icon: bi bi-globe
---
# git difftool

Afficher les modifications apportées aux fichiers à l'aide d'outils de comparaison externes. Accepte les mêmes options et arguments que Git diff.
Plus d'informations : <https://git-scm.com/docs/git-difftool>.

- Lister les outils de comparaison disponibles :

`git difftool --tool-help`

- Configurer Meld comme outil de comparaison par défaut :

`git config --global diff.tool "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meld</span>`"`

- Utiliser l'outil de comparaison par défaut pour afficher les fichiers modifiés :

`git difftool --staged`

- Utiliser un outil de comparaison spécifique (opendiff) pour afficher les changements depuis un commit :

`git difftool --tool=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opendiff</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
