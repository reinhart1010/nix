---
layout: page
title: common/adb (português (Brasil))
description: "Android Debug Bridge: Comunica com uma instância do emulador Android emulator ou dispositivos conectados."
content_hash: 235ad4d61e58488a30995f3967fd922b1bcbcd2d
related_topics:
  - title: English version
    url: /en/common/adb.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb.html
    icon: bi bi-globe
---
# adb

Android Debug Bridge: Comunica com uma instância do emulador Android emulator ou dispositivos conectados.
Alguns subcomandos tais como `adb shell` possuem sua própria documentação de uso.
Mais informações: <https://developer.android.com/studio/command-line/adb>.

- Checa se o servidor adb está em execução e o iniciar:

`adb start-server`

- Encerra o processo do servidor adb:

`adb kill-server`

- Inicia uma shell remota no emulador/dispositivo desejado:

`adb shell`

- Instala um app Android no emulador/dispositivo:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.apk</span>

- Copia um arquivo/pasta do dispositivo desejado:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_pasta_no_dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/pasta_de_destino_local</span>

- Copia um arquivo/pasta para o dispositivo desejado:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_pasta_local</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/pasta_de_destino_no_dispositivo</span>

- Exibe a lista de dispositivos conectados:

`adb devices`
