---
layout: page
title: common/aws-iam (español)
description: "CLI para AWS IAM."
content_hash: bc842207882d0b7cf7e281ff943ad36025b0086b
last_modified_at: 2023-05-19
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws iam

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

- Obtiene los usuarios de un grupo:

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_grupo</span>

- Describe una política IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_politica</span>

- Lista claves de acceso:

`aws iam list-access-keys`

- Lista claves de acceso para un usuario específico:

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>
