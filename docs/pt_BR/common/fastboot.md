---
layout: page
title: common/fastboot (português (Brasil))
description: "Se comunica com dispositivos Android conectados quando iniciados no modo _fastboot_ (o único lugar em que `adb` não funciona)."
content_hash: 3296f0ebfb2e767e41affd14449823171b8d9e01
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/fastboot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/fastboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fastboot

Se comunica com dispositivos Android conectados quando iniciados no modo _fastboot_ (o único lugar em que `adb` não funciona).
Mais informações: <https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

- Desbloqueia o bootloader:

`fastboot oem unlock`

- Bloqueia o bootloader novamente:

`fastboot oem lock`

- Reinicia o dispositivo no modo fastboot para o modo fastboot novamente:

`fastboot reboot bootloader`

- Flasheia uma imagem:

`fastboot flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.img</span>

- Flasheia uma imagem de _recovery_ customizada:

`fastboot flash recovery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.img</span>

- Exibe os dispositivos conectados:

`fastboot devices`

- Mostra todas as informações de um dispositivo:

`fastboot getvar all`
