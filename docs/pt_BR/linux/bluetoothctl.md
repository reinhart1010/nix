---
layout: page
title: linux/bluetoothctl (português (Brasil))
description: "Gerencia dispositivos Bluetooth a partir da linha de comando."
content_hash: f9b52f10c2bb948fd2ab099b580b4994b1d9eb28
related_topics:
  - title: English version
    url: /en/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bluetoothctl

Gerencia dispositivos Bluetooth a partir da linha de comando.
Mais informações: <https://bitbucket.org/serkanp/bluetoothctl>.

- Inicia o shell `bluetoothctl`:

`bluetoothctl`

- Lista todos os dispositivos conhecidos:

`bluetoothctl devices`

- Liga ou desliga o controlador Bluetooth:

`bluetoothctl power `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Emparelha com um dispositivo:

`bluetoothctl pair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço_mac</span>

- Remove um dispositivo:

`bluetoothctl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço_mac</span>

- Conecta a um dispositivo pareado:

`bluetoothctl connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço_mac</span>

- Desconecta um dispositivo pareado:

`bluetoothctl disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço_mac</span>

- Exibe ajuda:

`bluetoothctl help`
