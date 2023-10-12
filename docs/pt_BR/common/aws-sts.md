---
layout: page
title: common/aws-sts (português (Brasil))
description: "Serviço de Token de Segurança (STS) que permite solicitar credenciais temporárias para usuários (IAM) ou federados."
content_hash: 531c68f17e9f6aeb22eeca9521b1ffcc196ac80b
last_modified_at: 2023-10-12
related_topics:
  - title: English version
    url: /en/common/aws-sts.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws sts

Serviço de Token de Segurança (STS) que permite solicitar credenciais temporárias para usuários (IAM) ou federados.
Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- Obtém credenciais temporárias para acessar recursos AWS específicos:

`aws sts assume-role --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_do_papel_aws</span>

- Obtém um usuário IAM ou papel que foi usado para chamar a operação:

`aws sts get-caller-identity`
