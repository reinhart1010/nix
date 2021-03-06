---
layout: page
title: common/flutter (português (Brasil))
description: "SDK livre e open source do Google para desenvolvimento de aplicativos mobile cross-platform."
content_hash: f3c8c829787bf379435f28dfdd9425501f29e259
related_topics:
  - title: English version
    url: /en/common/flutter.html
    icon: bi bi-globe
---
# flutter

SDK livre e open source do Google para desenvolvimento de aplicativos mobile cross-platform.
Mais informações: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- Mostra ajuda sobre algum comando específico:

`flutter help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Verifica se todas as ferramentas externas necessárias estão instaladas:

`flutter doctor`

- Lista ou muda o channel do Flutter:

`flutter channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|beta|dev|master</span>

- Executa o projeto Flutter em todos os emuladores ativos ou devices conectados:

`flutter run -d all`

- Instala todas as dependências definidas no `pubspec.yaml`:

`flutter pub get`

- Executa todos os testes no terminal a partir da raíz do projeto:

`flutter test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test/example_test.dart</span>

- Buildar APK de release direcionado aos mais modernos smartphones:

`flutter build apk --target-platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android-arm</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android-arm64</span>
