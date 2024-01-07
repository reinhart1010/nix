---
layout: page
title: common/aws-iam (español)
description: "CLI para AWS IAM."
content_hash: b3141ca576cc6c3ae8d8cbb89fdd0c1d91f010d5
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/aws-iam.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-iam.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-iam.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-iam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws iam

CLI para AWS IAM.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Muestra la página de ayuda de `aws iam` (incluyendo todos los comandos iam disponibles):

`aws iam help`

- Lista usuarios:

`aws iam list-users`

- Lista políticas:

`aws iam list-policies`

- Lista grupos:

`aws iam list-groups`

- Obtén los usuarios de un grupo:

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_grupo</span>

- Describe una política IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_politica</span>

- Lista claves de acceso:

`aws iam list-access-keys`

- Lista claves de acceso para un usuario específico:

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>
