---
layout: page
title: common/bitcoind (español)
description: "Daemon de Bitcoin Core."
content_hash: 35682e2802a3ea1e29d982d8eb1f4d3563f57674
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/bitcoind.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bitcoind

Daemon de Bitcoin Core.
Utiliza la configuración definida en `bitcoin.conf`.
Más información: <https://manned.org/bitcoind>.

- Inicia el daemon Bitcoin Core (en primer plano):

`bitcoind`

- Inicia el daemon Bitcoin Core en segundo plano (usa `bitcoin-cli stop` para detenerlo):

`bitcoind -daemon`

- Inicia el daemon Bitcoin Core en una red específica:

`bitcoind -chain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|test|signet|regtest</span>

- Inicia el daemon Bitcoin Core usando un archivo de configuración y directorio de datos específicos:

`bitcoind -conf=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/bitcoin.conf</span>` -datadir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>
