---
layout: page
title: common/aws-cur (français)
description: "Crée, requête et supprime des rapports de définition d'utilisation AWS."
content_hash: c3b1bb008d0ca423e2a8b561c17d91118cc8d52b
related_topics:
  - title: English version
    url: /en/common/aws-cur.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-cur.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws cur

Crée, requête et supprime des rapports de définition d'utilisation AWS.
Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- Créé un rapport de définition de coût et d'utilisation AWS depuis un fichier JSON :

`aws cur put-report-definition --report-definition file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/rapport_de_définition.json</span>

- Liste les rapports de définition définis pour le compte connecté :

`aws cur describe-report-definitions`

- Supprime un rapport de définition d'utilisation :

`aws cur --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region_aws</span>` delete-report-definition --report-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rapport</span>
