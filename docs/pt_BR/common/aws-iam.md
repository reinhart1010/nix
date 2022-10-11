---
layout: page
title: common/aws-iam (português (Brasil))
description: "CLI for AWS IAM."
content_hash: 9142564b62357adfbe45e03dbd0147329497b702
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws iam

CLI for AWS IAM.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Exibe a página de ajuda do `aws iam` (incluindo todos os comandos iam disponíveis):

`aws iam help`

- Lista os usuários:

`aws iam list-users`

- Lista as políticas:

`aws iam list-policies`

- Lista os grupos:

`aws iam list-groups`

- Obtém os usuários de um grupo:

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_grupo</span>

- Descreve uma política IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_política</span>

- Lista as chaves de acesso:

`aws iam list-access-keys`

- Lista as chaves de acesso para um usuário específico:

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>
