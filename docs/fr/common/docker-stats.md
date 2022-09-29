---
layout: page
title: common/docker-stats (français)
description: "Affiché un flux en direct des statistiques d'utilisation des ressources pour les conteneurs."
content_hash: d6fa0e05f8e009c5825cb4110dd667a574db825c
related_topics:
  - title: Deutsch version
    url: /de/common/docker-stats.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-stats.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-stats.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-stats.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker stats

Affiché un flux en direct des statistiques d'utilisation des ressources pour les conteneurs.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/stats/>.

- Afficher un flux en direct des statistiques d'utilisation des ressources pour tous les conteneurs :

`docker stats`

- Afficher un flux en direct des statistiques d'utilisation des ressources pour un ou plusieurs conteneurs séparés par des espaces :

`docker stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>

- Change le format de sortie pour afficher l'utilisation CPU du conteneur en pourcentage :

`docker stats --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Name</span>`:\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.CPUPerc</span>`"`

- Afficher les statistiques d'utilisation des ressources pour tous les conteneurs (y compris ceux qui ne sont pas en cours d'exécution) :

`docker stats --all`

- Desactiver le flux en direct des statistiques d'utilisation des ressources et afficher les statistiques une seule fois :

`docker stats --no-stream`
