---
layout: page
title: common/aws (português (Brasil))
description: "A interface de linha de comando oficial para o Amazon Web Services."
content_hash: d4859c7a5aa8af3d91f45146bd35ce1db43c4800
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/aws.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/aws.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/aws.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws

A interface de linha de comando oficial para o Amazon Web Services.
Passo-a-passo, Single Sign-On (SSO), autocompletar de recursos e opções de YAML somente na v2.
Alguns subcomandos como `s3` tem sua própia documentação de uso.
Mais informações: <https://aws.amazon.com/cli>.

- Configura a linha de comando da AWS:

`aws configure wizard`

- Configura a linha de comando da AWS usando o SSO:

`aws configure sso`

- Obtenha a informações da identidade usada (útil para analisar problemas de permissão):

`aws sts get-caller-identity`

- Lista recursos da AWS em uma região em yaml:

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sa-east-1</span>` --output yaml`

- Usa prompt de comando para ajuda com o preenchimento:

`aws iam create-user --cli-auto-prompt`

- Usa um passo-a-passo interativo para um recurso da AWS:

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova-tabela</span>

- Gera um arquivo esqueleo em JSON (útil para ser usado em infraestrutura como código):

`aws dynamodb update-table --generate-cli-skeleton`

- Veja o texto de ajuda para o comando da AWS:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` help`
