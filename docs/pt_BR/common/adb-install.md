---
layout: page
title: common/adb-install (português (Brasil))
description: "Android Debug Bridge Install: Instalar apps em uma instância do Android emulator ou dispositivos conectados."
content_hash: 29a0e55c8a07dc0547d90a3e98bafdd8be4a9efd
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-install.html
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
tldri18n_status: 2
---
# adb install

Android Debug Bridge Install: Instalar apps em uma instância do Android emulator ou dispositivos conectados.
Mais informações: <https://developer.android.com/studio/command-line/adb>.

- Instala um app Android em um emulador/dispositivo:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>

- Instala um app Android em um emulador/dispositivo específico (sobrepõe `$ANDROID_SERIAL`):

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_serie</span>` install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>

- Reinstala um app existente, mantendo seus dados:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>

- Instala um app Android permitindo um downgrade de versão de código (apenas pacotes depuráveis):

`adb install -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>

- Concede todas as permissões listadas no manifesto do app:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>

- Atualiza rapidamente um app já instalado atualizando apenas as partes do APK que mudaram:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>
