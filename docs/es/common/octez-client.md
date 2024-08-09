---
layout: page
title: common/octez-client (español)
description: "Interactúa con la blockchain de Tezos."
content_hash: 958857c75a48c4065a85f5b0e572d08662ee6432
last_modified_at: 2024-08-09
related_topics:
  - title: English version
    url: /en/common/octez-client.html
    icon: bi bi-globe
tldri18n_status: 2
---
# octez-client

Interactúa con la blockchain de Tezos.
Más información: <https://tezos.gitlab.io/introduction/howtouse.html#client>.

- Configura el cliente con una conexión a un nodo RPC de Tezos como <https://rpc.ghostnet.teztnets.com>:

`octez-client -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint</span>` config update`

- Crea una cuenta y le asigna un alias local:

`octez-client gen keys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>

- Obtén el saldo de una cuenta por alias o dirección:

`octez-client get balance for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_o_dirección</span>

- Transfiere tez a otra cuenta:

`octez-client transfer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|address</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|address</span>

- Crea (despliega) un contrato inteligente, le asignar un alias local y establece su almacenamiento inicial como un valor codificado por Michelson:

`octez-client originate contract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>` transferring `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|address</span>` running `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_de_origen.tz</span>` --init "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">almacenamiento_inicial</span>`" --burn_cap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Llama a un contrato inteligente por su alias o dirección y pasa un parámetro codificado por Michelson:

`octez-client transfer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|address</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contract</span>` --entrypoint "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entrypoint</span>`" --arg "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parámetro</span>`" --burn-cap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Muestra ayuda:

`octez-client man`
