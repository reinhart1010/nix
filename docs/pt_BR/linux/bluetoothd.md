---
layout: page
title: linux/bluetoothd (português (Brasil))
description: "Daemon para gerenciar dispositivos Bluetooth."
content_hash: 3b8240ab0e9feecf24f18f422f00fa25e14ea76d
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/bluetoothd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bluetoothd

Daemon para gerenciar dispositivos Bluetooth.
Mais informações: <https://manned.org/bluetoothd>.

- Inicia o daemon:

`bluetoothd`

- Inicia o daemon, registrando em `stdout`:

`bluetoothd --nodetach`

- Inicia o daemon com um arquivo de configuração específico (`/etc/bluetooth/main.conf` por padrão):

`bluetoothd --configfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Inicia o daemon com saída verbosa em `stderr`:

`bluetoothd --debug`

- Inicia o daemon com saída verbosa proveniente de arquivos específicos na fonte bluetoothd ou plugins:

`bluetoothd --debug=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo3</span>
