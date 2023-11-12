---
layout: page
title: common/aws-ecr (português (Brasil))
description: "Enviar, buscar, e gerenciar imagens de container."
content_hash: a2a190d89d7c77bc3ae5217a78f44aca63d4c013
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-ecr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-ecr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ecr

Enviar, buscar, e gerenciar imagens de container.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>.

- Autentica o docker com o registro default (nome do usuário na AWS):

`aws ecr get-login-password --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker login</span>` --username AWS --password-stdin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>`.dkr.ecr.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`.amazonaws.com`

- Cria um repositório:

`aws ecr create-repository --repository-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --image-scanning-configuration scanOnPush=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>

- Cria uma tag em uma imagem local para o ECR:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>`.dkr.ecr.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Envia uma imagem para um repositório:

`docker push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>`.dkr.ecr.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Busca a imagem de um repositório:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>`.dkr.ecr.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Apaga uma imagem de um repositório:

`aws ecr batch-delete-image  --repository-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repositório</span>` --image-ids imageTag=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest</span>

- Apaga um repositório:

`aws ecr delete-repository --repository-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repositório</span>` --force`

- Lista as imagens de um repositório:

`aws ecr list-images --repository-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repositório</span>
