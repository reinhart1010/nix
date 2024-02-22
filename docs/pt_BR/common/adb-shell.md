---
layout: page
title: common/adb-shell (português (Brasil))
description: "Android Debug Bridge Shell: Executar remotamente comandos shell em instâncias do emulador Android ou dispositivos Android conectados."
content_hash: e84914b62274a63784c53cfbdf564889c547ae2c
last_modified_at: 2024-02-22
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-shell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-shell.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/adb-shell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-shell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb shell

Android Debug Bridge Shell: Executar remotamente comandos shell em instâncias do emulador Android ou dispositivos Android conectados.
Mais informações: <https://developer.android.com/tools/adb>.

- Inicia um shell interativo remoto no emulador/dispositivo:

`adb shell`

- Obtém todas as propriedades do emulador ou dispositivo:

`adb shell getprop`

- Reverte todas as permissões de tempo de execução para o padrão:

`adb shell pm reset-permissions`

- Revoga uma permissão perigosa para um aplicação:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permissao</span>

- Aciona um evento:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keycode</span>

- Limpa os dados da aplicação no emulador/dispositivo:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Inicia uma atividade no emulator/dispositivo:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atividade</span>

- Inicia atividade "home" no emulator/dispositivo:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
