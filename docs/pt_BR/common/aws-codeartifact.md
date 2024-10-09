---
layout: page
title: common/aws-codeartifact (português (Brasil))
description: "Gerencia repositórios, domínios, pacotes, versões de pacotes e ativos do CodeArtifact."
content_hash: 31c8387c4567853c8a892b20dfcc061b108fe3cc
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/common/aws-codeartifact.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-codeartifact.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws codeartifact

Gerencia repositórios, domínios, pacotes, versões de pacotes e ativos do CodeArtifact.
O CodeArtifact é um repositório de artefatos compatível com gerenciadores de pacotes populares e ferramentas de construção como Maven, Gradle, npm, Yarn, Twine, pip, NuGet e SwiftPM.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- Lista domínios disponíveis para a sua conta da AWS:

`aws codeartifact list-domains`

- Gera credenciais para um gerenciador de pacote específico:

`aws codeartifact login --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pip|twine</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seu_domínio</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_repositório</span>

- Recupera a URL do endpoint de um repositório do CodeArtifact:

`aws codeartifact get-repository-endpoint --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seu_domínio</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_repositório</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pypi|maven|nuget|generic</span>

- Exibe ajuda:

`aws codeartifact help`

- Exibe ajuda para um subcomando específico:

`aws codeartifact `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` help`
