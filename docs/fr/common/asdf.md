---
layout: page
title: common/asdf (français)
description: "Interface en ligne de commande pour gérer les versions de différents paquets."
content_hash: e1db78069501bbeebbcae0071e82fd4f9159c360
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/asdf.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/asdf.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asdf.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/asdf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asdf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asdf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asdf

Interface en ligne de commande pour gérer les versions de différents paquets.
Plus d'informations : <https://asdf-vm.com>.

- Liste toutes les extensions disponibles :

`asdf plugin list all`

- Installe une extension :

`asdf plugin add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Liste toutes les versions disponible d'un paquet :

`asdf list all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Installe une version spécifique d'un paquet :

`asdf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Fixe au global une version d'un paquet :

`asdf global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Fix en local la version d'un paquet :

`asdf local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
