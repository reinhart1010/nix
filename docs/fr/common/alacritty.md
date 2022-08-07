---
layout: page
title: common/alacritty (français)
description: "Emulateur de terminal propulsé par GPU, Multi-plateforme."
content_hash: c68e4ed934b525e7f35951756293c475cbb666c0
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alacritty.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alacritty.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alacritty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alacritty.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alacritty.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># alacritty

Emulateur de terminal propulsé par GPU, Multi-plateforme.
Plus d'informations : <https://github.com/alacritty/alacritty>.

- Ouvre une nouvelle fenêtre Alacritty :

`alacritty`

- Lance dans un dossier spécifique :

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Lance une commande dans une nouvelle fenêtre Alacritty :

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Utilise un autre fichier de configuration (le fichier par défault étant `$XDG_CONFIG_HOME/alacritty/alacritty.yml`) :

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/config.yml</span>

- Lance avec la mise à jour en live dès que la configuration est modifiée ( peu également être activé par défaut dans `alacritty.yml`) :

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/config.yml</span>
