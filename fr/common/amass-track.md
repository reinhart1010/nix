---
layout: page
title: common/amass-track (français)
description: "Traque les différences entre les énumérations d'un même domaine."
content_hash: 83e6801e39535fede9afce5d64fe9b888acc2d9e
related_topics:
  - title: English version
    url: /en/common/amass-track.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass track

Traque les différences entre les énumérations d'un même domaine.
Plus d'informations : <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>.

- Affiche la différence entre les deux dernières énumérations d'un domaine donné :

`amass track -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la_base_de_données</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>` -last 2`

- Affiche la différence entre un certain moment dans le temps et la dernière énumération :

`amass track -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la_base_de_données</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>` -since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01/02 15:04:05 2006 MST</span>
