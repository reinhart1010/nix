---
layout: page
title: common/adb-install (português (Brasil))
description: "Android Debug Bridge Install: Instalar apps em uma instância do Android emulator ou dispositivos conectados."
content_hash: 019fb190b363cb8e56a286fd020c0e1dd85f3bb1
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-install.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-install.html
    icon: bi bi-globe
---
# adb install

Android Debug Bridge Install: Instalar apps em uma instância do Android emulator ou dispositivos conectados.
Mais informações: <https://developer.android.com/studio/command-line/adb>.

- Instala um app Android em um emulador/dispositivo:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>

- Reinstala um app existente, mantendo seus dados:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>

- Concede todas as permissões listadas no manifesto do app:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>

- Atualiza rapidamente um app já instalado atualizando apenas as partes do APK que mudaram:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>
