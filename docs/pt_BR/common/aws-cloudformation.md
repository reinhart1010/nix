---
layout: page
title: common/aws-cloudformation (português (Brasil))
description: "Modela, provisiona e gerencia recursos AWS, e de terceiros, ao tratar a infraestrutura como código."
content_hash: 361fb0f550f721479d9543fb0b2c89e40a9d88b4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/aws-cloudformation.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-cloudformation.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-cloudformation.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws cloudformation

Modela, provisiona e gerencia recursos AWS, e de terceiros, ao tratar a infraestrutura como código.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html>.

- Cria uma pilha a partir de um arquivo de modelo:

`aws cloudformation create-stack --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome-da-pilha</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">região</span>` --template-body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://caminho/para/arquivo.yml</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>

- Deleta uma pilha:

`aws cloudformation delete-stack --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome-da-pilha</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>

- Lista todas as pilhas:

`aws cloudformation list-stacks --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>

- Lista todas as pilhas em execução:

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>

- Verifica o status de uma pilha:

`aws cloudformation describe-stacks --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id-da-pilha</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>

- Inicia a detecção de desvio para uma pilha:

`aws cloudformation detect-stack-drift --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id-da-pilha</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>

- Verifica o status de desvio de uma pilha usando 'StackDriftDetectionId' do resultado do comando anterior:

`aws cloudformation describe-stack-resource-drifts --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack-drift-detection-id</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>
