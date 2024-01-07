---
layout: page
title: common/flutter (português (Brasil))
description: "SDK livre e open source do Google para desenvolvimento de aplicativos mobile cross-platform."
content_hash: 4b3a35a1b00328542b5cb19d6c7fc4db15f9ba47
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/flutter.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/flutter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flutter

SDK livre e open source do Google para desenvolvimento de aplicativos mobile cross-platform.
Mais informações: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- Inicializa um novo projeto Flutter em um diretório de mesmo nome:

`flutter create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_projeto</span>

- Verifica se todas as ferramentas externas necessárias estão instaladas:

`flutter doctor`

- Lista ou muda o channel do Flutter:

`flutter channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|beta|dev|master</span>

- Executa o projeto Flutter em todos os emuladores ativos ou devices conectados:

`flutter run -d all`

- Executa todos os testes no terminal a partir da raíz do projeto:

`flutter test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test/example_test.dart</span>

- Builda APK de release direcionado aos mais modernos smartphones:

`flutter build apk --target-platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android-arm</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android-arm64</span>

- Mostra ajuda sobre algum comando específico:

`flutter help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
