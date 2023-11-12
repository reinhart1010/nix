---
layout: page
title: common/zsh (français)
description: "Z SHell, un interpréteur de ligne de commande compatible avec Bash."
content_hash: fe9b6dcd06a10d85d69c49b3b039e08e2f49e2fe
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/zsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zsh.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zsh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zsh

Z SHell, un interpréteur de ligne de commande compatible avec Bash.
Voir aussi `histexpand` pour l'expansion de l'historique.
Plus d'informations : <https://www.zsh.org>.

- Démarre une session shell interactive :

`zsh`

- Exécute une commande, puis termine la session :

`zsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>`"`

- Exécute un script :

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/script.zsh</span>

- Exécute un script en affichant chaque commande avant de l'exécuter :

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/script.zsh</span>

- Démarre une session shell interactive en mode verbeux, qui affiche chaque commande avant de l'exécuter :

`zsh --verbose`

- Exécute une commande spécifique dans `zsh` sans motifs génériques d'expansion des noms de fichier :

`noglob "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`
