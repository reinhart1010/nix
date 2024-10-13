---
layout: page
title: common/ansiweather (français)
description: "Un script Shell pour afficher les conditions météo actuelles dans votre terminal."
content_hash: 9721b9310fe20bb5231a059469952aeedc95cfaa
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/ansiweather.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansiweather.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansiweather.html
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
tldri18n_status: 2
---
# ansiweather

Un script Shell pour afficher les conditions météo actuelles dans votre terminal.
Plus d'informations : <https://github.com/fcambus/ansiweather>.

- Affiche une prévision avec le système métrique pour les 7 prochains jours dans la ville de Paris, France :

`ansiweather -u metric -f 7 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Paris,FR</span>

- Affiche une prévision avec des symboles et les données d'ensoleillement pour votre position actuelle :

`ansiweather -F -s true -d true`

- Affiche une prévision avec les données sur le vent et l'humidité pour votre position actuelle :

`ansiweather -w true -h true`
