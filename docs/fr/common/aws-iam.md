---
layout: page
title: common/aws-iam (français)
description: "CLI pour AWS IAM."
content_hash: 13230e8ad5f3a93404f3d7889aa699e497aa5b41
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/aws-iam.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-iam.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-iam.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-iam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws iam

CLI pour AWS IAM.
Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Affiche la page d'aide pour `aws iam` (avec toutes les commandes iam disponibles) :

`aws iam help`

- Liste les utilisateurs :

`aws iam list-users`

- Liste les politiques :

`aws iam list-policies`

- Liste les groupes :

`aws iam list-groups`

- Récupère les utilisateurs dans un groupe :

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_groupe</span>

- Décris une politique IAM :

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_politique</span>

- Liste les clés d’accès :

`aws iam list-access-keys`

- Liste les clés d'accès pour un utilisateur spécifique :

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>
