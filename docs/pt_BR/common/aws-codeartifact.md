---
layout: page
title: common/aws-codeartifact (português (Brasil))
description: "Interface de linha de comando para o AWS CodeArtifact."
content_hash: c0016dd7c89d3039e88204d2335918206250df29
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-codeartifact.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws codeartifact

Interface de linha de comando para o AWS CodeArtifact.
O CodeArtifact permite armazenar artefatos usando gerenciadores de pacotes populares e criar ferramentas como Maven, Gradle, npm, Yarn, Twine, pip e NuGet.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- Lista domínios disponíveis para a sua conta da AWS:

`aws codeartifact list-domains`

- Gera credenciais para um gerenciador de pacote específico (p.e.: npm, pip):

`aws codeartifact login --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gerenciador_de_pacotes</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seu_domínio</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_repositório</span>

- Recupera a URL do endpoint de um repositório do CodeArtifact:

`aws codeartifact get-repository-endpoint --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seu_domínio</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_repositório</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pypi|maven|nuget|generic</span>

- Lista todos os comandos disponíveis para o CodeArtifact:

`aws codeartifact help`

- Exibe ajuda específica para um subcomando do CodeArtifact:

`aws ec2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` help`
