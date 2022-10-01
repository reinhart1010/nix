---
layout: page
title: common/balena (français)
description: "Interagis avec balenaCloud, openBAlena et l'API balena depuis la ligne de commande."
content_hash: 060a6ddf5764cf0d6fb8cbfb1665f714aad0a0ea
related_topics:
  - title: English version
    url: /en/common/balena.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/balena.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># balena

Interagis avec balenaCloud, openBAlena et l'API balena depuis la ligne de commande.
Plus d'informations : <https://www.balena.io/docs/reference/cli/>.

- Connexion à balenaCloud :

`balena login`

- Crée une application balenaCloud ou openBalena :

`balena app create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_application</span>

- Affiche toutes les applications balenaCloud ou openBalena du compte :

`balena apps`

- Affiche tous les appareils associés au compte balenaCloud ou openBalena :

`balena devices`

- Flash une image balenaOS sur l'appareil local :

`balena local flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/balenaos.img</span>` --drive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localisation_de_l_appareil</span>
