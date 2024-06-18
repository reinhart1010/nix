---
layout: page
title: common/aws-iam (español)
description: "Interactúa con el Manejo de Identidad y Acceso (o \"IAM\" en inglés), un servicio web para controlar seguramente el acceso a servicios de AWS."
content_hash: 564b59be73dff78f00784b9c950a58177424c55d
last_modified_at: 2024-06-18
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

Interactúa con el Manejo de Identidad y Acceso (o "IAM" en inglés), un servicio web para controlar seguramente el acceso a servicios de AWS.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Lista usuarios:

`aws iam list-users`

- Lista políticas:

`aws iam list-policies`

- Lista grupos:

`aws iam list-groups`

- Obtén los usuarios en un grupo:

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_grupo</span>

- Describe una política IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_política</span>

- Lista claves de acceso:

`aws iam list-access-keys`

- Lista claves de acceso para un usuario específico:

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>

- Muestra ayuda:

`aws iam help`
