---
layout: page
title: common/aws-glue (français)
description: "CLI pour AWS Glue."
content_hash: ea2df6b64ffd49959b6041f115f2db2a65c7e083
related_topics:
  - title: English version
    url: /en/common/aws-glue.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws glue

CLI pour AWS Glue.
Définie un endpoint publique pour le service AWS Glue.
Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Liste les tâches :

`aws glue list-jobs`

- Démarre une tâche :

`aws glue start-job-run --job-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_tâche</span>

- Démarre un flux de travail :

`aws glue start-workflow-run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_flux_de_travail</span>

- Liste les déclencheurs :

`aws glue list-triggers`

- Démarre un déclencheur :

`aws glue start-trigger --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_déclencheur</span>

- Créé un endpoint de développement :

`aws glue create-dev-endpoint --endpoint-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rôle_arn_utilisé_par_l_endpoint</span>
