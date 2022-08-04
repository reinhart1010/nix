---
layout: page
title: common/tldr (français)
description: "Affiche des pages d'aide simples pour les outils en ligne de commande, depuis le projet `tldr-pages`."
content_hash: 095f8890bf3cf4e4a96e7207b2d0b7209a64a3d6
related_topics:
  - title: Deutsch version
    url: /de/common/tldr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tldr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/tldr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tldr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tldr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tldr.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/tldr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tldr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tldr.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/tldr.html
    icon: bi bi-globe
---
# tldr

Affiche des pages d'aide simples pour les outils en ligne de commande, depuis le projet `tldr-pages`.
Plus d'informations : <https://tldr.sh>.

- Affiche la page tldr d'une commande (indice : c'est comme ça que vous êtes arrivé ici !) :

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Affiche la page tldr de `cd`, en forçant la plateforme par défaut :

`tldr -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android|linux|osx|sunos|windows</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cd</span>

- Affiche la page tldr d'une sous-commande :

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git-checkout</span>

- Met à jour les pages enregistrées localement (si le client supporte la mise en cache) :

`tldr -u`
