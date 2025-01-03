---
layout: page
title: common/dart (português (Brasil))
description: "A ferramenta para gerenciar projetos Dart."
content_hash: dbc8902597391771a7bb34d68573033ade97d3b1
last_modified_at: 2025-01-03
related_topics:
  - title: Deutsch version
    url: /de/common/dart.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dart.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dart.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dart.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dart

A ferramenta para gerenciar projetos Dart.
Mais informações: <https://dart.dev/tools/dart-tool>.

- Inicializa um novo projeto Dart em um diretório com o mesmo nome:

`dart create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_projeto</span>

- Executa um arquivo Dart:

`dart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.dart</span>

- Baixa as dependências do projeto atual:

`dart pub get`

- Executa testes de unidade para o projeto atual:

`dart test`

- Atualiza as dependências de um projeto desatualizado para oferecer suporte à segurança nula:

`dart pub upgrade --null-safety`

- Compila um arquivo Dart para um binário nativo:

`dart compile exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.dart</span>

- Aplica correções automáticas ao projeto atual:

`dart fix --apply`
