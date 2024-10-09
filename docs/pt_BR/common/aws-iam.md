---
layout: page
title: common/aws-iam (português (Brasil))
description: "Interage com o Identity and Access Management (IAM), um serviço web para controlar com segurança o acesso aos serviços da AWS."
content_hash: 00dc5e45e9541e071271d98c1525fbc4defe7049
last_modified_at: 2024-10-09
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
  - title: français version
    url: /fr/common/aws-iam.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-iam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws iam

Interage com o Identity and Access Management (IAM), um serviço web para controlar com segurança o acesso aos serviços da AWS.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Lista os usuários:

`aws iam list-users`

- Lista as políticas:

`aws iam list-policies`

- Lista os grupos:

`aws iam list-groups`

- Obtém os usuários de um grupo:

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_grupo</span>

- Descreve uma política do IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_política</span>

- Lista as chaves de acesso:

`aws iam list-access-keys`

- Lista as chaves de acesso para um usuário específico:

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>

- Exibe ajuda:

`aws iam help`
