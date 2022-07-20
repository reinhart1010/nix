---
layout: page
title: common/ansiweather (français)
description: "Un script Shell pour afficher les conditions météo actuelles dans votre terminal."
content_hash: e0c2b5f9c5806ce7da3f3fa0602652044437aaed
related_topics:
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansiweather.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansiweather.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansiweather.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansiweather

Un script Shell pour afficher les conditions météo actuelles dans votre terminal.
Plus d'informations : <https://github.com/fcambus/ansiweather>.

- Affiche une prévision avec le système métrique pour les 5 prochains jours dans la ville de Paris, France :

`ansiweather -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Paris,FR</span>

- Affiche une prévision avec des symboles et les données d'ensoleillement pour votre position actuelle :

`ansiweather -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>

- Affiche une prévision avec les données sur le vent et l'humidité pour votre position actuelle :

`ansiweather -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
